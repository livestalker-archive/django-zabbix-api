from django.db.models.sql.compiler import SQLCompiler as BaseSQLCompiler
from django.db.models.sql.constants import SINGLE, MULTI, CURSOR, NO_RESULTS
from django.core.exceptions import EmptyResultSet
from jsonrpcdb.error import ProgrammingError

SELECT_METHOD = 'get'


class SQLCompiler(BaseSQLCompiler):
    def __init__(self, query, connection, using):
        super(SQLCompiler, self).__init__(query, connection, using)

    def execute_sql(self, result_type=MULTI, chunked_fetch=False):
        cursor = self.connection.cursor()
        if not result_type:
            cursor.close()
            return
        try:
            sql, params = self.as_sql()
            if not sql:
                raise EmptyResultSet
        except EmptyResultSet:
            if result_type == MULTI:
                return iter([])
            else:
                return
        try:
            cursor.execute(sql, params)
        except Exception as original_eception:
            try:
                cursor.close()
            except Exception:
                pass
            raise original_eception

        if result_type == CURSOR:
            return cursor
        if result_type == SINGLE:
            try:
                val = cursor.fetchone()
                if val:
                    return val[0:self.col_count]
                return val
            finally:
                cursor.close()

        result = cursor_iter(cursor, self._get_field_list(), self.col_count)
        return result

    def as_sql(self, with_limits=True, with_col_aliases=False):
        extra_select, order_by, group_by = self.pre_sql_setup()
        distinct_fields = self.get_distinct()

        # This must come after 'select', 'ordering', and 'distinct' -- see
        # docstring of get_from_clause() for details.
        from_, f_params = self.get_from_clause()
        if len(from_) > 1:
            raise ProgrammingError("Can not select from multiply tables.")
        sql = '{}.{}'.format(from_[0], SELECT_METHOD)
        params = {}
        return sql, params

    def results_iter(self, results=None):
        if results is None:
            results = self.execute_sql(MULTI)
        fields = [s[0] for s in self.select[0:self.col_count]]
        converters = self.get_converters(fields)
        for rows in results:
            for row in rows:
                if converters:
                    row = self.apply_converters(row, converters)
                yield row

    def _get_field_list(self):
        return [(k[0].field.column, k[0].field) for k in self.select[0:self.col_count]]


def cursor_iter(cursor, fields, col_count):
    try:
        results = iter((lambda: cursor.fetchall()), [])
        for rows in results:
            remap_rows = remap_results(rows, fields)
            yield [r[0:col_count] for r in remap_rows]
    finally:
        cursor.close()


def remap_results(rows, fields):
    return [tuple([k[1].to_python(d.get(k[0], None)) for k in fields]) for d in rows]

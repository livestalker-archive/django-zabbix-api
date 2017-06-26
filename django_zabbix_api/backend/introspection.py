from django.db.backends.base.introspection import BaseDatabaseIntrospection


class DatabaseIntrospection(BaseDatabaseIntrospection):
    def get_constraints(self, cursor, table_name):
        pass

    def get_key_columns(self, cursor, table_name):
        pass

    def get_table_list(self, cursor):
        pass

    def get_indexes(self, cursor, table_name):
        pass

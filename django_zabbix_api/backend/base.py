"""
Zabbix API like database backend for Django.

Requires jsonrpcdb: https://pypi.python.org/pypi/jsonrpcdb
"""
from django.core.exceptions import ImproperlyConfigured
from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.backends.base.client import BaseDatabaseClient
from django.db.backends.base.creation import BaseDatabaseCreation

try:
    import jsonrpcdb as Database
except ImportError as e:
    raise ImproperlyConfigured("Error loading jsonrpcdb module: %s" % e)

from .features import DatabaseFeatures
from .introspection import DatabaseIntrospection
from .operations import DatabaseOperations
from .schema import DatabaseSchemaEditor


class DatabaseWrapper(BaseDatabaseWrapper):
    Database = Database

    SchemaEditorClass = DatabaseSchemaEditor
    client_class = BaseDatabaseClient
    """This class should encapsulate all backend-specific methods for opening a
    client shell. We do not have any shell for json-rpc, so simple use BaseDatabaseClient class."""
    creation_class = BaseDatabaseCreation
    """This class should encapsulate all backend-specific differences that pertain to
    creation and destruction of the database. We can not create/destruct any tables in zabbix via json-rpc.
    So simple use BaseDatabaseCreation."""
    features_class = DatabaseFeatures
    introspection_class = DatabaseIntrospection
    ops_class = DatabaseOperations

    def _start_transaction_under_autocommit(self):
        pass

    def _set_autocommit(self, autocommit):
        pass

    def init_connection_state(self):
        pass

    def is_usable(self):
        pass

    def get_connection_params(self):
        pass

    def create_cursor(self, name=None):
        pass

    def get_new_connection(self, conn_params):
        pass

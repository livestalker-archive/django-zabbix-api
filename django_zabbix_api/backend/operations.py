from django.db.backends.base.operations import BaseDatabaseOperations


class DatabaseOperations(BaseDatabaseOperations):
    compiler_module = 'django_zabbix_api.backend.compiler'

    def quote_name(self, name):
        """We do not need quoting name."""
        return name

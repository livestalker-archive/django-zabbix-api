from django.db import models
from .fields import UnixDateTimeField


class ZUser(models.Model):
    hostid = models.TextField(primary_key=True, editable=False)
    host = models.TextField()
    available = models.IntegerField(editable=False)  # TODO List of values
    description = models.TextField()
    disable_until = UnixDateTimeField(editable=False)  # TODO timestamp
    error = models.TextField(editable=False)
    error_from = UnixDateTimeField(editable=False)  # TODO timestamp
    flags = models.IntegerField(editable=False)  # TODO List of values
    inventory_mode = models.IntegerField()  # TODO List of values
    ipmi_authtype = models.IntegerField()  # TODO List of values
    ipmi_available = models.IntegerField(editable=False)  # TODO List of values
    ipmi_disable_until = UnixDateTimeField(editable=False)  # TODO timestamp
    ipmi_error = models.TextField(editable=False)
    ipmi_errors_from = UnixDateTimeField(editable=False)  # TODO timestamp
    ipmi_password = models.TextField()
    ipmi_privilege = models.IntegerField(editable=False)  # TODO List of values
    ipmi_username = models.TextField()
    jmx_available = models.IntegerField(editable=False)  # TODO List of values
    jmx_disable_until = UnixDateTimeField(editable=False)  # TODO timestamp
    jmx_error = models.TextField(editable=False)  # TODO timestamp
    jmx_errors_from = UnixDateTimeField(editable=False)  # TODO timestamp
    maintenance_from = UnixDateTimeField(editable=False)  # TODO timestamp
    maintenance_status = models.IntegerField(editable=False)  # TODO List of values
    maintenance_type = models.IntegerField(editable=False)  # TODO List of values
    maintenanceid = models.TextField(editable=False)  # TODO timestamp
    name = models.TextField()
    proxy_hostid = models.TextField()
    snmp_available = models.IntegerField(editable=False)  # TODO List of values
    snmp_disable_until = UnixDateTimeField(editable=False)  # TODO timestamp
    snmp_error = models.TextField(editable=False)  # TODO timestamp
    snmp_errors_from = UnixDateTimeField(editable=False)  # TODO timestamp
    status = models.IntegerField()  # TODO List of values
    tls_connect = models.IntegerField()  # TODO List of values
    tls_accept = models.IntegerField()  # TODO List of values
    tls_issuer = models.TextField()
    tls_subject = models.TextField()
    tls_psk_identity = models.TextField()
    tls_psk = models.TextField()

    class Meta:
        db_table = 'host'
        managed = False
        verbose_name = 'host'
        verbose_name_plural = 'hosts'

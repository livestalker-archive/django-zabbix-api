from django.db import models


class ZUser(models.Model):
    hostid = models.CharField(primary_key=True, editable=False)
    host = models.CharField()
    available = models.IntegerField(editable=False)  # TODO List of values
    description = models.CharField()
    disable_until = models.TimeField(editable=False)  # TODO timestamp
    error = models.CharField(editable=False)
    error_from = models.TimeField(editable=False)  # TODO timestamp
    flags = models.IntegerField(editable=False)  # TODO List of values
    inventory_mode = models.IntegerField()  # TODO List of values
    ipmi_authtype = models.IntegerField()  # TODO List of values
    ipmi_available = models.IntegerField(editable=False)  # TODO List of values
    ipmi_disable_until = models.TimeField(editable=False)  # TODO timestamp
    ipmi_error = models.CharField(editable=False)
    ipmi_errors_from = models.TimeField(editable=False)  # TODO timestamp
    ipmi_password = models.CharField()
    ipmi_privilege = models.IntegerField(editable=False)  # TODO List of values
    ipmi_username = models.CharField()
    jmx_available = models.IntegerField(editable=False)  # TODO List of values
    jmx_disable_until = models.TimeField(editable=False)  # TODO timestamp
    jmx_error = models.CharField(editable=False)  # TODO timestamp
    jmx_errors_from = models.TimeField(editable=False)  # TODO timestamp
    maintenance_from = models.TimeField(editable=False)  # TODO timestamp
    maintenance_status = models.IntegerField(editable=False)  # TODO List of values
    maintenance_type = models.IntegerField(editable=False)  # TODO List of values
    maintenanceid = models.CharField(editable=False)  # TODO timestamp
    name = models.CharField()
    proxy_hostid = models.CharField()
    snmp_available = models.IntegerField(editable=False)  # TODO List of values
    snmp_disable_until = models.TimeField(editable=False)  # TODO timestamp
    snmp_error = models.CharField(editable=False)  # TODO timestamp
    snmp_errors_from = models.TimeField(editable=False)  # TODO timestamp
    status = models.IntegerField()  # TODO List of values
    tls_connect = models.IntegerField()  # TODO List of values
    tls_accept = models.IntegerField()  # TODO List of values
    tls_issuer = models.CharField()
    tls_subject = models.CharField()
    tls_psk_identity = models.CharField()
    tls_psk = models.CharField()

    class Meta:
        db_table = 'host'
        managed = False
        verbose_name = 'host'
        verbose_name_plural = 'hosts'

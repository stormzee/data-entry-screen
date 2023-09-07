# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Hospitalization(models.Model):
    dov = models.DateField(db_column='DOV', blank=True, null=True)  # Field name made lowercase.
    pid = models.IntegerField(db_column='PID', primary_key=True)  # Field name made lowercase.
    compno = models.IntegerField(db_column='COMPNO', blank=True, null=True)  # Field name made lowercase.
    pname = models.CharField(db_column='PNAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mname = models.CharField(db_column='MNAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vname = models.CharField(db_column='VNAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    grup = models.CharField(db_column='GRUP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dob = models.DateField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    wt = models.CharField(db_column='WT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hsp1 = models.IntegerField(db_column='HSP1', blank=True, null=True)  # Field name made lowercase.
    hsp2 = models.IntegerField(db_column='HSP2', blank=True, null=True)  # Field name made lowercase.
    hsp3 = models.IntegerField(db_column='HSP3', blank=True, null=True)  # Field name made lowercase.
    hsp4 = models.IntegerField(db_column='HSP4', blank=True, null=True)  # Field name made lowercase.
    hsp5 = models.IntegerField(db_column='HSP5', blank=True, null=True)  # Field name made lowercase.
    hsp6 = models.IntegerField(db_column='HSP6', blank=True, null=True)  # Field name made lowercase.
    hsp7 = models.IntegerField(db_column='HSP7', blank=True, null=True)  # Field name made lowercase.
    hsp8 = models.IntegerField(db_column='HSP8', blank=True, null=True)  # Field name made lowercase.
    hsp9 = models.IntegerField(db_column='HSP9', blank=True, null=True)  # Field name made lowercase.
    hsp10 = models.IntegerField(db_column='HSP10', blank=True, null=True)  # Field name made lowercase.
    hsp11 = models.IntegerField(db_column='HSP11', blank=True, null=True)  # Field name made lowercase.
    hsp12 = models.IntegerField(db_column='HSP12', blank=True, null=True)  # Field name made lowercase.
    hsp13 = models.IntegerField(db_column='HSP13', blank=True, null=True)  # Field name made lowercase.
    hsp14 = models.IntegerField(db_column='HSP14', blank=True, null=True)  # Field name made lowercase.
    doa = models.DateField(db_column='DOA', blank=True, null=True)  # Field name made lowercase.
    doop = models.DateField(db_column='DOOP', blank=True, null=True)  # Field name made lowercase.
    time = models.TimeField(db_column='TIME', blank=True, null=True)  # Field name made lowercase.
    hhosp = models.CharField(db_column='HHOSP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    facloc = models.CharField(db_column='FACLOC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    temp = models.FloatField(db_column='TEMP', blank=True, null=True)  # Field name made lowercase.
    rout = models.IntegerField(db_column='ROUT', blank=True, null=True)  # Field name made lowercase.
    aesi = models.IntegerField(db_column='AESI', blank=True, null=True)  # Field name made lowercase.
    mal = models.IntegerField(db_column='MAL', blank=True, null=True)  # Field name made lowercase.
    rfrm = models.IntegerField(db_column='RFRM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'hospitalization'


class Visit2(models.Model):
    pid = models.IntegerField(db_column='PID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    compno = models.IntegerField(db_column='COMPNO', blank=True, null=True)  # Field name made lowercase.
    vname = models.CharField(db_column='VNAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dob = models.DateField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    cat = models.IntegerField(db_column='CAT', blank=True, null=True)  # Field name made lowercase.
    mpermid = models.IntegerField(db_column='MPERMID', blank=True, null=True)  # Field name made lowercase.
    cpermid = models.IntegerField(db_column='CPERMID', blank=True, null=True)  # Field name made lowercase.
    ccnum = models.IntegerField(db_column='CCNUM', blank=True, null=True)  # Field name made lowercase.
    ccdate = models.DateField(db_column='CCDATE', blank=True, null=True)  # Field name made lowercase.
    sdov = models.DateField(db_column='SDOV', blank=True, null=True)  # Field name made lowercase.
    seen = models.CharField(db_column='SEEN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dor = models.DateField(db_column='DOR', blank=True, null=True)  # Field name made lowercase.
    reason = models.IntegerField(db_column='REASON', blank=True, null=True)  # Field name made lowercase.
    disconti = models.IntegerField(db_column='DISCONTI', blank=True, null=True)  # Field name made lowercase.
    precon = models.IntegerField(db_column='PRECON', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'visit2'

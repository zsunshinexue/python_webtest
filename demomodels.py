# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ApiTestApigrouplevelfirst(models.Model):
    name = models.CharField(max_length=50)
    project = models.ForeignKey('ApiTestProject', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_test_apigrouplevelfirst'


class ApiTestApihead(models.Model):
    name = models.CharField(max_length=1024)
    value = models.CharField(max_length=1024, blank=True, null=True)
    api = models.ForeignKey('ApiTestApiinfo', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_test_apihead'


class ApiTestApiinfo(models.Model):
    name = models.CharField(max_length=50)
    httptype = models.CharField(db_column='httpType', max_length=50)  # Field name made lowercase.
    requesttype = models.CharField(db_column='requestType', max_length=50)  # Field name made lowercase.
    apiaddress = models.CharField(db_column='apiAddress', max_length=1024)  # Field name made lowercase.
    requestparametertype = models.CharField(db_column='requestParameterType', max_length=50)  # Field name made lowercase.
    status = models.IntegerField()
    mockstatus = models.IntegerField(db_column='mockStatus')  # Field name made lowercase.
    mockcode = models.CharField(db_column='mockCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    data = models.TextField(blank=True, null=True)
    lastupdatetime = models.DateTimeField(db_column='lastUpdateTime')  # Field name made lowercase.
    description = models.CharField(max_length=1024, blank=True, null=True)
    apigrouplevelfirst = models.ForeignKey(ApiTestApigrouplevelfirst, models.DO_NOTHING, db_column='apiGroupLevelFirst_id', blank=True, null=True)  # Field name made lowercase.
    project = models.ForeignKey('ApiTestProject', models.DO_NOTHING)
    userupdate = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='userUpdate_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'api_test_apiinfo'


class ApiTestApioperationhistory(models.Model):
    time = models.DateTimeField()
    description = models.CharField(max_length=1024, blank=True, null=True)
    api = models.ForeignKey(ApiTestApiinfo, models.DO_NOTHING)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_test_apioperationhistory'


class ApiTestApiparameter(models.Model):
    name = models.CharField(max_length=1024)
    field_type = models.CharField(db_column='_type', max_length=1024)  # Field renamed because it started with '_'.
    value = models.CharField(max_length=1024, blank=True, null=True)
    required = models.IntegerField()
    restrict = models.CharField(max_length=1024, blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)
    api = models.ForeignKey(ApiTestApiinfo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_test_apiparameter'


class ApiTestApiparameterraw(models.Model):
    data = models.TextField(blank=True, null=True)
    api = models.ForeignKey(ApiTestApiinfo, models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'api_test_apiparameterraw'


class ApiTestApirequesthistory(models.Model):
    requesttime = models.DateTimeField(db_column='requestTime')  # Field name made lowercase.
    requesttype = models.CharField(db_column='requestType', max_length=50)  # Field name made lowercase.
    requestaddress = models.CharField(db_column='requestAddress', max_length=1024)  # Field name made lowercase.
    httpcode = models.CharField(db_column='httpCode', max_length=50)  # Field name made lowercase.
    api = models.ForeignKey(ApiTestApiinfo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_test_apirequesthistory'


class ApiTestApiresponse(models.Model):
    name = models.CharField(max_length=1024)
    field_type = models.CharField(db_column='_type', max_length=1024)  # Field renamed because it started with '_'.
    value = models.CharField(max_length=1024, blank=True, null=True)
    required = models.IntegerField()
    description = models.CharField(max_length=1024, blank=True, null=True)
    api = models.ForeignKey(ApiTestApiinfo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_test_apiresponse'


class ApiTestAutomationcaseapi(models.Model):
    name = models.CharField(max_length=50)
    httptype = models.CharField(db_column='httpType', max_length=50)  # Field name made lowercase.
    requesttype = models.CharField(db_column='requestType', max_length=50)  # Field name made lowercase.
    apiaddress = models.CharField(db_column='apiAddress', max_length=1024)  # Field name made lowercase.
    requestparametertype = models.CharField(db_column='requestParameterType', max_length=50)  # Field name made lowercase.
    formatraw = models.IntegerField(db_column='formatRaw')  # Field name made lowercase.
    examinetype = models.CharField(db_column='examineType', max_length=50)  # Field name made lowercase.
    httpcode = models.CharField(db_column='httpCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    responsedata = models.TextField(db_column='responseData', blank=True, null=True)  # Field name made lowercase.
    automationtestcase = models.ForeignKey('ApiTestAutomationtestcase', models.DO_NOTHING, db_column='automationTestCase_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'api_test_automationcaseapi'


class ApiTestAutomationcasetestresult(models.Model):
    header = models.CharField(max_length=1024, blank=True, null=True)
    parameter = models.TextField(blank=True, null=True)
    result = models.CharField(max_length=50)
    httpstatus = models.CharField(db_column='httpStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
    responseheader = models.TextField(db_column='responseHeader', blank=True, null=True)  # Field name made lowercase.
    responsedata = models.TextField(db_column='responseData', blank=True, null=True)  # Field name made lowercase.
    testtime = models.CharField(db_column='testTime', max_length=128, blank=True, null=True)  # Field name made lowercase.
    automationcaseapi = models.ForeignKey(ApiTestAutomationcaseapi, models.DO_NOTHING, db_column='automationCaseApi_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'api_test_automationcasetestresult'


class ApiTestAutomationgrouplevelfirst(models.Model):
    name = models.CharField(max_length=50)
    project = models.ForeignKey('ApiTestProject', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_test_automationgrouplevelfirst'


class ApiTestAutomationhead(models.Model):
    name = models.CharField(max_length=1024)
    value = models.CharField(max_length=1024)
    interrelate = models.IntegerField()
    automationcaseapi = models.ForeignKey(ApiTestAutomationcaseapi, models.DO_NOTHING, db_column='automationCaseApi_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'api_test_automationhead'


class ApiTestAutomationparameter(models.Model):
    name = models.CharField(max_length=1024)
    value = models.CharField(max_length=1024, blank=True, null=True)
    interrelate = models.IntegerField()
    automationcaseapi = models.ForeignKey(ApiTestAutomationcaseapi, models.DO_NOTHING, db_column='automationCaseApi_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'api_test_automationparameter'


class ApiTestAutomationparameterraw(models.Model):
    data = models.TextField(blank=True, null=True)
    automationcaseapi = models.ForeignKey(ApiTestAutomationcaseapi, models.DO_NOTHING, db_column='automationCaseApi_id', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'api_test_automationparameterraw'


class ApiTestAutomationreportsendconfig(models.Model):
    reportfrom = models.CharField(db_column='reportFrom', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    mailuser = models.CharField(db_column='mailUser', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    mailpass = models.CharField(db_column='mailPass', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    mailsmtp = models.CharField(db_column='mailSmtp', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    project = models.ForeignKey('ApiTestProject', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'api_test_automationreportsendconfig'


class ApiTestAutomationresponsejson(models.Model):
    name = models.CharField(max_length=1024, blank=True, null=True)
    tier = models.CharField(max_length=1024, blank=True, null=True)
    type = models.CharField(max_length=1024)
    automationcaseapi = models.ForeignKey(ApiTestAutomationcaseapi, models.DO_NOTHING, db_column='automationCaseApi_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'api_test_automationresponsejson'


class ApiTestAutomationtaskruntime(models.Model):
    starttime = models.CharField(db_column='startTime', max_length=50)  # Field name made lowercase.
    host = models.CharField(max_length=1024, blank=True, null=True)
    elapsedtime = models.CharField(db_column='elapsedTime', max_length=50)  # Field name made lowercase.
    project = models.ForeignKey('ApiTestProject', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_test_automationtaskruntime'


class ApiTestAutomationtestcase(models.Model):
    casename = models.CharField(db_column='caseName', max_length=50)  # Field name made lowercase.
    description = models.CharField(max_length=1024, blank=True, null=True)
    updatetime = models.DateTimeField(db_column='updateTime')  # Field name made lowercase.
    automationgrouplevelfirst = models.ForeignKey(ApiTestAutomationgrouplevelfirst, models.DO_NOTHING, db_column='automationGroupLevelFirst_id', blank=True, null=True)  # Field name made lowercase.
    project = models.ForeignKey('ApiTestProject', models.DO_NOTHING)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_test_automationtestcase'


class ApiTestAutomationtestresult(models.Model):
    url = models.CharField(max_length=1024)
    requesttype = models.CharField(db_column='requestType', max_length=1024)  # Field name made lowercase.
    host = models.CharField(max_length=1024, blank=True, null=True)
    header = models.CharField(max_length=1024, blank=True, null=True)
    parameter = models.TextField(blank=True, null=True)
    statuscode = models.CharField(db_column='statusCode', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    examinetype = models.CharField(db_column='examineType', max_length=1024)  # Field name made lowercase.
    data = models.TextField(blank=True, null=True)
    result = models.CharField(max_length=50)
    httpstatus = models.CharField(db_column='httpStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
    responsedata = models.TextField(db_column='responseData', blank=True, null=True)  # Field name made lowercase.
    testtime = models.DateTimeField(db_column='testTime')  # Field name made lowercase.
    automationcaseapi = models.ForeignKey(ApiTestAutomationcaseapi, models.DO_NOTHING, db_column='automationCaseApi_id', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'api_test_automationtestresult'


class ApiTestAutomationtesttask(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    frequency = models.IntegerField(blank=True, null=True)
    unit = models.CharField(max_length=50, blank=True, null=True)
    starttime = models.DateTimeField(db_column='startTime')  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='endTime')  # Field name made lowercase.
    host = models.ForeignKey('ApiTestGlobalhost', models.DO_NOTHING, db_column='Host_id')  # Field name made lowercase.
    project = models.ForeignKey('ApiTestProject', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'api_test_automationtesttask'


class ApiTestCustommethod(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1024, blank=True, null=True)
    type = models.CharField(max_length=50)
    datacode = models.TextField(db_column='dataCode')  # Field name made lowercase.
    status = models.IntegerField()
    project = models.ForeignKey('ApiTestProject', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_test_custommethod'


class ApiTestGlobalhost(models.Model):
    name = models.CharField(max_length=50)
    host = models.CharField(max_length=1024)
    description = models.CharField(max_length=1024, blank=True, null=True)
    status = models.IntegerField()
    project = models.ForeignKey('ApiTestProject', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_test_globalhost'


class ApiTestProject(models.Model):
    name = models.CharField(max_length=50)
    version = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    description = models.CharField(max_length=1024, blank=True, null=True)
    status = models.IntegerField()
    lastupdatetime = models.DateTimeField(db_column='LastUpdateTime')  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime')  # Field name made lowercase.
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_test_project'


class ApiTestProjectdynamic(models.Model):
    time = models.DateTimeField()
    type = models.CharField(max_length=50)
    operationobject = models.CharField(db_column='operationObject', max_length=50)  # Field name made lowercase.
    description = models.CharField(max_length=1024, blank=True, null=True)
    project = models.ForeignKey(ApiTestProject, models.DO_NOTHING)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_test_projectdynamic'


class ApiTestProjectmember(models.Model):
    permissiontype = models.CharField(db_column='permissionType', max_length=50)  # Field name made lowercase.
    project = models.ForeignKey(ApiTestProject, models.DO_NOTHING)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_test_projectmember'


class ApiTestUserprofile(models.Model):
    phone = models.CharField(max_length=11)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'api_test_userprofile'


class ApiTestVisitorsrecord(models.Model):
    formattedaddress = models.CharField(db_column='formattedAddress', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(max_length=50, blank=True, null=True)
    province = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    township = models.CharField(max_length=50, blank=True, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)
    number = models.CharField(max_length=50, blank=True, null=True)
    success = models.CharField(max_length=50, blank=True, null=True)
    reason = models.CharField(max_length=1024, blank=True, null=True)
    calltime = models.DateTimeField(db_column='callTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'api_test_visitorsrecord'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
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

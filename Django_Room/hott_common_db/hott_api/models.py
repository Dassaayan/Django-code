# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ApiCommontable(models.Model):
    id = models.CharField(primary_key=True,max_length=100)
    source_id = models.CharField(max_length=30)
    season_id = models.CharField(max_length=80)
    series_id = models.CharField(max_length=80)
    parent_id = models.CharField(max_length=100)
    history_ids = models.CharField(max_length=200)
    item_type = models.CharField(max_length=30)
    title = models.CharField(max_length=512)
    episode_title = models.CharField(max_length=512, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    episode_number = models.CharField(max_length=11, blank=True, null=True)
    season_number = models.CharField(max_length=11, blank=True, null=True)
    release_year = models.CharField(max_length=4, blank=True, null=True)
    release_date = models.CharField(max_length=50, blank=True, null=True)
    expiry_date = models.CharField(max_length=50, blank=True, null=True)
    genres = models.TextField(blank=True, null=True)
    language = models.TextField(blank=True, null=True)
    maturity_ratings = models.TextField(blank=True, null=True)
    duration = models.PositiveIntegerField(blank=True, null=True)
    is_prime = models.CharField(max_length=50, blank=True, null=True)
    purchase_info = models.TextField(blank=True, null=True)
    addon_service = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    directors = models.TextField(blank=True, null=True)
    producers = models.TextField(blank=True, null=True)
    writers = models.TextField(blank=True, null=True)
    cast = models.TextField(blank=True, null=True)
    categories = models.TextField(blank=True, null=True)
    is_valid = models.IntegerField()
    aux_info = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'api_commontable'
        unique_together = (('id', 'item_type', 'source_id', 'season_id', 'series_id'), ('id', 'source_id', 'item_type', 'season_id', 'series_id', 'is_valid'),)


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
    last_name = models.CharField(max_length=30)
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


class Category(models.Model):
    source_name = models.CharField(primary_key=True, max_length=100)
    item_type = models.CharField(max_length=50)
    categories = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'
        unique_together = (('source_name', 'item_type'),)


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


class MissedContent(models.Model):
    source_id = models.CharField(max_length=100)
    source_name = models.CharField(max_length=100)
    item_type = models.CharField(max_length=50, blank=True, null=True)
    crawl_status = models.IntegerField()
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'missed_content'


class MissedContentInfo(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    source_id = models.CharField(max_length=100)
    item_type = models.CharField(max_length=50, blank=True, null=True)
    count = models.IntegerField()
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'missed_content_info'


class Rank(models.Model):
    source_id = models.CharField(primary_key=True, max_length=100)
    feed = models.CharField(max_length=100)
    content_type = models.CharField(max_length=30)
    reference_url = models.TextField(blank=True, null=True)
    count = models.CharField(max_length=100)
    list = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rank'
        unique_together = (('source_id', 'content_type', 'feed'),)


class Source(models.Model):
    source_id = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    is_released = models.IntegerField(blank=True, null=True)
    image_url = models.TextField()
    reference_url = models.TextField()
    content_type = models.CharField(max_length=100)
    crawl_frequency = models.IntegerField()
    fas_required = models.IntegerField(blank=True, null=True)
    db_ip = models.CharField(max_length=20)
    db_name = models.CharField(max_length=32)
    proxy_ip = models.CharField(max_length=20)
    proxy_port = models.CharField(max_length=10)
    is_robots = models.IntegerField()
    station_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'source'
        unique_together = (('source_id', 'content_type'),)

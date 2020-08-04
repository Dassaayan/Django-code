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


class HbogoPrograms(models.Model):
    launch_id = models.CharField(unique=True, max_length=255, blank=True, null=True)
    show_type = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    series_launch_id = models.CharField(max_length=255, blank=True, null=True)
    series_url = models.CharField(max_length=255, blank=True, null=True)
    series_title = models.CharField(max_length=255, blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True)
    season_number = models.IntegerField(blank=True, null=True)
    episode_number = models.IntegerField(blank=True, null=True)
    duration = models.CharField(max_length=255, blank=True, null=True)
    maturity_rating = models.CharField(max_length=255, blank=True, null=True)
    audio_quality = models.CharField(max_length=255, blank=True, null=True)
    video_quality = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    cast = models.TextField(blank=True, null=True)
    producers = models.TextField(blank=True, null=True)
    directors = models.TextField(blank=True, null=True)
    writers = models.TextField(blank=True, null=True)
    expired = models.IntegerField(blank=True, null=True)
    season_count = models.IntegerField(blank=True, null=True)
    expired_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hbogo_programs'


class ShowtimePrograms(models.Model):
    source_program_id = models.IntegerField(unique=True, blank=True, null=True)
    item_type = models.CharField(max_length=32, blank=True, null=True)
    title = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=2048, blank=True, null=True)
    img_url = models.CharField(max_length=2048, blank=True, null=True)
    screen_writers = models.TextField(blank=True, null=True)
    directors = models.TextField(blank=True, null=True)
    story_writers = models.TextField(blank=True, null=True)
    cast = models.TextField(blank=True, null=True)
    year = models.BigIntegerField(blank=True, null=True)
    rating = models.CharField(max_length=128, blank=True, null=True)
    run_time = models.IntegerField(blank=True, null=True)
    season_cnt = models.IntegerField(blank=True, null=True)
    total_episodes = models.IntegerField(blank=True, null=True)
    series_id = models.IntegerField(blank=True, null=True)
    season_number = models.BigIntegerField(blank=True, null=True)
    episode_number = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    expired = models.IntegerField(blank=True, null=True)
    mapped = models.IntegerField(blank=True, null=True)
    expiry_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'showtime_programs'


class StarzPrograms(models.Model):
    item_type = models.CharField(max_length=32, blank=True, null=True)
    title = models.CharField(max_length=128, blank=True, null=True)
    episode_title = models.CharField(max_length=128, blank=True, null=True)
    new_content = models.IntegerField(blank=True, null=True)
    source_program_id = models.CharField(unique=True, max_length=32, blank=True, null=True)
    episode_number = models.BigIntegerField(blank=True, null=True)
    media_id = models.CharField(max_length=128, blank=True, null=True)
    mpaa_rating = models.CharField(max_length=8, blank=True, null=True)
    run_time = models.IntegerField(blank=True, null=True)
    release_year = models.BigIntegerField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    actors = models.TextField(blank=True, null=True)  # This field type is a guess.
    directors = models.TextField(blank=True, null=True)  # This field type is a guess.
    categories = models.TextField(blank=True, null=True)  # This field type is a guess.
    genre = models.TextField(blank=True, null=True)  # This field type is a guess.
    popularity = models.BigIntegerField(blank=True, null=True)
    season_id = models.BigIntegerField(blank=True, null=True)
    season_number = models.BigIntegerField(blank=True, null=True)
    is_original = models.IntegerField(blank=True, null=True)
    original_airdate = models.DateTimeField(blank=True, null=True)
    expiry_time = models.DateTimeField(blank=True, null=True)
    series_id = models.CharField(max_length=32, blank=True, null=True)
    program_id = models.CharField(max_length=32, blank=True, null=True)
    url = models.CharField(max_length=128, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'starz_programs'

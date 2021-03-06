# Generated by Django 2.2.9 on 2020-01-09 16:04

"""Create a skeleton User we can use when automatically ingesting content
so that Wagtail behaves as expected.

The user will be INACTIVE, so they can't log in (but, regardless, they will lack
Mozilla SSO). This won't block them being used as the Editor user when
importing content.

"""

from django.db import migrations
from .. import constants


def forwards(apps, schema_editor):

    # Live import - we can pretty much rely on auth.User being stable
    from django.contrib.auth.models import User

    user = User.objects.create_user(
        username=constants.INGESTION_USER_USERNAME,
        first_name=constants.INGESTION_USER_FIRST_NAME,
        last_name=constants.INGESTION_USER_LAST_NAME,
        is_active=False,
    )
    user.set_unusable_password()
    user.save()


def backwards(apps, schema_editor):

    # Live import - we can pretty much rely on auth.User being stable
    from django.contrib.auth.models import User

    User.objects.filter(username=constants.USERNAME).delete()


class Migration(migrations.Migration):

    dependencies = [("ingestion", "0002_bootstrap_ingestion_config")]

    operations = [migrations.RunPython(forwards, backwards)]

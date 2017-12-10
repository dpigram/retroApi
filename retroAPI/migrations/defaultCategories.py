from __future__ import unicode_literals
from django.db import models, migrations

def load_categories(apps, schema_editor):
    Category = apps.get_model("retroAPI", "Category")
    communication_cat = Category(id=0,name='Communication')
    communication_cat.save()

    Category = apps.get_model("retroAPI", "Category")
    communication_cat = Category(id=0,name='Web Services')
    communication_cat.save()

    Category = apps.get_model("retroAPI", "Category")
    communication_cat = Category(id=0,name='Trust')
    communication_cat.save()

def delete_categories(apps, schema_editor):
	Category = apps.get_model("retroAPI", "Category")
	Category.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('retroAPI', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(load_categories,delete_categories),
    ]


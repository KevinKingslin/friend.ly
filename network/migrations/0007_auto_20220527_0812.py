# Generated by Django 3.2.12 on 2022-05-27 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_auto_20220527_0808'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created']},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='timestamp',
            new_name='created',
        ),
    ]

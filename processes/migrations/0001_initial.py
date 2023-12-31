# Generated by Django 4.2.1 on 2023-07-19 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=50)),
                ('contact_phone_number', models.PositiveIntegerField()),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_message', models.TextField(max_length=300)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

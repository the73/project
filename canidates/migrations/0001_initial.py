# Generated by Django 4.0.1 on 2022-04-25 10:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userprofiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=12)),
                ('status', models.CharField(choices=[('looking', 'looking'), ('cancelled', 'cancelled'), ('order', 'order')], default='looking', max_length=150)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owner.admin')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

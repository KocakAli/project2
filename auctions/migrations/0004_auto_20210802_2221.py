# Generated by Django 3.2.5 on 2021-08-02 19:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auction_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='name',
        ),
        migrations.AddField(
            model_name='auction',
            name='title',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('comment', models.CharField(max_length=256)),
                ('comment_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_comment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
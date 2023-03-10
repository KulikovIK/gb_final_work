# Generated by Django 4.1.7 on 2023-03-06 16:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=180, verbose_name='заголовок')),
                ('message_text', models.TextField(blank=True, null=True, verbose_name='текст сообщения')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='удалено')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to=settings.AUTH_USER_MODEL, verbose_name='от кого')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to=settings.AUTH_USER_MODEL, verbose_name='кому')),
            ],
            options={
                'verbose_name': 'сообщение',
                'verbose_name_plural': 'сообщения',
                'ordering': ['is_deleted', 'created_at'],
            },
        ),
    ]

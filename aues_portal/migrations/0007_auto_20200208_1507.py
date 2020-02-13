# Generated by Django 3.0.3 on 2020-02-08 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aues_portal', '0006_auto_20200208_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_adviser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='group_adviser', to='aues_portal.Teacher', verbose_name='Эдвайзер группы'),
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to='Teachers/Documents/', verbose_name='Фотография')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='teacher_name', to='aues_portal.Teacher', verbose_name='Кому принадлежит докумет')),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Документы',
            },
        ),
    ]

# Generated by Django 3.0.3 on 2020-02-08 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aues_portal', '0007_auto_20200208_1507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documents',
            name='name',
        ),
        migrations.AddField(
            model_name='documents',
            name='doc_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_query_name='document_name', to='aues_portal.Teacher', verbose_name='Название документа'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='doc_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Название документа'),
        ),
        migrations.AlterField(
            model_name='documents',
            name='file',
            field=models.FileField(blank=True, upload_to='Teachers/Documents/', verbose_name='Документ'),
        ),
    ]

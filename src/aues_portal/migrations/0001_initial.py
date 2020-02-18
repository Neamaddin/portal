# Generated by Django 3.0.3 on 2020-02-15 12:49

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Полное название кафедры')),
                ('short_name', models.CharField(max_length=10, verbose_name='Аббревиатура кафедры')),
                ('url_name', models.CharField(max_length=10, verbose_name='Ссылка')),
                ('info', models.TextField(blank=True, verbose_name='Информация о кафедре')),
                ('release', models.BooleanField(verbose_name='Выпуск групп')),
            ],
            options={
                'verbose_name': 'Кафедра',
                'verbose_name_plural': 'Кафедры',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='Название группы')),
                ('study_start', models.DateField(verbose_name='Дата начала обучения группы')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='department', to='aues_portal.Department', verbose_name='Кафедра')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
            },
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Полное название института')),
                ('short_name', models.CharField(max_length=10, verbose_name='Аббревиатура института')),
                ('url_name', models.CharField(max_length=10, verbose_name='Ссылка')),
                ('info', models.TextField(blank=True, verbose_name='Информация об институте')),
            ],
            options={
                'verbose_name': 'Институт',
                'verbose_name_plural': 'Институты',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('surname', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=20, verbose_name='Отчество')),
                ('image', models.ImageField(blank=True, default='Prof.png', upload_to='Teachers/', verbose_name='Фотография')),
                ('rezume', models.TextField(blank=True, verbose_name='Резюме')),
                ('phone', models.CharField(blank=True, max_length=12, verbose_name='Телефон')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Почта')),
                ('post', models.CharField(blank=True, max_length=100, verbose_name='Занимаемая должность')),
                ('education', models.TextField(blank=True, verbose_name='Образование')),
                ('qualification_up', models.TextField(blank=True, verbose_name='Повышение квалификации')),
                ('science_articles', models.TextField(blank=True, verbose_name='Научные статьи')),
                ('аwards', models.TextField(blank=True, verbose_name='Награды')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='department', to='aues_portal.Department', verbose_name='Кафедра')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='user', to=settings.AUTH_USER_MODEL, verbose_name='Пользовательская страница')),
            ],
            options={
                'verbose_name': 'Преподаватель',
                'verbose_name_plural': 'Преподаватели',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('surname', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=20, verbose_name='Отчество')),
                ('age', models.PositiveSmallIntegerField(default=0, verbose_name='Возраст')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='group', to='aues_portal.Group', verbose_name='Группа')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='group_adviser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='group_adviser', to='aues_portal.Teacher', verbose_name='Эдвайзер группы'),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Описание документа')),
                ('category', models.CharField(choices=[('document', 'Документ(Дипломы)'), ('sertificat', 'Скан сертификатов(повышение квалификации)'), ('article', 'Оттиск из статьи'), ('award', 'Награды')], max_length=10, verbose_name='Категория')),
                ('file', models.FileField(upload_to='Teachers/Documents/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name='Документ')),
                ('doc_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='document_name', to='aues_portal.Teacher', verbose_name='Кому принадлежит докумет')),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Документы',
            },
        ),
        migrations.AddField(
            model_name='department',
            name='institute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='institute', to='aues_portal.Institute', verbose_name='Институт'),
        ),
    ]
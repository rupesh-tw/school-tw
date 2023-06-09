# Generated by Django 4.2.1 on 2023-05-26 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_delete_college'),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'college_details',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.college')),
            ],
            options={
                'db_table': 'teacher_details',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('stream', models.CharField(max_length=255)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.college')),
                ('teacher', models.ManyToManyField(to='core.teacher')),
            ],
            options={
                'db_table': 'student_details',
            },
        ),
        migrations.AddIndex(
            model_name='college',
            index=models.Index(fields=['id'], name='college_det_id_4ea44e_idx'),
        ),
        migrations.AddIndex(
            model_name='teacher',
            index=models.Index(fields=['id'], name='teacher_det_id_ecce33_idx'),
        ),
        migrations.AddIndex(
            model_name='student',
            index=models.Index(fields=['id'], name='student_det_id_fb416a_idx'),
        ),
    ]

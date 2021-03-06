# Generated by Django 3.2.7 on 2022-02-01 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignar_ejercicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_ejercicio', models.DateField()),
                ('semana', models.IntegerField()),
                ('n_ejercicio', models.IntegerField()),
                ('comentarios_adicionales', models.TextField(max_length=150)),
                ('completado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Ejercicio_Pomo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_ejercicio', models.CharField(max_length=30)),
                ('detalle_ejercicio', models.TextField(max_length=150)),
                ('video', models.FileField(null=True, upload_to='video')),
            ],
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_semanas', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='familiar',
            old_name='user',
            new_name='userD',
        ),
        migrations.RenameField(
            model_name='kinesiologo',
            old_name='user',
            new_name='userD',
        ),
        migrations.RenameField(
            model_name='paciente',
            old_name='user',
            new_name='userD',
        ),
        migrations.RemoveField(
            model_name='ejercicio',
            name='fecha_ejercicio',
        ),
        migrations.RemoveField(
            model_name='ejercicio',
            name='id_paciente',
        ),
        migrations.RemoveField(
            model_name='familiar',
            name='id_ciudad',
        ),
        migrations.RemoveField(
            model_name='familiar',
            name='id_kinesiologo',
        ),
        migrations.RemoveField(
            model_name='kinesiologo',
            name='id_ciudad',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='id_ciudad',
        ),
        migrations.AddField(
            model_name='ejercicio',
            name='video',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='familiar',
            name='ciudad',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='familiar',
            name='foto',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='familiar',
            name='id_paciente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='proyecto.paciente'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='familiar',
            name='rut',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kinesiologo',
            name='ciudad',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kinesiologo',
            name='foto',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='kinesiologo',
            name='rut',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='ciudad',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='foto',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='paciente',
            name='id_kinesiologo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='proyecto.kinesiologo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='rut',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resultado',
            name='completado',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='resultado',
            name='evidencia',
            field=models.FileField(null=True, upload_to='video'),
        ),
        migrations.DeleteModel(
            name='Ciudad',
        ),
        migrations.AddField(
            model_name='programa',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.paciente'),
        ),
        migrations.AddField(
            model_name='asignar_ejercicio',
            name='ejercicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.ejercicio'),
        ),
        migrations.AddField(
            model_name='asignar_ejercicio',
            name='programa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.programa'),
        ),
        migrations.AlterField(
            model_name='resultado',
            name='id_ejercicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.asignar_ejercicio'),
        ),
    ]

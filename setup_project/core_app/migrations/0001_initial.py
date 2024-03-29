# Generated by Django 4.0.6 on 2022-07-18 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alternative', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField()),
                ('alternative_a', models.TextField(default='')),
                ('alternative_b', models.TextField(default='')),
                ('alternative_c', models.TextField(default='')),
                ('alternative_d', models.TextField(default='')),
                ('expected_answer', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core_app.option')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('question', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='core_app.question')),
                ('option', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core_app.option')),
            ],
        ),
    ]

# Generated by Django 3.0.2 on 2020-01-26 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examMaker.Category')),
            ],
        ),
        migrations.CreateModel(
            name='ExamLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_name', models.CharField(max_length=255, unique=True)),
                ('hard_questions', models.DecimalField(decimal_places=0, max_digits=2)),
                ('medium_questions', models.DecimalField(decimal_places=0, max_digits=2)),
                ('easy_questions', models.DecimalField(decimal_places=0, max_digits=2)),
                ('time', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('A', models.CharField(max_length=100)),
                ('B', models.CharField(max_length=100)),
                ('C', models.CharField(max_length=100)),
                ('D', models.CharField(max_length=100)),
                ('answer', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1)),
                ('question_level', models.CharField(choices=[('3', 'hard'), ('2', 'medium'), ('1', 'easy')], max_length=1)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examMaker.Category')),
            ],
        ),
        migrations.CreateModel(
            name='MakeExam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examMaker.Exam')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examMaker.Question')),
            ],
        ),
        migrations.AddField(
            model_name='exam',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examMaker.ExamLevel'),
        ),
        migrations.AddField(
            model_name='exam',
            name='questions',
            field=models.ManyToManyField(through='examMaker.MakeExam', to='examMaker.Question'),
        ),
    ]

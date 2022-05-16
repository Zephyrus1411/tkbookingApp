# Generated by Django 4.0.4 on 2022-05-03 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tkbookingApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticketbooking',
            name='begining',
        ),
        migrations.RemoveField(
            model_name='ticketbooking',
            name='destination',
        ),
        migrations.AlterField(
            model_name='buses',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tkbookingApp.category'),
        ),
        migrations.AlterField(
            model_name='ticketbooking',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tkbookingApp.category'),
        ),
        migrations.AlterField(
            model_name='ticketbooking',
            name='customers',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tkbookingApp.customers'),
        ),
        migrations.AlterField(
            model_name='ticketbooking',
            name='routes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tkbookingApp.routes'),
        ),
    ]
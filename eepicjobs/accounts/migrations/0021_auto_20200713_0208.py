# Generated by Django 2.2.2 on 2020-07-13 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_auto_20200713_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='contract_type',
            field=models.CharField(choices=[('Contract', 'Contract'), ('Internship', 'Internship'), ('Temporary', 'Temporary'), ('Freelance', 'Freelance'), ('Part Time', 'Part Time'), ('Full Time', 'Full Time')], default='Internship', max_length=10),
        ),
        migrations.AlterField(
            model_name='employee',
            name='salary_currency',
            field=models.CharField(choices=[('Rupees', 'Rupees'), ('Dollar', 'Dollar'), ('Euro', 'Euro'), ('Pound', 'Pound')], default='Rupees', max_length=10),
        ),
        migrations.AlterField(
            model_name='employee',
            name='salry_type',
            field=models.CharField(choices=[('Monthly', 'Monthly'), ('Weekly', 'Weekly'), ('Hourly', 'Hourly'), ('Yearly', 'Yearly')], default='Monthly', max_length=10),
        ),
    ]

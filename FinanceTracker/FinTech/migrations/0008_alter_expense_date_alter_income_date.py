# Generated by Django 4.2 on 2024-11-17 15:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinTech', '0007_alter_expense_date_alter_income_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateField(default=datetime.date(2024, 11, 17)),
        ),
        migrations.AlterField(
            model_name='income',
            name='date',
            field=models.DateField(default=datetime.date(2024, 11, 17)),
        ),
    ]
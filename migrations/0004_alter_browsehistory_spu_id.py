# Generated by Django 4.1.7 on 2024-11-10 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baykeshop', '0003_browsehistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='browsehistory',
            name='spu_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='baykeshop.baykeshopspu', verbose_name='商品'),
        ),
    ]
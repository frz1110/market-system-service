# Generated by Django 3.2.13 on 2022-05-26 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='gambar', upload_to='produk/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

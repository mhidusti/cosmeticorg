# Generated by Django 4.2.4 on 2024-02-29 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Special_Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='MenuSpecials.jpg', upload_to='Special_Products')),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=200)),
                ('content2', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]
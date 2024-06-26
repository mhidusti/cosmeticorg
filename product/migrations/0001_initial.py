

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Products')),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=200)),
                ('attributes', models.CharField(max_length=200)),
                ('price', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ManyToManyField(to='product.category')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]

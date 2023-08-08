from django.db import migrations, models
from api.user.models import CustomUser

class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(name="rokon",
                          email="rokon.raz@gmail.com",
                          is_staff=True,
                          is_superuser=True,
                          phone='01739933258',
                          gender='Male',
                          )
        
        user.set_password('12345')
        user.save()

    dependencies = [
    ]

    operations = [
        migrations.RunPython(seed_data),
    ]

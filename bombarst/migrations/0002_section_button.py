import cms.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bombarst", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="section",
            name="button",
            field=cms.fields.CharField(default=""),
            preserve_default=False,
        ),
    ]

from django.db import models

# Create your models here.


class User(models.Model):
    class Meta:
        db_table = "user"

    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=20, null=False, unique=True)
    username = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=128, null=False)

    def __repr__(self):
        return "<{} {}>".format(self.id, self.email)

    __str__ = __repr__
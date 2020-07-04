from django.db import models
from user.models import User


class Article(models.Model):
    class Meta:
        db_table = 'article'

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    pub_date = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __repr__(self):
        return "<id={}, title={}>".format(self.id, self.title)

    __str__ = __repr__
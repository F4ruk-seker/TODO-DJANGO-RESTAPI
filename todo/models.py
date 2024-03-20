from django.contrib.auth.models import User
from django.db import models


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=250)
    is_Complete = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} - {"tammalandı" if self.is_Complete else "tamamlanmadı"}'


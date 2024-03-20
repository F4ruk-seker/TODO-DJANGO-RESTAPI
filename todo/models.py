from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=250)
    is_Complete = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} - {"tammalandı" if self.is_Complete else "tamamlanmadı"}'


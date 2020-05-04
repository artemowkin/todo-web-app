from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Task(models.Model):
    title = models.CharField(max_length=144)
    description = models.TextField(blank=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    date = models.DateTimeField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks_list')

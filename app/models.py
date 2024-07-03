from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tags")

    class Meta:
        ordering = ["is_completed", "-created_at"]

    def __str__(self):
        return self.name

from django.db import models
from django.urls import reverse


class Video(models.Model):
    Video_Description = models.CharField(max_length=500)
    slug = models.SlugField(unique=True)
    videofile = models.FileField(upload_to='deploy/videos/%Y/%m/%d/', null=True, verbose_name="")
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return reverse("deploy:detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.Video_Description + ": " + str(self.id)

# Create your models here.

from django.db import models

from django.utils import timezone

class Comment(models.Model):
  title = models.CharField(max_length=20)
  body = models.TextField()
  date_added = models.DateTimeField(default=timezone.now)
  
  def __str__(self):
    return self.title
    
  class Meta:
    verbose_name_plural = "Comments"

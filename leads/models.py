from django.db import models

# Create your models here.
class LeadQuerySet(models.QuerySet):
    pass


class LeadManager(models.Manager):
    def get_queryset(self):
        return LeadQuerySet(self.model, using=self._db)


class Lead(models.Model):
    name = models.CharField(max_length=100)
    email=models.EmailField()
    message = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    object = LeadManager()


    
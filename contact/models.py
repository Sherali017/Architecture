from django.db import models

class ContactModel(models.Model):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    message = models.TextField()
    phone = models.IntegerField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'

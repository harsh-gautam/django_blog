from django.db import models

# Create your models here.
class ContactForm(models.Model):
    s_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=80)
    date = models.DateField(auto_now_add=True)
    query = models.TextField()

    def __str__(self):
        return self.query[:25] + "..."
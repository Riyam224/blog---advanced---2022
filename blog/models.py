import imp
from django.db import models
# Create your models here.
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse



class Post(models.Model):
    title = models.CharField(_("title"), max_length=250)
    content = models.TextField(_("content"))
    date_posted = models.DateTimeField(_("date posted"), default=timezone.now)
    author = models.ForeignKey(User, verbose_name=_("author"), on_delete=models.CASCADE)

    

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})


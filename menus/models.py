from django.db import models
from django.urls import reverse


class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=255, blank=True)
    named_url = models.CharField(max_length=100, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def get_url(self):
        if self.url:
            return self.url
        elif self.named_url:
            return reverse(self.named_url)
        return '#'

    def __str__(self):
        return self.name

    @property
    def get_ancestors(self):
        ancestors = []
        parent = self.parent
        while parent:
            ancestors.append(parent)
            parent = parent.parent
        return ancestors

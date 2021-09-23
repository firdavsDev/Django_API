from django.contrib import admin
from django.db import models

# Register your models her
from .models import Article
admin.site.register(Article)
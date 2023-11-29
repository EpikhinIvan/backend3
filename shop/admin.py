from django.contrib import admin
from .models import UserProfile, Order

# Регистрация моделей
admin.site.register(UserProfile)
admin.site.register(Order)
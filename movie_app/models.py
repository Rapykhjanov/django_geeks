from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
import random

class User(AbstractUser):
    is_active = models.BooleanField(default=False)
    confirmation_code = models.CharField(max_length=6, unique=True, blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",  # Уникальное имя для обратного доступа
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions_set",  # Уникальное имя для обратного доступа
        blank=True
    )

    def generate_confirmation_code(self):
        while True:
            code = str(random.randint(100000, 999999))
            if not User.objects.filter(confirmation_code=code).exists():
                self.confirmation_code = code
                self.save(update_fields=["confirmation_code"])
                break

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Director(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Режиссёр"
        verbose_name_plural = "Режиссёры"


class Movie(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    duration = models.PositiveIntegerField()
    director = models.ForeignKey(
        Director, on_delete=models.SET_NULL, null=True, blank=True, related_name="movies"
    )

    def __str__(self):
        return f"{self.title} ({self.duration} мин)"

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


class Review(models.Model):
    STARS_CHOICES = [(i, str(i)) for i in range(1, 6)]
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    stars = models.PositiveSmallIntegerField(choices=STARS_CHOICES, default=1)

    def __str__(self):
        return f"Отзыв на {self.movie.title} - {self.stars}⭐"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

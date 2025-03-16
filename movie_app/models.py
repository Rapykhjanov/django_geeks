from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Запрещаем дубли имен

    def __str__(self):
        return f"Director: {self.name}"

class Movie(models.Model):
    title = models.CharField(max_length=255, unique=True)  # Запрещаем дубли фильмов
    description = models.TextField()
    duration = models.PositiveIntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name="movies")

    def __str__(self):
        return f"Movie: {self.title} ({self.duration} min)"

class Review(models.Model):
    STARS_CHOICES = [(i, str(i)) for i in range(1, 6)]
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    stars = models.PositiveSmallIntegerField(choices=STARS_CHOICES, default=1)

    def __str__(self):
        return f"Review for {self.movie.title} - {self.stars} stars"

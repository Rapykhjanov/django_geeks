from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name="movies")

    def __str__(self):
        return self.title


class Review(models.Model):
    STARS_CHOICES = [(i, str(i)) for i in range(1, 6)]

    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    stars = models.PositiveSmallIntegerField(choices=STARS_CHOICES, default=1)

    def __str__(self):
        return f"Review for {self.movie.title} - {self.stars} stars"

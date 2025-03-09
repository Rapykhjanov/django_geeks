from rest_framework import serializers
from .models import Director, Movie, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    rating = serializers.SerializerMethodField()

    def get_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews.exists():
            return round(sum([r.stars for r in reviews]) / reviews.count(), 1)
        return 0

    class Meta:
        model = Movie
        fields = '__all__'

class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.IntegerField(source='movies.count', read_only=True)

    class Meta:
        model = Director
        fields = '__all__'

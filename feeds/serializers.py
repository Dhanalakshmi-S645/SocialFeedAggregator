
from rest_framework import serializers
from feeds .models import Feed

class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = '__all__'  # Or specify the exact fields you want to include
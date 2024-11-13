# feeds/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from feeds.models import Feed
from feeds.serializers import FeedSerializer

class FeedList(APIView):
    def get(self, request):
        feeds = Feed.objects.all()
        serializer = FeedSerializer(feeds, many=True)
        return Response(serializer.data)

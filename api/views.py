from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import GuestSerializer

class WeddingListView(APIView):
    def post(self, request):
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # This returns the success response your frontend expects
            return Response({"message": "Successfully added"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

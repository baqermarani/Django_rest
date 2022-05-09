from django.shortcuts import render , get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from .serializers import UserSerializer , UserSerializer2
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(validated_data=serializer.validated_data)
            return Response({'massage':'User created successfully'
                             ,'data':serializer.data}
                            ,status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated,]
    queryset = User.objects.all()

    def list(self, request):
        serializer = UserSerializer2(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)  # get user by id
        serializer = UserSerializer2(user)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)  # get user by id
        if user != request.user:
            return Response({'massage':'You are not authorized to update this user'})
        serializer = UserSerializer2(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)  # get user by id
        if user != request.user:
            return Response({'massage':'You are not authorized to update this user'})
        user.is_active = False
        user.save() # save user
        return Response({'massage':'User deleted successfully'})


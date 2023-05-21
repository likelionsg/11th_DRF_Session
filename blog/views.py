from rest_framework import generics
from .serializers import *
from .models import *


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # lookup_field = 'name'


class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # lookup_field = 'name'


class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # lookup_field = 'name'


class BlogCreateAPIView(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogListAPIView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogUpdateAPIView(generics.UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogDestroyAPIView(generics.DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

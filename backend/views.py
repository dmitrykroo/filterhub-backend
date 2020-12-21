from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import status, permissions
from rest_framework.generics import ListAPIView, get_object_or_404, CreateAPIView

from backend.models import Post
from backend.serializers import PostSerializer, PostDetailsSerializer, UserDetailsSerializer


class PostView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self, request):
        user_id = request.GET.get('user')
        if user_id is not None:
            queryset = self.get_queryset().filter(user_id=user_id)
        else:
            queryset = self.get_queryset()

        serializer = self.serializer_class(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)


class PostDetailsView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostDetailsSerializer

    def post(self, request):
        request_data = dict(request.data)
        request_data['user'] = request.user.pk
        serializer = self.serializer_class(data=request_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        post = get_object_or_404(self.get_queryset(), pk=pk)
        if post.user.pk != request.user.pk:
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={"status": "error"})

        request_data = dict(request.data)
        serializer = self.serializer_class(data=request_data, instance=post, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = get_object_or_404(self.get_queryset(), pk=pk)
        if post.user.pk != request.user.pk:
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST)

        post.delete()
        return JsonResponse(data="OK", safe=False)


class UserDetailsView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserDetailsSerializer

    def patch(self, request):
        user = get_object_or_404(self.get_queryset(), pk=request.user.pk)

        request_data = dict(request.data)

        serializer = self.serializer_class(data=request_data, instance=user, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST)
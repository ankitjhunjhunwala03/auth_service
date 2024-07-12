from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserDetailsSerializer


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserRegistrationSerializer(user, context=self.get_serializer_context()).data,
            "message": "User created successfully."
        })


class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class TokenVerifyView(generics.GenericAPIView):
    serializer_class = UserDetailsSerializer
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return Response({'message': "Invalid Token"}, status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(instance=request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

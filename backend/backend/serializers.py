
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from cryptography.fernet import Fernet


class CustomAuthToken(ObtainAuthToken):
   
    def post(self, request, *args, **kwargs):
        try:
            _key = b'IkB0Lq7xZHzfSLgVnvDjBm8mXe6jQclfMUyfaoAUK4E='
            
            fernet = Fernet(_key)
            request.data._mutable = True
            request.data['password'] = fernet.decrypt(request.data['password'].encode('utf-8')).decode()
            request.data._mutable = False
            serializer = self.serializer_class(data=request.data,
                                            context={'request': request})
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            print(user.first_name)
            token, created = Token.objects.get_or_create(user=user)

            
            return Response({
                'token': token.key,
                'user_id': user.pk,
            })
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class Logout(ListAPIView):
    permission_classes = (IsAuthenticated,) 
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response({"status":"success"},status=status.HTTP_200_OK)

class UserDetail(ListAPIView):
    permission_classes = (IsAuthenticated,) 
    def get(self,request):
        user = Token.objects.get(key=request.auth.key).user
        return Response({
            "first_name":user.first_name,
            "last_name":user.last_name
        })

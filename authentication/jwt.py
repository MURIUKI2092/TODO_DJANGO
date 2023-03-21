from rest_framework.authentication import get_authorization_header,BaseAuthentication
from rest_framework import exceptions
import jwt
from django.conf import settings
from authentication.models import User
class JWTAuthentication(BaseAuthentication):
    def authenticate(self,request):
        auth_headers = get_authorization_header(request)
        print("+++++",auth_headers)
        auth_data = auth_headers.decode('utf8')
        auth_token = auth_data.split(' ')
        if len(auth_token)!=2:
            raise exceptions.AuthenticationFailed('Token not valid')
        
        else:
            token = auth_token[1]
            try:
                payload = jwt.decode(token,settings.SECRET_KEY,algorithms='HS256')
                user_name = payload['username']
                user = User.objects.get(username=user_name)
                return (user,token)
            except jwt.ExpiredSignatureError as e:
                raise exceptions.AuthenticationFailed("Token expired,Log in again!!")
            except jwt.DecodeError as e:
                raise exceptions.AuthenticationFailed("Token is invalid,Log in again!!")
            except User.DoesNotExist as e:
                raise exceptions.AuthenticationFailed("No such user!!")
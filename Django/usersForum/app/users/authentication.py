import os
from django.conf import settings
from rest_framework import authentication, exceptions
from decouple import config
from ..helpers.tokenize import Tokenize
from .models import User_model

class JWTAuthentication(authentication.BaseAuthentication):
    keyword = config('TOKEN_KEYWORD')

    def authenticate(self, request):
        """
        This checks that the passed JWt token is valid and returns a user and his/her token on successful verification.
        """
        request.user = None

        # returns Authorization header as a bytestring

        auth_header = authentication.get_authorization_header(request).split()
       
        if not auth_header or auth_header[0].decode().lower() != self.keyword.lower():
            return None

        if len(auth_header) == 1:
            raise exceptions.AuthenticationFailed('Invalid token header. No credentials provided.')
        elif len(auth_header) > 2:
            raise exceptions.AuthenticationFailed('Invalid token header. Token string should not spaces.')
        return self.authenticate_credentials(request, auth_header[1].decode())

    def authenticate_credentials(self, request, token):
        """
        authenticate given credentials. If authentication is successful,
        return the user and token. If not, return an error.
        """
        try:
            verify=False
            secrete = None
            unverifiedPayload = Tokenize.decrypt(token,secrete,verify)
            user = User_model.objects.get(pk=unverifiedPayload['id'])
        except Exception as e:
            raise exceptions.AuthenticationFailed('Invalid session. Please login again to continue')

        try:
            decode_key = config('SECRETE')+f'{user.id}'.lower().replace('e', config('SECRETE'))
            Tokenize.decrypt(token, decode_key)
        except Exception as e:
            raise exceptions.AuthenticationFailed(str(e))
        return (user, token)

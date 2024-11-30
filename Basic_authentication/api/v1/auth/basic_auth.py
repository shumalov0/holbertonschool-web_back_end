#!/usr/bin/env python3
''' Module of Basic_auth
'''
from typing import TypeVar
from models.user import User
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """ BasicAuth class
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        ''' Extract base64 authorization header '''
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if authorization_header.startswith("Basic "):
            return "".join(authorization_header.split(" ")[1:])
        return None

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        ''' Decode base64 authorization header '''
        if base64_authorization_header and isinstance(base64_authorization_header, str):
            try:
                encoded = base64_authorization_header.encode('utf-8')
                decoded = base64.b64decode(encoded)
                return decoded.decode('utf-8')
            except Exception:
                return None
        return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        ''' Return the user email and the password '''
        if decoded_base64_authorization_header and isinstance(decoded_base64_authorization_header, str) and ":" in decoded_base64_authorization_header:
            mail, password = decoded_base64_authorization_header.split(':', 1)
            return mail, password
        return None, None

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str
    ) -> TypeVar('User'):
        """ Get User object from credentials """
        if (
                user_email is None or
                user_pwd is None or
                not isinstance(user_email, str) or
                not isinstance(user_pwd, str)
        ):
            return None
        user = User()
        search = user.search({"email": user_email})
        if not search:
            return None
        user = search[0]

        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """ Get current user """
        auth = self.authorization_header(request)
        if auth is None:
            return None
        extract = self.extract_base64_authorization_header(auth)
        if extract is None:
            return None
        decode = self.decode_base64_authorization_header(extract)
        if decode is None:
            return None
        user, pwd = self.extract_user_credentials(decode)
        if user is None or pwd is None:
            return None
        return self.user_object_from_credentials(user, pwd)

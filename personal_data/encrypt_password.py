#!/usr/bin/env python3
'''Module for encrypting'''
import bcrypt


def hash_password(password: str) -> bytes:
    '''Returns hash'''
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''Checks if equal'''
    return bcrypt.checkpw(password.encode(), hashed_password)

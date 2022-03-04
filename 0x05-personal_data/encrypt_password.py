#!/usr/bin/env python3
"""
5. Encrypting passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    5. Encrypting passwords
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    5. is_valid passwords
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)


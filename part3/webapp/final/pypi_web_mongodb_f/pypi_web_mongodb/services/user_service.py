from typing import Optional
from passlib.handlers.sha2_crypt import sha512_crypt

from pypi_web_mongodb.data.users import User


def user_count() -> int:
    return User.objects().count()


def user_by_id(user_id) -> Optional[User]:
    return User.objects().filter(id=user_id).first()


def user_by_email(email: str) -> Optional[User]:
    found = User.objects().filter(email=email).first()
    return found


def create_account(full_name: str, email: str, plain_text_password: str) -> Optional[User]:
    if not email or not email.strip():
        raise Exception("Email address required")
    if not plain_text_password or not plain_text_password.strip():
        raise Exception("Password required")

    email = email.strip().lower()

    found = user_by_email(email)
    if found:
        raise Exception("User with email {} already exists.".format(email))

    user = User()
    user.email = email
    user.name = full_name
    user.hashed_password = hash_text(plain_text_password)

    user.save()
    return user


def login_account(email: str, plain_text_password: str) -> Optional[User]:
    if not email or not email.strip():
        return None
    if not plain_text_password or not plain_text_password.strip():
        return None

    email = email.strip().lower()

    found = user_by_email(email)
    if not found:
        return None

    if not verify_hash(found.hashed_password, plain_text_password):
        return None

    return found


def hash_text(text: str) -> str:
    hashed_text = sha512_crypt.encrypt(text, rounds=150000)
    return hashed_text


def verify_hash(hashed_text: str, plain_text: str) -> bool:
    return sha512_crypt.verify(plain_text, hashed_text)

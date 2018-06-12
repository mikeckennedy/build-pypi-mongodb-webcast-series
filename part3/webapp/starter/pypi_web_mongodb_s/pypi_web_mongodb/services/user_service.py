from typing import Optional
from passlib.handlers.sha2_crypt import sha512_crypt

from pypi_web_mongodb.data.users import User


def user_count() -> int:
    # TODO: Return the count of users
    return 0


def user_by_id(user_id) -> Optional[User]:
    # TODO: Find user by id
    return None


def user_by_email(email: str) -> Optional[User]:
    # TODO: Find user by email
    return None


def create_account(full_name: str, email: str, plain_text_password: str) -> Optional[User]:
    if not email or not email.strip():
        raise Exception("Email address required")
    if not plain_text_password or not plain_text_password.strip():
        raise Exception("Password required")

    # Normalize the email
    email = email.strip().lower()

    # TODO: Verify the user does not already exist.
    # TODO: Create a user, set email, name, password
    # TODO: Save and return
    return None


def login_account(email: str, plain_text_password: str) -> Optional[User]:
    if not email or not email.strip():
        return None
    if not plain_text_password or not plain_text_password.strip():
        return None

    # Normalize the email
    email = email.strip().lower()

    # TODO: Get the user by email (return if missing)
    # TODO: Verify the hash (password)

    # TODO: Return user
    return None


def hash_text(text: str) -> str:
    hashed_text = sha512_crypt.encrypt(text, rounds=150000)
    return hashed_text


def verify_hash(hashed_text: str, plain_text: str) -> bool:
    return sha512_crypt.verify(plain_text, hashed_text)

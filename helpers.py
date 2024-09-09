import secrets

class Generator:
    email_generator = f"{secrets.token_hex(8)}@gmail.com"
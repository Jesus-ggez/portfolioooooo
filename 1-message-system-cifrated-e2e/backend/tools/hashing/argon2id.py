from nacl.pwhash import argon2id


def to_hash_or_raises(value: str) -> str:
    return argon2id.str(
        password=value.encode(encoding='utf-8')
    ).decode('utf-8')


def veryfy_or_raises(password: str, hashed: str) -> None:
    # raises InvalidkeyError if password and hashed are not equals
    argon2id.verify(
        password_hash=hashed.encode(),
        password=password.encode(),
    )

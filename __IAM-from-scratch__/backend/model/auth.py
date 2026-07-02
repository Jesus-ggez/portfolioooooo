from typing import Annotated

from pydantic import (
    StringConstraints,
    BaseModel,
    EmailStr,
)


__PasswordField = StringConstraints(
    strip_whitespace=True,
    max_length=64,
    min_length=8,
    strict=True,
)


class RegisterForm(BaseModel):
    password: Annotated[str, __PasswordField]
    email: EmailStr

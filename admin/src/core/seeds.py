from src.core import auth


def run():
    user = auth.create_User(
        email="jose@mail.com",
        password="1234"
    )

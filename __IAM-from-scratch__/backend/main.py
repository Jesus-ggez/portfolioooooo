from dotenv import load_dotenv


from app import (
    Application,
    __run_serve,
    create_app,
)


load_dotenv()


api: Application = Application()
api.root_path = '/api'


def main() -> None:
    create_app(app=api)

    __run_serve(app=api)


if __name__ == '__main__':
    main()

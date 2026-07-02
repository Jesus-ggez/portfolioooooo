from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI as Application
from uvicorn import run


from config import __get_varenv # type: ignore
# from api.__ import ___ as Router


def __run_serve(app: Application) -> None:
    return run(
        host=__get_varenv(name='HOST'),
        port=int(__get_varenv(name='PORT')),
        app=app,
    )


def create_app(app: Application) -> None:
    # app.include_router(router=Router)

    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_origins=['*'],
        allow_methods=['*'],
        allow_headers=['*'],
    )

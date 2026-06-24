from os import environ as varenv


def __get_varenv(name: str) -> str:
    if var := varenv.get(name):
        return var

    raise NotImplementedError('any varenv doesnt exists or not implemented')

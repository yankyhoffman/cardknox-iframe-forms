def bool_env(value):
    if not value:
        return False

    if isinstance(value, str):
        return value.lower() not in ['0', 'false']

    return True

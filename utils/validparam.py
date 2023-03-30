import json


def post_param_valid(params):
    if params is None or params == "":
        return 1
    try:
        json.loads(params)
    except Exception as e:
        return 1
    return 0

import json


def is_json(json_str):
    try:
        json.loads(json_str)
    except ValueError as e:
        # print(e)
        return False
    return True


def better_print(json_str):
    if is_json(json_str):
        return json.dumps(json.loads(json_str), indent=4, ensure_ascii=False)
    else:
        return json_str


def error_print(json_str):
    if is_json(json_str):
        return json.dumps(json.loads(json_str), indent=4, ensure_ascii=False)
    else:
        return json_str


if __name__ == '__main__':
    # e = better_print('{"name":"aaaa","age":18}')
    # e = error_print('{"name":"aaaa","age":18}')
    e = error_print('adfasdfasdfasdfasd')
    print(e)

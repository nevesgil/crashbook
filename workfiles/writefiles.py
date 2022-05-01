import json


def file_simple(file_path, message, mode):
    with open(file_path, mode) as file_object:
        file_object.write(f"{message}\n")


def json_simple(file_path, message, mode):
    with open(file_path, mode) as file_object:
        json.dump(message, file_object)

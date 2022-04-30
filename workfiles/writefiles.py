def file_simple(file_path, message, mode):
    with open(file_path, mode) as file_object:
        file_object.write(f"{message}\n")

def read_all_file(path_file):
    with open(path_file) as file_object:
        contents = file_object.read()
    contents = contents.strip()
    return contents


def read_lines(path_file):
    with open(path_file) as file_object:
        for line in file_object:
            print(line.strip())


def list_from_lines(path_file):
    with open(path_file) as file_object:
        lines = file_object.readlines()

    data = []
    for line in lines:
        data.append(line.strip())
    print(data)


def to_single_line(path_file):
    with open(path_file) as file_object:
        lines = file_object.readlines()

    single_line = ""
    for line in lines:
        single_line += line.strip()

    print(single_line)


def file_properties(file_path):
    with open(file_path, "r") as file_object:
        contents = file_object.read()

    words = contents.split()
    num_words = len(words)

    print(f"number of words: {num_words}")


def files_properties(files_paths):

    for file in files_paths:
        with open(file, "r+") as file_object:
            contents = file_object.read()

        words = contents.split()
        num_words = len(words)

        print(f"number of words in {file}: {num_words}")


files_paths = ["workfiles/hamlet.txt", "workfiles/divinecomedy_paradise.txt"]

files_properties(files_paths)

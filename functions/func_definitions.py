def dict_func():
    responses = {}
    polling_active = True

    while polling_active:
        name = input("name: ")
        response = input("breja: ")

        responses[name] = response

        repeat = input("continue (yes/no): ")
        if repeat == "no":
            polling_active = False

    return responses


dictionaryOfResponses = dict_func()

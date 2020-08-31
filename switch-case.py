## switch-case in python##

def numbers_to_strings(argument):

    switcher = {
        0: "v",
        1: "c",
        2: "b",
        3: "d",
        4: "a"
    }
    return switcher.get(argument, "nothing")
print(numbers_to_strings(6))
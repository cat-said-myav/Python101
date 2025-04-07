# TODO решите задачу
import json

def task() -> float:
    data = 0
    with open("input.json", "r") as file:
        list_ = json.load(file)
    for dict_ in list_ :
        data += dict_["score"] * dict_["weight"]
    return round(data, 3)


print(task())

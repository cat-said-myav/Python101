import csv
from csv import DictReader
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, "r") as csv_:
        list_ = [row for row in DictReader(csv_)]
    with open(OUTPUT_FILENAME, "w") as json_:
        json.dump(list_, json_, indent=4)



if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME, encoding="utf-8") as output_f:
        for line in output_f:
            print(line, end="")

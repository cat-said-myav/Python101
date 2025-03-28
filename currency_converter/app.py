import requests
import json


def check_user(username:str) -> str | None:
    """
    Функция проверки наличия пользователя и ключа в файле key_access.txt:
    username = str
    return str or None
    """
    with open ("E://key_access.txt", "r") as file:
        for line in file:
            if line.split()[0] == username.lower():
                key = line.split()[1]
                return key
            else:
                return None

def create_username_key(username:str, key:str) -> str:
    """
    Функция создания пользователя и ключа в файле key_access.txt:
    1. username = str
    2. key = str
    return str
    """
    while True:
        key = input("Введите ключ: ")
        url = f"https://v6.exchangerate-api.com/v6/{key}/latest/USD"
        response = requests.get(url)
        if response.status_code == 200:
            with open ("key_access.txt", "a") as file:
                file.write(f"{username.lower()} {key}\n")
            return key
        else:
            print("Введеный ключ не возвращает статус 200 OK ,проверьте коректность ввода")
            continue
    
def check_valute(valute:str) -> bool | list:
    """
    Функция проверки наличия запрашиваемой валюты в файле currency.json:
    1. valute = str
    return bool or list
    """
    with open ("currency.json") as json_:
        valute_dict = json.load(json_)
        if valute in valute_dict.keys():
             return True
        else:
            result = list(valute_dict.keys())
            return result
        
def converter(key:str, base:str, target:str ,amount:float) -> float :
    """
    Функция конвертации валюты:
    1. key = str
    2. base = str
    3. target = str
    4. amount = float
    return float
    """
    response = requests.get(f"https://v6.exchangerate-api.com/v6/{key}/latest/{base}")
    data = response.json()
    result = float(data["conversion_rates"].get(target)) * amount
    return result
        
def input_username_and_key() -> str:
    """
    Функция запроса имени пользователя и в случае необходимости ключа:
    return str
    """
    username = input("Введите ваше имя: ")
    key = check_user(username)
    if key == None:
        key = create_username_key(username,key)
        return key
    else:
        return key

def get_base_valute() -> str:
    """
    Функция запроса базовой валюты:
    return str
    """
    while True:
        base_valute = input("Введите код исходной валюты (например, USD): ").upper()
        check_ = check_valute(base_valute)
        if check_ != True:
            print(f"Ввыберите  код исходной валюты из списка :\n {check_}")
            continue
        else:
            return base_valute

def get_target_valute() -> str:
    """
    Функция запроса целевой валюты:
    return str
    """
    while True:
        target_valute = input("Введите код целевой валюты (например, RUB):").upper()
        check_ = check_valute(target_valute)
        if check_ != True:
            print(f"Ввыберите  код исходной валюты из списка :\n {check_}")
            continue
        else:
            return target_valute
        
def get_amount() -> float:
    """
    Функция запроса суммы конвертации:
    return float
    """
    while True:
        amount = input("Введите сумму для конвертации: ")
        if amount.isdigit and float(amount) > 0 :
            amount = float(amount)
            return amount
        else:
            ("Проверьте что введены цифры и сума больше 0")
            continue
 

if __name__ == "__main__":
    print ("Добро пожаловать в конвертор валют")
    key = input_username_and_key()
    while True:
        choise = input("""
                       Введите start - для начала работы
                       Введите exit - для выхода из программы:\n""")
        if choise == "start":
            base_valute = get_base_valute ()
            target_valute = get_target_valute()
            amount = get_amount()
            result = converter(key, base_valute, target_valute,amount)
            print (f"За {float(amount):.2f} {base_valute} Вы получите {result:.2f} {target_valute}")
            continue
        elif choise == "exit":
            print("Досвидание!")
            break
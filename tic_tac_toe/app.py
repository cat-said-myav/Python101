
def input_value(text:str) -> int :
    while True:
        value = input(f"Введите количество {text}: ")
        if not value.isdigit():
            print("Введены не цифры!")
            continue
        elif 3 > int(value) or int(value) > 9:
            print("Значение должно быть в диапазоне от 3 до 9")
            continue
        return int(value)

def create_field() -> list:
    while True:
        coll = input_value("столбцов")
        row = input_value("строк")
        if coll != row:
            print("Количество столбцов и строк должно быть одинаковым")
            continue
        else:
            field = [["_"] * coll for _ in range(row)]
            return field

def print_field(field:list,field_size:int):
    for n in range(field_size):
        if n == 0:
            print(f"  {n}", end="")
        else: 
            print(f" {n}", end="")
    for number, row in enumerate(field):
        print("")
        print(f"{number}|", end="")
        for cell in row:
            print(f'{cell}|', end="")
    print("\n")

def chech_data(text:str, field_size:int) -> int:
    while True:
        row = input(text)
        if not row.isdigit():
            print('Нужны цифры')
            continue
        row = int(row)
        if not 0 <= row <= field_size:
            print('Ошибка неверный диапазон')
            continue
        return row

def check_win(field:list, field_size:int) -> bool:
    for value in field:
        cond = [value[i] == value[i + 1] for i in range(field_size - 1)]
        if all(cond) and value[0] != "_":
            return True
    for value in zip(*field):
        cond = [value[i] == value[i + 1] for i in range(field_size - 1)]
        if all(cond) and value[0] != "_":
            return True
    cond = [field[i][i] == field[i + 1][i + 1] for i in range(field_size - 1)]
    if all(cond) and field[0][0] != "_":
        return True
    cond = [field[i][field_size - 1 - i] == field[i + 1][field_size - 2 - i] for i in range(field_size - 1)]
    if all(cond) and field[0][-1] != "_":
        return True
    return False

def start() -> tuple:
    current_player = None
    while True:
        is_first = input('Будешь ходить первым? [y/n]: ').lower()
        if is_first == ("y" or "у"):
            while True:
                symb = input('Игрок-1 Выберите символ (х\o): ').lower()
                if symb == ("x" or "х"):
                    symb = symb
                elif symb == ("o" or "0"):
                    symb = symb
                else:
                    print("Символ должен быть (х\o)")
                    continue
                player1 = symb
                current_player = "1"
                player2 = "x" if symb == ("o" or "0") else "o"
                return player1, player2, current_player
        elif is_first == "n":
             while True:
                symb = input('Игрок-2 Выберите символ (х\o): ').lower()
                if symb == ("x" or "х"):
                    symb = symb
                elif symb == ("o" or "0"):
                    symb = symb
                else:
                    print("Символ должен быть (х\o)")
                    continue
                current_player = "2"
                player2 = symb
                player1 = "x" if symb == ("o" or "0") else "o"
                return player1, player2, current_player
        else:
            print("Введите (y/n)")
            continue

def game(field:list, current_player:str, player1:str, player2:str) -> str:
    field_size = len(field)
    print_field(field,field_size)
    for i in range((field_size)**2):
        if current_player == '1':
            while True:
                row = chech_data('Игрок-1 куда будешь ставить(строка): ', field_size)
                col = chech_data('Игрок-1 куда  будешь ставить(столбец): ', field_size)
                if field[row][col] != "_":
                    print('Ошибка ячейка уже занята')
                    continue
                field[row][col] = player1
                break
        else:
            while True:
                row = chech_data('Игрок-2 куда будешь ставить(строка): ', field_size)
                col = chech_data('Игрок-2 куда ставить(столбец): ', field_size)
                if field[row][col] != "_":
                    print('Ошибка ячейка уже занята')
                    continue
                field[row][col] = player2
                break
        print_field(field,field_size)
        is_win = check_win(field, field_size)
        if is_win == True:
            return f"Победа Игрока-{current_player} на {i+1} ходу"
        else:
            current_player = '2' if current_player == '1' else '1'
    if not is_win:
        return "Ходы закончились Ничья"
    
if __name__ == "__main__":
    game_data = start()
    player1 = game_data[0]
    player2 = game_data[1]
    current_player = game_data[2]
    field = create_field()
    print(game(field,current_player, player1, player2))
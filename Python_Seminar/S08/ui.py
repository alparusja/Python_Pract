from logger import input_data, print_data


def interface():
    print("Добрый день! Вы попали на специальный бот справочник от GeekBrains! \n 1 - запись данных \n 2 - вывод данных")
    command = int(input('Введите число '))

    while command != 1 and command != 2:
        print("Неправильный ввод")
        command = int(input('Введите число '))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()



# def export_info(file_name, second_file_name, num):    
#     res = file_name
#     for el in res:
#         if el["Телефон"] == str(num):            
#             el = [el["Имя"], el["Фамилия"], el["Телефон"]]   
#         second_file_name, el
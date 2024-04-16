def export_info(file_name, second_file_name, num):    
    res = file_name
    for el in res:
        if el["Телефон"] == str(num):            
            el = [el["Имя"], el["Фамилия"], el["Телефон"]]   
        second_file_name, el
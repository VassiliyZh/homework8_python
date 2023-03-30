def show_data():
    '''Эта функция показывает содержимое справочника'''
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file.read()
    return book

def new_data():
    '''Добавляет новую информацию в справочник'''
    with open('data.txt', 'a', encoding='utf-8') as file:
        file.write(input('Введите необходимую информацию: ') + '\n')
    
def find_data():
    '''Данная функция находит нужную информацию в справочнике''' 
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
        temp = input('Введите подсказку для поиска: ')
        for i in book:
            if temp in i:
                print(i)

# def rewrited(strings, data, filename):
#     fio = input('Введите изменение в ФИО: ')
#     phone = input('Введите изменение в телефоне')
#     with open(filename, 'w', encoding='utf-8') as f2:
#         [f2.write('{fio} | {phone}\n') if line == strings else f2.write(
#             f'{data[line]}\n') for line in range(len(data)-1)]
#         print('Данные успешно изменены')

# def deleted(strings, data, filename):
#     with open(filename, 'w', encoding='utf-8') as f2:
#         [f2.write(f'{data[line]}\n') if line != 
#          strings else '' for line in range(len(data)-1)] 
#         print('Данные успешно удалены') 

def edit_data(filename):
    data = seach_data(filename)
    if len(data[0]) == 1:
        rewrited(data[0][0], data[1], filename)
    elif len(data[0]) > 1:
        change = int(input('Введите порядковый номер для изменения записи: '))
        while change not in [i for i in range(1, len(data[1] + 1))]:
            print('Введенный номер отсутствует в списке вариантов')
            change = int(input('Введите порядковый номер для изменения записи: '))  
        rewrited(int(data[0][change-1], data[1], filename))

# def delete_data(filename):
#     data = seach_data(filename)
#     if len(data[0]) == 1:
#         rewrited(data[0][0], data[1], filename)
#     elif len(data[0]) > 1:

def delete_data(string):
    '''Данная функция удаляет ненужную информацию в справочнике''' 
    new = []
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file.read()
        for i in book.splitlines():
            if i != string:
                new.append(i)
    with open('data.txt', 'w', encoding='utf-8') as fd:
        fd.write('\n'.join(new))
        fd.write('\n')            

# def remove_string3(filename, string):
    # rst = []
    # with open(filename) as fd:
    #     t = fd.read()
        # for line in t.splitlines():
        #     if line != string:
        #         rst.append(line)

                   

while True:
    mode = input('Выберите режим работы справочника: ')
    if mode == '1':
        print(show_data())
    elif mode == '2':
        new_data()
    elif mode == '3':
        find_data()
    elif mode == '4':
        string = input('Введите удаляемую фразу: ')
        delete_data(string)
    elif mode == '0':
        break    
    else:
        print('No mode')
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
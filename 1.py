# Создать телефонный справочник с возможностью 
# импорта и экспорта данных в нескольких форматах.

# В рамках этого обсуждения вам надо нарисовать 
# “архитектуру” (например, в виде блок-схемы) для 
# работы данного приложения.

import pickle 

class Member:
    
    def init(self, listfields, arg):
        
        self.data = dict(zip(listfields,arg))

    def identifier(self):
          return ' '.join([self.data['имя'],self.data['фамилия']]).lower()

    def paramchan(self,key, values):
          self.data[key] = values

    def years(self):
          return self.data['возраст']

    def show(self):
        return set(map(str.lower, list(self.data.values())))

    def change(self):
        return list(self.data.keys())

    def str(self):
        return ' '.join(list(self.data.values()))

def readfile(name):
    try:
        with open(name, 'rb') as f:
            return  pickle.load(f)
    except:
        print('\t\tданных еще не сохранено!\n ')
        return []
        
def savedata(obj,name):
    file = open(name,'wb')
    pickle.dump(obj , file)


def correct_input(text):
    name = input(f'{text} > ')
    if name == '*':
        return name 
    while not name.isalpha():
        print('не корректный ввод')
        name = input(f'{text} > ')
    return name.capitalize()
    

def correct_number(text):
    print('номер +7 код номер без пробелов -> ')
    number = input(f'{text} > ')
    while True:
        if number[0] == '+' and number[1:].isdigit() and len(number) == 12:
            return number
        print('не корректный ввод')
        number = input(f'{text} > ')
        
def correct_age(text):
    age = input(f'{text} > ')
    while True:
        if age.isdigit() or age == '*':
            return age
        print('введите цифры !')
        age = input(f'{text} > ')
    
        
def data_input(listfields):
    list_fun = [correct_input, correct_input, correct_number, correct_age, correct_input]
    return [fun(text) for text, fun in zip(listfields, list_fun)]
        
                

def look(data):
    for obj in data:
        print(obj)

def search(data,line):
    trigger = 1 
    for obj in data:
        if line.issubset(obj.show() ):
            trigger = 0
            print(f'\t результат - {obj}')
    if trigger:
        print('совпадений не найдено')

def search_age(data,member):
    for obj in data:
        if obj.identifier().lower() == member.lower():
            print( obj.years())
            return
   

def addmember(listfields, data, name):
    database = data_input(listfields)
    client = ' '.join(database[:2])
    for obj in data:
        client == obj.identifier()
        print('имя и фамилия существуют. выберите другие.')
        return
                      
    memb = Member(listfields, database)
    print( 'пользователь добавлен')
    data.append(memb)
    savedata(data,name)
    

def del_memb(data):
    member = ' '.join(map(str.lower, [input('имя > '), input('фамилия > ')]))
    for i,obj in enumerate(data):
            if obj.identifier() == member:
                data.pop(i)
                savedata(data,name)
                print('удалено')
                return
        
def change(data, member):
    for obj in data: 
        if  obj.identifier() == member:
            key = input('введите имя поля > ')
            if key not in obj.change():
                print('нет такого поля')
                if input(' создать поле? д\н > ').lower() == 'д':
                    key = input('введите имя поля > ')
                else:
                    return
            values = input('введите значение > ')
            obj.paramchan(key, values)
            break


name = 'data.pickle'
data = readfile(name) 
listfields = ['имя','фамилия','номер','возраст','город']

while True:
    
    print('''\n\t\tКоманды для работы со справочником:
    \t\tПросмотр всех записей справочника:  - 1
    \t\tПоиск по справочнику -2
    \t\tДобавление новой записи - 3
    \t\t Удаление записи из справочника по Имени и Фамилии - 4
    \t\tИзменение любого поля в определенной записи справочника - 5 
    \t\tВывод возраста человека (записи) по Имени и Фамилии - 6
     \t\tВыход - 0 \n''')
    
    command = input('Команда: > ')
    
    if command == '1':
        look(data)
    elif command == '2':
        line = set(input('что искать> ').lower().split())
        search(data,line)
    elif command == '3':
        print('Введите данные или * при их отсутствии')
        addmember(listfields, data, name)
    elif command == '4':
        del_memb(data)
    elif command == '5':
        member = input('имя фамилия > ').lower()
        change(data, member)
    elif command == '6':
        member = input('имя фамилия > ').lower()
        search_age(data,member)
        
    elif command == '0':
        savedata(data,name)
        print("Работа завершена") 
        raise SystemExit
def imp():
    with open('spravochnic.txt', 'a', encoding='utf-8') as file:
        file.write('\n')
        fio = (input('Введите фио: ') + '\n')
        for info in fio:
            file.write(info)
        phone_number = input('Введите номер телефона:' + '\n')
        for info1 in phone_number:
            file.write(info1)

        print(f'Добавлена запись: {fio} | {phone_number}\n')





def exp():
    name = input('Введите фамилию искомого контакта ')
    with open('spravochnic.txt', 'r', encoding='utf-8') as file:
        text = file.read()
        for i in range(len(text)):
            if text[i] == name:
                for line in text[i:i+3]:
                    print(line)


def all_cont():
    with open('spravochnic.txt', 'r', encoding='utf-8') as file:
        text = file.read()
        print(text)

print('Режим 1 - новый контакт ')
print('Режим 2 - поиск контакта ')
print('Режим 3 - все контакты ')
mode = int(input("Введите режим: "))
if mode == 1:
    exp()
elif mode == 2:
    imp()
elif mode == 3:
    all_cont()
else:
    print('Некорректный режим!')











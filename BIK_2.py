#python BIK_2.py


prompt = '\nДобро пожаловать в игру "БЫКИ и КОРОВЫ!"\n'
prompt += '(Чтоб завершить игру введите 00)'
print(prompt)

import random
list_dlya_zagadivaniya = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(list_dlya_zagadivaniya)
zagadannie_tsifri = list_dlya_zagadivaniya[0:4]
#print(zagadannie_tsifri)
active = True
while active:
    chislo = str(input('\nВведите 4 неповторяющиеся цифры: '))
    if chislo == '00':
        active = False
    if len(chislo) != 4:           #проверка на 4 цифры
        print('\nКоличество цифр в числе не равно 4. Пожалуйста, введите 4 неповторяющиеся цифры:')
        continue

    spiskom = []
   
    for value in chislo:
        value = int(value)
        spiskom.append(value)
    print(f'{spiskom} - Вы ввели это число')

    len(spiskom)     #проверка на повторяющиеся цифры
    spisok_posle_proverki = set(spiskom)
    if len(spiskom) > len (spisok_posle_proverki):
        print('\nЦифры в числе не должны повторяться. Пожалуйста, введите другое число:')
        continue

    k = 0
    b = 0

    for x in range(4):
        if zagadannie_tsifri[x] == spiskom[x]:      
            b += 1
       
    for value in spiskom:
        if value in zagadannie_tsifri:
            k += 1
        
    ko = k - b

#vivod_bikov 
    if b == 0:
       vivod_bikov = f''
    if b == 1:
        vivod_bikov = f'{b} бык'
    if 1< b <4:
        vivod_bikov = f'{b} быка'
    if b == 4:
       print(f'\nВы выиграли!\n')
       break
#vivod_korov
    if ko == 0:
       vivod_korov = f''
    if ko == 1:
       vivod_korov = f'{ko} корова'
    if ko > 1:
       vivod_korov = f'{ko} коровы'
    if b == 0 and ko == 0:
        print('В числе нет быков и коров')

    print(f'{vivod_bikov} {vivod_korov}')
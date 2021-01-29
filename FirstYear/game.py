import sys
import random

general_list = list()
skor = 0

difficulty = input("Select difficulty(1 or 2 or 3 )")
row = 0
column = 0
if difficulty == "1":
    row = 3
    column = 3
elif difficulty == "2":
    row = 5
    column = 5
elif difficulty == "3":
    row = 7
    column = 7
else:
    print("Wrong difficulty!")
    sys.exit(1)


def game_creator(row, column, general_list):
    for i in range(row):
        row_list = list()
        for j in range(column):
            row_list.append(random.randint(0, 4))
        general_list.append(row_list)
    return general_list


def table_shower(general_list):
    for i in range(len(general_list)):
        print(*general_list[i])
    print()


def real_degistirici_bosluk(general_list, row, column, number, deger):
    try:
        if general_list[row + 1][column] == deger:
            general_list[row + 1][column] = " "
            number += 1
            real_degistirici_bosluk(general_list, row + 1, column, number, deger)
    except IndexError:
        pass
    try:
        if row == 0:
            pass
        elif general_list[row - 1][column] == deger:
            general_list[row - 1][column] = " "
            number += 1
            real_degistirici_bosluk(general_list, row - 1, column, number, deger)
    except IndexError:
        pass
    try:
        if general_list[row][column + 1] == deger:
            general_list[row][column + 1] = " "
            number += 1
            real_degistirici_bosluk(general_list, row, column + 1, number, deger)
    except IndexError:
        pass
    try:
        if (column != 0) and (general_list[row][column - 1] == deger):
            general_list[row][column - 1] = " "
            number += 1
            real_degistirici_bosluk(general_list, row, column - 1, number, deger)
    except IndexError:
        pass
    return number


def real_degistirici_k(general_list, row, column, number, deger):
    try:
        if general_list[row + 1][column] == deger:
            general_list[row + 1][column] = "k"
            number += 1
            real_degistirici_k(general_list, row + 1, column, number, deger)
    except IndexError:
        pass
    try:
        if row == 0:
            pass
        elif general_list[row - 1][column] == deger:
            general_list[row - 1][column] = "k"
            number += 1
            real_degistirici_k(general_list, row - 1, column, number, deger)
    except IndexError:
        pass
    try:
        if general_list[row][column + 1] == deger:
            general_list[row][column + 1] = "k"
            number += 1
            real_degistirici_k(general_list, row, column + 1, number, deger)
    except IndexError:
        pass
    try:
        if (column != 0) and (general_list[row][column - 1] == deger):
            general_list[row][column - 1] = "k"
            number += 1
            real_degistirici_k(general_list, row, column - 1, number, deger)
    except IndexError:
        pass
    return number


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def kaydirici(general_list, index1, index2):
    try:
        if general_list[index1 + 1][index2] == " ":
            general_list[index1][index2], general_list[index1 + 1][index2] = general_list[index1 + 1][index2], \
                                                                             general_list[index1][index2]
    except IndexError:
        pass


def satir_silici(general_list):
    for ters_satir in reversed(general_list):
        if ters_satir.count(" ") == len(ters_satir):
            general_list.remove(general_list[general_list.index(ters_satir)])


def kaydirma_tarayici(general_list):
    for satir in general_list:
        index1 = general_list.index(satir)
        control = 0
        for sutun in satir:
            index2 = control
            kaydirici(general_list, index1, index2)
            control += 1


def sola_kaydirici(general_list):
    deger1 = 0
    for satir in general_list:
        index1 = deger1
        deger2 = 0
        for sutun in satir:
            index2 = deger2
            counter = 0
            counter2 = 0
            while True:
                try:
                    if general_list[counter][index2] == " ":
                        counter2 += 1
                except IndexError:
                    pass
                if counter2 == len(general_list):
                    for j in general_list:
                        j.remove(j[index2])
                    break
                elif (counter2 != len(general_list)) and (counter == len(general_list)):
                    break
                else:
                    pass
                counter += 1
            deger2 += 1
        deger1 += 1


def degistirici_bosluk(number, general_list, column, row, deger):
    deger = deger
    # SOLDAKINE BAKAN
    try:
        if (column != 0) and (general_list[row][column - 1]) == "k":
            general_list[row][column - 1] = " "
            number += 1
            real_degistirici_bosluk(general_list, row, column - 1, number,
                                    "k")  # solundaki değiştikten sonra fonksiyonu cagırıyor
    except IndexError:
        general_list[row][column] = " "
        number += 1
        real_degistirici_bosluk(general_list, row, column, number,
                                "k")  # solundaki index error verirse kendisi değiştikten sonra kendisini gönderiyor fonksiyona
    # SAGDAKINE BAKAN
    try:
        if general_list[row][column + 1] == "k":
            general_list[row][column + 1] = " "
            number += 1
            real_degistirici_bosluk(general_list, row, column + 1, number,
                                    "k")  # sağındaki değiştikten sonra sağındakini fonksiyona gönderiyor.
    except IndexError:
        real_degistirici_bosluk(general_list, row, column, number,
                                "k")  # hiçbir şey değişmediği için kendisini fonksiyona gönderiyor
        pass
    # USTTEKINE BAKAN
    try:
        if general_list[row + 1][column] == "k":
            general_list[row + 1][column] = " "
            number += 1
            real_degistirici_bosluk(general_list, row + 1, column, number, "k")
    except IndexError:
        pass
    # ALTTAKINE BAKAN
    try:
        if row == 0:
            pass
        elif general_list[row - 1][column] == "k":
            general_list[row - 1][column] = " "
            number += 1
            real_degistirici_bosluk(general_list, row - 1, column, number, "k")
    except IndexError:
        pass
    # SAGDAKI VE SOLDAKILER VARSA HALLETTIKTEN SONRA ASIL SAYIYI DEGISTIREN
    try:
        if not (((column != 0) and (general_list[row][column - 1] == "k")) and (
                general_list[row][column + 1] == "k") and (general_list[row + 1][column] == "k") and (
                        general_list[row - 1][column] == "k")):
            pass
    except IndexError:
        pass
    return number


def degistirici_k(number, general_list, column, row, deger):
    deger = deger
    # SOLDAKINE BAKAN
    try:
        if (column != 0) and (general_list[row][column - 1]) == deger:
            general_list[row][column - 1] = "k"
            number += 1
            real_degistirici_k(general_list, row, column - 1, number,
                               deger)  # solundaki değiştikten sonra fonksiyonu cagırıyor
    except IndexError:
        general_list[row][column] = "k"
        number += 1
        real_degistirici_k(general_list, row, column, number,
                           deger)  # solundaki index error verirse kendisi değiştikten sonra kendisini gönderiyor fonksiyona
    # SAGDAKINE BAKAN
    try:
        if general_list[row][column + 1] == deger:
            general_list[row][column + 1] = "k"
            number += 1
            real_degistirici_k(general_list, row, column + 1, number,
                               deger)  # sağındaki değiştikten sonra sağındakini fonksiyona gönderiyor.
    except IndexError:
        real_degistirici_k(general_list, row, column, number,
                           deger)  # hiçbir şey değişmediği için kendisini fonksiyona gönderiyor
        pass
    # USTTEKINE BAKAN
    try:
        if general_list[row + 1][column] == deger:
            general_list[row + 1][column] = "k"
            number += 1
            real_degistirici_k(general_list, row + 1, column, number, deger)
    except IndexError:
        pass
    # ALTTAKINE BAKAN
    try:
        if row == 0:
            pass
        elif general_list[row - 1][column] == deger:
            general_list[row - 1][column] = "k"
            number += 1
            real_degistirici_k(general_list, row - 1, column, number, deger)
    except IndexError:
        pass
    # SAGDAKI VE SOLDAKILER VARSA HALLETTIKTEN SONRA ASIL SAYIYI DEGISTIREN
    try:
        if not (((column != 0) and (general_list[row][column - 1] == deger)) and (
                general_list[row][column + 1] == deger) and (general_list[row + 1][column] == deger) and (
                        general_list[row - 1][column] == deger)):
            pass
    except IndexError:
        pass
    return number


def bosluk_tarayici(general_list):
    sayac = 0
    for roww in general_list:
        for columnn in roww:
            if columnn == "k":
                sayac += 1
    return sayac


general_list = game_creator(row, column, general_list)
print(general_list)

table_shower(general_list)
print("Your score is : {}\n".format(skor))
while True:
    donus_kontrolu = 0
    row, column = input("Please enter a row and column number: ").split()
    """if row == "e":
        break
    """
    print()
    row = int(row) - 1
    column = int(column) - 1
    try:
        deger = general_list[row][column]
    except:
        print("Please enter correct size!\n")
        continue
    if deger == " ":
        print("Please enter correct size!\n")
        continue
    degistirici_k(0, general_list, column, row, deger)
    n = bosluk_tarayici(general_list)
    skor += int(deger) * fibonacci(n)
    degistirici_bosluk(0, general_list, column, row, deger)
    while True:
        if donus_kontrolu == len(general_list) * 10:
            break
        real_control = 0
        for satir in general_list:
            index1 = real_control
            control = 0
            for sutun in satir:
                index2 = control
                kaydirici(general_list, index1, index2)
                control += 1
            real_control += 1
        donus_kontrolu += 1
    satir_silici(general_list)
    sola_kaydirici(general_list)
    table_shower(general_list)
    print("Your score is  : {}\n".format(skor))

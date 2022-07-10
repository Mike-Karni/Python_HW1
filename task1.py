# Homework number 1

dayWeek= input("Введите номер дня недели от 1 до 7 ")
try:
    dayWeek = int(dayWeek)
except:
    print(" СКАЗАНО ЖЕ ####ь номер ввести.НОМЕР! ")

def CheckHolidays(number):
    if number < 1 or number > 7:
        print("Такого дня недели не существует. В неделе 7 дней.")
    elif number == 6 or number == 7:
        print("Этот день недели является выходным")
    else:
        print("Этот день недели является будничным")

CheckHolidays(dayWeek)
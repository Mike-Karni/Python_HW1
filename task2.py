coordinateX = input("Введите координату X = ")
try:
    coordinateX = int(coordinateX)
except:
    print("Вы ввели не ЧИСЛО!Повторите заново работу программы")

coordinateY = input("Введите координату Y = ")
try:
    coordinateY = int(coordinateY)
except:
    print("Вы ввели не ЧИСЛО!Повторите заново работу программы")


def QuarterNumber(a,b):
    if a == 0 or b == 0:
        print("Число не находится ни в одной плоскости!")
    elif a > 0 and b > 0:
        print("Число находится в координатной четверти 1")
    elif a < 0 and b > 0:
        print("Число находится в координатной четверти 2")
    elif a < 0 and b < 0:
        print("Число находится в координатной четверти 3")
    else:
        print("Число находится в координатной четверти 4")

QuarterNumber(coordinateX,coordinateY)
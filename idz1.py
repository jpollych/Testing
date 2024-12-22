""" Module test program for lr1. """
NAME = 'Новосельцева П.И.'
GROUP = '3586'
STRING = "Тестовая программа " + NAME + " группа " + GROUP
with open("test.txt", 'ta', encoding="utf-8") as f:
    print(STRING, sep="\n", file=f)
    f.close()
    print(STRING, sep="\n")
    print ("тестовый", "вывод", "на экран")
N= 25
X= 0.5
print(N + X) # проверить значение x в отладчике
print(N - X) # проверить значение n - x в отладчике
print(N * X)
print(N / X) # проверить значение n / x в отладчике
print(N ** X)

from math import log10


# Вычисление простого арифметического выражения со знаками "+-*:/"
# без скобок с учетом приоритета операций
def schet(arr):
    res = 0

    for w in ["*:/", "+-"]:
        c = 0
        for q in range(len(arr[:])):
            q += c
            if str(arr[q]) in w:
                x1 = arr[q - 1]
                x2 = arr[q + 1]
                if arr[q] == '*':
                    res = x1 * x2
                elif arr[q] == ':' or arr[q] == '/':
                    res = x1 / x2
                elif arr[q] == '+':
                    res = x1 + x2
                elif arr[q] == '-':
                    res = x1 - x2
                arr[q - 1] = res
                arr.pop(q)
                arr.pop(q)
                c -= 2

        arr = [i for i in arr if i != ""]

    return arr[0]


# Отделение каждого знака арифметической операции или скобки пробелами
# с двух сторон (на случай если этого не сделал пользователь) для корректного разделения
def prime(a):
    c = 0

    if "log10(" in a:
        a = a.split("log10(")
        for q in range(1, len(a)):
            ot = 0
            za = 0
            for w in range(len(a[q])):
                if a[q][w] == "(":
                    ot += 1
                elif a[q][w] == ")":
                    za += 1
                if za > ot: break
            a[q] = str(log10(int(prime(a[q][:w])))) + a[q][w + 1:]
    a = ''.join(a)

    for q in range(len(a[:])):
        q += c
        if a[q] in "()+-*:/":
            a = a[:q] + " " + a[q] + " " + a[q + 1:]
            c += 2

    arr = a.split()

    # Смена типа из строки в числа
    for q in range(len(arr)):
        if len(arr[q]) == len([i for i in arr[q] if i in '0123456789.']):
            arr[q] = float(arr[q])

    # Подсчет скобок с учетом приоритета операций
    while ")" in arr:
        for q in range(len(arr)):
            if arr[q] == ")":
                break
        for w in range(len(arr[:q]), 0, -1):
            if arr[w] == "(":
                break
        res = schet(arr[w + 1:q])
        arr = arr[:w] + [res] + arr[q + 1:]

    # Вычисление упрощенного выражения
    itog = schet(arr)
    return itog


print("Здравствуйте, это калькулятор арифметических выражений\n"
      "Введите пример, который необходимо вычислить")

a = input()

if a == "":
    a = "log10(1+9) + (7 * 6) - 3 * (1 + 32 - 33) + log10(10)"  # Пример выражения на случай пустой строки
print(prime(a))

while len("".join(a.split("log10("))) != len([i for i in "".join(a.split("log10(")) if i in " 0123456789()+-*/:"]):
    print("Введенный пример содержит лишние символы, пожалуйста используйте только арабские цифры,\n"
          "знаки арифметических операций (+-:/*) и скобки\n"
          "Введите пример снова")
    a = input()
    if a == "":
        a = "1 + (7 * 6) - 3 * (1 + 32 - 33)"
    print(prime(a))

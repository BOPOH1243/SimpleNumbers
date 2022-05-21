n = int(input("n=")) #ввод числа и преобразование его в int
def FindNumbers(number):
    lst = []
    for i in range(2, number): #для каждого i между 2 и number
        for j in range(2, i):
            if i % j == 0:
                # если делитель найден, число не простое.
                break
        else:
            lst.append(i)
    return lst
numbers = FindNumbers(n)
print(numbers)
print("Всего: "+str(len(numbers))+" чисел")

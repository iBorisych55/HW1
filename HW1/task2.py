#Задача 2: Найдите сумму цифр трехзначного числа.
n = int(input("Введите трехзначное число "))
summ = (n//100)+(n-((n//100)*100))//10+(n-((n//100)*100))%10
print("Сумма цифр числа",n,"равна :",summ)
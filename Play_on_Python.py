import random
import pandas as pd 

print("Привет! Это игра Города, пиши город, а я назову тебе следующий, потом ты пишешь на последнюю букву следующий город. Чтобы закончить напиши СТОП вместо города")
city = input('Введи город: ').lower()
using_cityes = []
# Счет количество городов
count = 0

while city!='стоп':
    using_cityes.append(city)
    cityes = []
    def SQL_city():
        # Загрузка данных из файла Excel в DataFrame
        df = pd.read_excel('c:/Users/Vladislav/Desktop/Python/spisok_gorodov_v_rossii-1021j.xlsx')

        # Извлечение содержимого столбца по его названию
        column_cities = df['Город'].tolist()
        for i in column_cities:
            if i!='none' and type(i)==str:
                if i[0].lower()==city[-1] and i not in using_cityes:
                    cityes.append(i)
                    using_cityes.append(i)
                elif city[-1]=="ы" or city[-1]=="ь":
                    if i[0].lower()==city[-2] and i not in using_cityes:
                        cityes.append(i+column_population[column_cities.find(i)])
                        using_cityes.append(i)
    SQL_city()
    while cityes==[] or len(city)<=1:
        city = input("Разве это город? ").lower()
        SQL_city()
    random_city = random.choice(cityes)
    print(random_city.upper())
    city = input("Пиши следующий город или стоп для окончания игры: ").lower()
    count+=2
    if city == "стоп":
        break
    elif random_city[-1]=="ь" or random_city[-1]=="ы":
        while city in using_cityes or city[0]!=random_city[-2]:
            city = input("Такой город уже был или буква не совпадает, пиши другой: ").lower()
    else:
        while city in using_cityes or city[0]!=random_city[-1]:
            city = input("Такой город уже был или буква не совпадает, пиши другой: ").lower()
print("Вот столько городов мы назвали:", count)
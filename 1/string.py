import pandas as pd #импорт библиотеки

df = pd.read_excel('КОЕ_Поверхность_кожи_живота_змеи.xlsx') #создание переменной содержащей файл

string = int(input('Bitte geben Sie eine Zeichenfolge ein: ')) #ввод

print(df.iloc[:,string]) #вывод строки

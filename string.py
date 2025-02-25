import pandas as pd #

df = pd.read_excel('КОЕ_Поверхность_кожи_живота_змеи.xlsx') #

string = int(input('Bitte geben Sie eine Zeichenfolge ein: ')) #

print(df.iloc[:,string]) #
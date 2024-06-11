import pandas as pd
import random
from termcolor import colored

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

df = pd.DataFrame({'whoAmI': lst})
print(colored("Исходный DataFrame:", 'green'))
print(df.head(), '\n')

def onehot_encode(df, column):
    # уникальные значения в указанном столбце
    unique_values = df[column].unique()
    
    # создаем пустой DataFrame для хранения one-hot кодировки
    one_hot_df = pd.DataFrame()
    
    # для каждого уникального значения
    for value in unique_values:
        # создаем новый столбец в one_hot_df
        # заполняем его 1, если значение в исходном столбце совпадает с текущим уникальным значением, иначе 0
        one_hot_df[value] = df[column].apply(lambda x: 1 if x == value else 0)

    return one_hot_df

# применяем функцию one-hot кодировки к столбцу whoAmI в df
one_hot_encoded_data = onehot_encode(df, 'whoAmI')

print(colored("One-hot DataFrame:", 'green'))
print(one_hot_encoded_data.head())

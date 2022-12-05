import pandas as pd

def lowercase(text):
    return text.lower()
 
df = pd.read_csv('data/datatesting.csv', encoding='utf-8')
kolom_text = df.iloc[:, 1]

test = "AAAAAAFFSFSFASF"

print("sebelum")
print(lowercase(test))
print('sesudah')

print(kolom_text)

print("berhasil")
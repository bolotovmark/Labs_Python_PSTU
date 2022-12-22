import requests
from bs4 import BeautifulSoup
from sklearn.datasets import load_digits

print("Введите числа через пробел:")
a = list(map(int, input().split()))
print(list(a))

url = 'https://www.statisticbrain.com/fun-facts/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
table = soup.find('table', cellspacing="0", cellpadding="2")
td_all = table.find_all('td')
fact_list = list(map(lambda temp: temp.contents[0], td_all))
fact_list.pop(0)
print(fact_list)

data = load_digits()
dictionary_wine = list(map(lambda temp: str(temp), data.target_names))
print(dictionary_wine)

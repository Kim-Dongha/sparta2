import requests
from bs4 import BeautifulSoup




for i in range(1, 50) :
    url = 'https://www.mangoplate.com/search/%EA%B0%95%EB%82%A8?keyword=%EA%B0%95%EB%82%A8&page=' + str(i)
    print(url)

    # 타겟 URL을 읽어서 HTML를 받아오고,
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url,
                        headers=headers)


    soup = BeautifulSoup(data.text, 'html.parser')



    title1 = soup.find_all('h2', 'title')
    list1 = []
    for i in title1:

        list1.append(i.text)

    title2 = soup.find_all('p', 'etc')
    list2 = []

    for i in title2:

        list2.append(i.text)

    for i in range(0, len(list1)):

        print(list1[i],list2[i])
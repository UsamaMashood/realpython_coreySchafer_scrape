from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
import openpyxl


ua = UserAgent()

header = {
    'user-agent' : ua.chrome
}

data = requests.get('https://realpython.com/interview-corey-schafer/',headers=header, timeout = 3).text

soup = BeautifulSoup(data,'lxml')

attr = {
    'class' : 'article-body'
}

para = soup.find_all('div',attrs=attr)

attr = {
    'class' : 'mt-5'
}

paragraph = soup.find_all('p', attrs=attr)
for question_ans in paragraph:
    print(question_ans.text)
    for cory_ans in question_ans.next_siblings:
            try:
                temp = cory_ans.text
                if not cory_ans.has_attr('class'):
                    print(temp,end='')
                else:
                    break
            except:
                pass
    print()

# print(para[0].prettify())
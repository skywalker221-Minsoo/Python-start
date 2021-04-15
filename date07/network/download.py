import requests
import pandas
from bs4 import BeautifulSoup


url = "https://movie.naver.com/movie/running/current.nhn"
result = requests.get(url)
#result
# print(result.content)

content = BeautifulSoup(result.content, "html.parser")
#content

dt_list = content.findAll("dt", {"class":"tit"})
#dt_list

# print(dt_list)
print(dt_list[0].find("a").text)
#
title=[]
for dt in dt_list:
    title.append(dt.find("a").text)

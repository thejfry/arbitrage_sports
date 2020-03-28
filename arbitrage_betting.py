import requests
from bs4 import BeautifulSoup

## sportsbetting
# url='https://www.sportsbetting.ag/sportsbook'
#
# r=requests.get(url)
# html=r.content
# soup=BeautifulSoup(html, "html.parser")
# games=soup.find_all("tbody",{"class":"event"})
#
# for game in games:
#     if game.find("tr",{"class":"eventseparator"}):
#         break
#     gameTime=game.find("td",{"class":"col_time bdevtt"}).text
#     team1_row=game.find("tr",{"class":"h2hSeq firstline"})
#     team1=team1_row.find("td",{"class":"col_teamname bdevtt"}).text
#     team1_hdcp=team1_row.find("td",{"class":"hdcp bdevtt"}).text
#     team1_odds=team1_row.find("td",{"class":"odds bdevtt displayOdds"}).text
#     team2_row=game.find("tr",{"class":"otherline"})
#     team2=team2_row.find("td",{"class":"col_teamname bdevtt"}).text
#     team2_hdcp=team2_row.find("td",{"class":"hdcp bdevtt"}).text
#     team2_odds=team2_row.find("td",{"class":"odds bdevtt displayOdds"}).text
#
#     print("gameTime:\n",gameTime)
#     print("team1:\n",team1,"\n",team1_hdcp,"\n",team1_odds)
#     print("team2:\n",team2,"\n",team2_hdcp,"\n",team2_odds)


## sports interaction betting site
# url='https://www.sportsinteraction.com/volleyball/international/world-league-betting/'

# r=requests.get(url)
# html=r.content
# soup=BeautifulSoup(html, "html.parser")
# games = soup.find_all("div",{"class":"game"})

# for game in games:
#     gameTime = game.find("h3",{"class":"gameHeader"}).find("span",{"class":"time"}).text.replace("\t","").replace("\n","")
#     runners = game.find_all("ul",{"class":"runnerListRow twoWay"})
#     if len(runners)==0:
#         break
#     boxes = runners[0].find_all("li",{"class":"runner"})
#     team1 = boxes[0].find("span",{"class":"name"}).text
#     team1_odds = boxes[0].find("span",{"class":"price wide"}).text
#     team2 = boxes[1].find("span",{"class":"name"}).text
#     team2_odds = boxes[1].find("span",{"class":"price wide"}).text
#     print(gameTime)
#     print(team1)
#     print(team1_odds)
#     print(team2)
#     print(team2_odds)
#     print(" ")


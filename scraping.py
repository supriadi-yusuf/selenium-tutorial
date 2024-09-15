from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import os


website = 'https://www.adamchoi.co.uk/overs/detailed'

driver = webdriver.Chrome()

# open website with selenium, chrome will be launched in new window
driver.get(website)

#title = driver.title
#print(title)

# find button
all_matches_button = driver.find_element(by=By.XPATH, value='//label[@analytics-event="All matches"]')

# click on the button
all_matches_button.click()

dates_ = []
home_teams = []
scores = []
away_teams = []

matches = driver.find_elements(by=By.TAG_NAME, value='tr')
for match in matches:

    # search td from current context
    if len(match.find_elements(by=By.XPATH,value='./td')) == 4:

        # search td from current context
        date_ = match.find_element(by=By.XPATH,value='./td[1]').text
        dates_.append(date_)

        home_team = match.find_element(by=By.XPATH,value='./td[2]').text
        home_teams.append(home_team)

        score = match.find_element(by=By.XPATH,value='./td[3]').text
        scores.append(score)

        away_team = match.find_element(by=By.XPATH,value='./td[4]').text
        away_teams.append(away_team)

# driver.implicitly_wait(5)
#time.sleep(5)

# close website, the launched chrome will be closed
driver.quit()

try:
    os.mkdir('result')
except FileExistsError:
    pass

df = pd.DataFrame({
    'date': dates_,
    'home team': home_teams,
    'score': scores,
    'away team': away_teams
    })

df.to_csv('result/footbal_game.csv', index=False)
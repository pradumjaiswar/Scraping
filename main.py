import requests
from bs4 import BeautifulSoup
import csv
url = "https://www.hdfcbank.com/personal/pay/cards/credit-cards"
#Get the HTML
r = requests.get(url)
htmlContent = r.content
#Parse the HTML
soup = BeautifulSoup(htmlContent,'html.parser')
#HTML tree traversal
cards = soup.find_all('div', {'class': 'product-card'})
results = []
for card in cards:
    card_name = card.find('h3').text.strip()
    card_fee = card.find('div', {'class': 'card-fee'}).text.strip()
    reward_points = card.find('div', {'class': 'reward-points'}).text.strip()
    lounge_access = card.find('div', {'class': 'lounge-access'}).text.strip()
    milestone_benefit = card.find('div', {'class': 'milestone-benefit'}).text.strip()
    fee_reversal_condition = card.find('div', {'class': 'fee-reversal-condition'}).text.strip()

    results.append([card_name, card_fee, reward_points, lounge_access, milestone_benefit, fee_reversal_condition])

with open('hdfc_credit_cards.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Card Name', 'Card fee', 'Reward points/percentage per 100 spent', 'Lounge access', 'Milestone benefit', 'Card fee reversal condition if any'])
    writer.writerows(results)

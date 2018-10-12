import requests

api_username = "3bad08cc125bc6002ca6ad08498d8f88"
api_password = "23e632c550c5331736b7905c0b587e46"
base_url = "https://api.intrinio.com/historical_data?identifier=PVTL&item=close_price&start_date=2018-03-25&end_date=2020-10-11&frequency=daily&type=count&page_number=1&page_size=10"

ticker = "PVTL"
requests_url = base_url + "/financials/standardized"
query_params = {
    'ticker': 'income_statement',
    'type': 'FY'
}

response = requests.get(requests_url, params=query_params, auth=(api_username, api_password))
if response.status_code == 401:
    print("Unautherized! Check your username and password.")
    exit()
data = response.json()['data']

for row in data:
    for value in row:
        print(value)




def buyOrNah(dayAverage, CurrentPrice):
    dayAverage = float(dayAverage)
    CurrentPrice = float(CurrentPrice)
  
    if dayAverage == CurrentPrice:
        print("Buy Stock")
    elif dayAverage > CurrentPrice:
        theDiff = dayAverage - CurrentPrice
        print("The Stock price is lower than the average by:" + str(theDiff))
    else:
        print("Do not Buy Stock") 

def main():
    print(buyOrNah(input("Enter The Day Average:"), input("Enter The Current Price:")))

if __name__ == "__main__":
    main()


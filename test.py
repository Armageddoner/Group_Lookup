import requests
import os
from dotenv import load_dotenv

load_dotenv()

auth_key = os.getenv('API_KEY')

g_id = 826277858
url = f'https://groups.roblox.com/v1/groups/{g_id}'


result = requests.get(url)

print(result.status_code)
data = result.json()
print(data['name'], data['owner'])

# Gets user input for a ROBLOX group id. This will run until a number has been inputted
def get_group() -> int:
    
    while True:
        try:
            id = int(input("Input a ROBLOX Group ID: "))
            return id
        except:
            print("Invalid syntax!")


get_group()
import requests
import os
from dotenv import load_dotenv

load_dotenv()

auth_key = os.getenv('API_KEY')

# print(data['name'], data['owner'])

# Checks if the inputted group exists
# If validated, returns data in a JSON format.
def validate_request(group_id: int):
    url = f'https://groups.roblox.com/v1/groups/{group_id}'
    result = requests.get(url)

    if result.status_code == 200:
        data = result.json()
        print(f"Pinged group: {data['name']}")
        return data
    else:
        print(f"Could not validate group [Error code: {result.status_code}]")
    

# Gets user input for a ROBLOX group id. This will run until a number has been inputted
def get_group() -> int:
    
    while True:
        try:
            id = int(input("Input a ROBLOX Group ID: "))
            return id
        except:
            print("Invalid syntax!")


if __name__ == "__main__":
    group_id = get_group()
    data = validate_request(group_id)
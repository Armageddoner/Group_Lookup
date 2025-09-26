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


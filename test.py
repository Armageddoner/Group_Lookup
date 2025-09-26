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

# Terminal menu to add more functionality to group checking
def menu(data):
    print("="*50)
    print(f'\nViewing Group: [{data['name']} ({data['id']})]\n"{data['description']}"\nActions below... (Numeric input)\n')
    print("(1). View Group Owner")
    print("(2). View Group Shout")
    print("(3). View Member Count")
    print("(4). View Verification Status")
    print("(5). View Group Owner")
    print("(6). Check if Locked")
    print("\n(7). EXIT")
    print("="*50)

    selection: int = NotImplemented
    while True:
        try:
            selection = int(input("Select an option: "))
            if selection > 7 or selection < 1:
                print("Defaulting to 1")
                selection = 1
            break
        except:
            print("Input a number within the range")
    
    match selection:
        case 1:
            print("Group Owner:")
            if data['owner'] != None:
                print(f'Name: {data['owner']['username']} ({data['owner']['displayName']})\nUserId: {data['owner']['userId']}\nVerified Badge: {data['owner']['hasVerifiedBadge']}')
            else:
                print("[None]")
        case 2:
            if data['shout']:
                print(f"Group Shout:\n{data['shout']['body']}")
            else:
                print("(No shout available.)")
                
                
    print("="*50)


if __name__ == "__main__":
    group_id = get_group()
    data = validate_request(group_id)
    if data:
        menu(data)
    else:
        print(f"[The group you provided ({group_id}) does not exist!]")
        
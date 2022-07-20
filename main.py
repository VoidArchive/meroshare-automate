from colorama import Fore
from meroshare import MeroShare
import json


asci_art = '''
                  .----.
      .---------. | == |
      |.-"""""-. | |----|
      | | | | | == |
      | | | | |----|
      |'-.....-' | |: : : : |
      `"")---(""` | ___.|
     /:::::::::::\" _  "
    /:::=======:::\`\`\
'''
# Remove encoding if json file is not encoded in utf-6
users = json.load(open('data/data.json', encoding='utf-8-sig'))

print(Fore.MAGENTA + asci_art)
print(Fore.BLUE + 'Welcome to IPO Automation for Meroshare')


while users:
    meroshare = MeroShare()
    user_input = input('Enter: Apply(a) or Check (c): ')
    if user_input.lower() == 'c':

        for user in users:
            try:
                meroshare.login(
                    name=user['Name'],
                    depository=user['DP'],
                    username=user['Username'],
                    password=user['Password']
                )

                print(meroshare.get_result(offer_row=0))
                meroshare.logout()
            except:
                print(f"Could not Log In on: {user['Name']}")
                break

        meroshare.close()
        break

    elif user_input.lower() == 'a':

        for user in users:
            try:
                meroshare.login(
                    name=user['Name'],
                    depository=user['DP'],
                    username=user['Username'],
                    password=user['Password']
                )
                meroshare.show_offering()
                row = 0
                # Comment this line if you're sure all account have same row structure, bonus or right share are provided.
                row = int(input("Enter the row no: "))
                meroshare.get_offering(offer_row=row)
                meroshare.apply_offering(crn=user['CRN'], pin=user['PIN'])
                meroshare.logout()

            except:
                # Bug? Sometimes, If a single loop give error. All loop stop. Why???
                print(f"-_- Something wrong with user: {user['Name']}")
                break
        meroshare.close()
        break
    else:
        print("Please Enter a or c for apply and check")

from sqlite3 import Row
from ipobot import MeroShare
import json
import sys


# Number of Kitta than you want to apply. (Default 10)
APPLIED_KITTA = 10

ROW_NO = sys.argv
# Call Meroshare class from ipobot
meroshare = MeroShare()

# Load JSON data file
file = open("data.json")
# file = open("example.json")
data = json.load(file)

print(ROW_NO)

for i in range(len(data)):
    try:
    # Login
        user = data[i]
        meroshare.login(user["DP"], user["Username"], user["Password"])

        # Fill the IPO Form and click proceed
        meroshare.check_ipo(ROW_NO[1])
        result = meroshare.get_result()
        print(f"{user['Name']}------------{result}")
        # Logout
        meroshare.logout()
    except Exception as e:
        print(f"Error on {user['Name']} ")



from ipobot import MeroShare
import json
import sys


# Number of Kitta than you want to apply. (Default 10)
APPLIED_KITTA = 10
# Call Meroshare class from ipobot
meroshare = MeroShare()
ROW_NO = sys.argv
# Load JSON data file
file = open("data.json")
# file = open("example.json")
data = json.load(file)


# Loop until last object in json file
for i in range(len(data)):
    try:
        user = data[i]
        # Login
        meroshare.login(user["DP"], user["Username"], user["Password"])
        # Go to My ASBA and click apply on the first IPO
        meroshare.find_ipo(int(ROW_NO[1]))
        # Fill the IPO Form and click proceed
        meroshare.apply_ipo(APPLIED_KITTA, user["CRN"])
        # Enter the transaction PIN

        meroshare.enter_pin(user["PIN"])
        # Logout
        meroshare.logout()

    except:
        print(f"Error on {user['Name']}")

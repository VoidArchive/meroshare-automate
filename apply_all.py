from ipobot import MeroShare
import json

# Number of Kitta than you want to apply. (Default 10)
APPLIED_KITTA = 10
# Call Meroshare class from ipobot
meroshare = MeroShare()

# Load JSON data file
file = open("data.json")
data = json.load(file)

# Loop until last object in json file
for i in range(len(data)): 
    try:
        user = data[i] 
        # Login 
        meroshare.login(user["DP"],user["Username"], user["Password"])
        # Go to My ASBA and click apply on the first IPO
        meroshare.find_ipo()
        # Fill the IPO Form and click proceed
        meroshare.apply_ipo(APPLIED_KITTA, user["CRN"])
        # Enter the transaction PIN
        meroshare.enter_pin(user["PIN"])
        print(f"{user['Name']: Applied}")
        # Logout
        meroshare.logout()
        
    except:
        print(f"Error on {user['Name']}")


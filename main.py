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
        meroshare.login(user["DP"],user["Username"], user["Password"])
        meroshare.find_ipo()
        # meroshare.apply_ipo(APPLIED_KITTA, data.crn)
        # meroshare.enter_pin(data.pin)
        meroshare.logout()
    except:
        print(f"Error on {user['Name']}")


from ipobot import MeroShare
import json

# Number of Kitta than you want to apply. (Default 10)
APPLIED_KITTA = 10
# Call Meroshare class from ipobot
meroshare = MeroShare()

# Load JSON data file
file = open("data.json")
# file = open("example.json")
data = json.load(file)


user = data[2] 
# Login 
meroshare.login(user["DP"],user["Username"], user["Password"])

# Fill the IPO Form and click proceed
meroshare.check_ipo()
meroshare.get_result()
# Logout

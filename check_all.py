from cgitb import reset
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


result = []
for i in range(len(data)):
    user = data[i]
    # Login
    meroshare.login(user["DP"], user["Username"], user["Password"])

    # Fill the IPO Form and click proceed
    meroshare.check_ipo(1)
    result += meroshare.get_result()

    # Logout
    meroshare.logout()

print(result)

# user = data[1]
# # Login
# meroshare.login(user["DP"], user["Username"], user["Password"])

# # Fill the IPO Form and click proceed
# meroshare.check_ipo(1)
# result = meroshare.get_result()



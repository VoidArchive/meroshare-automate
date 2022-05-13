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

# Loop until last object in json file

user = data[1] 
# Login 
meroshare.login(user["DP"],user["Username"], user["Password"])


test = meroshare.find_ipo(2)
print(len(test))

meroshare.logout()

from ipobot import CheckResult
import json

# check = CheckResult()

# Load json
file = open('data.json')
data = json.load(file)

# Loop and print result
for i in range(len(data)):
    user = data[i]

    print(user["BOID"])



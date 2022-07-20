import json
from meroshare import MeroShare


# [Loads Name, DP, Username, Password, CRN, BOID, PIN]
data = json.load(open('data/example.json'))
meroshare = MeroShare()
data = data[0]

meroshare.login(name=data['Name'], depository=data['DP'],
                username=data['Username'], password=data['Password'])
meroshare.show_offering()
# meroshare.get_offering(0)
# meroshare.apply_offering(data['CRN'], data['PIN'])
# meroshare.logout()
a = meroshare.get_result(0)
print(a)

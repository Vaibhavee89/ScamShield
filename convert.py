import json
import pandas as pd

# Read the JSON file
with open('realAccountData.json', 'r') as json_file:
    data = json.load(json_file)
# with open('nonAutomatedAccountData.json', 'r') as json_file:
#     data = json.load(json_file)
# with open('fakeAccountData.json', 'r') as json_file:
#     data = json.load(json_file)
# with open('automatedAccountData (5).json', 'r') as json_file:
#     data = json.load(json_file)

# Convert the JSON data to a DataFrame
df = pd.json_normalize(data)

# Save as CSV
# df.to_csv('fakeAccountData.csv', index=False)
# df.to_csv('realAccountData.csv', index=False)
df.to_csv('nonAutomatedAccountData.csv', index=False)
# df.to_csv('automated.csv', index=False)

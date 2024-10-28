import openai
import json


acm_papers = {'yes': 0, 'no': 0}
ieee_papers = {'yes': 0, 'no': 0}



with open('./modified_data_ieee.json', 'r') as file_acm, open('./modified_data_acm.json', 'r') as file_ieee:
    data_ieee = json.load(file_ieee)
    data_acm = json.load(file_acm)


# Loop through each entry and add a new field 'country' to each entry
for entry in data_acm:
    if entry['verdict'] == "YES":
        acm_papers["yes"] += 1
    else:
        acm_papers["no"] += 1
    print(acm_papers)
    
for entry in data_ieee:
    if entry['verdict'] == "YES":
        ieee_papers["yes"] += 1
    else:
        ieee_papers["no"] += 1
    print(ieee_papers)


# You can also write the modified data back to a file if needed
with open('count_ieee.json', 'w') as file:
    json.dump(ieee_papers, file, indent=2)

with open('count_acm.json', 'w') as file:
    json.dump(acm_papers, file, indent=2)
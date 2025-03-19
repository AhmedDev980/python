# Get pull requests information on a Github repo using python
# Algorithm: 1. Python will connect to git hub using API of github 
# 2. Request module is used to connect to Git Hub API.
# 3. We will get the out put in json format. We need to convert it to dictonary as it is readable by python.
# 4. print the output.

import requests
# refer this  for pull api https://docs.github.com/en/rest/pulls/pulls?apiVersion=2022-11-28
# below example https://github.com/AhmedDev980/python/pulls

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
full_details = response.json()

# len is used to do the itrations in full_details output if it has list of items to be executed.
# Without len(), you wouldn’t know how many iterations to run, so the loop might not process all elements of the list. len() is a simple and effective way to make sure your loop runs the correct number of times.
for i in range(len(full_details)):
  print(full_details[i]["user"]["login"])

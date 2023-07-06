
#Define a dictionary
teams = {"Hamilton":"Mercedes AMG Patronas F1","Max":"Redbull"}
print(teams)
print(teams["Hamilton"])
print(teams["Max"])
#Adding values to dict 
teams["Russell"] = "Mercedes AMG Patronas F1"
print(teams["Russell"])
print(teams)

newDriver = {"Perez":"Redbull"}
teams.update(newDriver)
print(teams)
print(len(teams))

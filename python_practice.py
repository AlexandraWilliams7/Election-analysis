counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties")
else: 
    print("El Paso is not in counties")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of Counties.")
else: 
    print("Arapahoe or El Paso is not in the list of Counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso are in the list of Counties.")
else: 
    print("Arapahoe and El Paso is not in the list of Counties.")

for county in counties:
    print(county)

counties_dict = {"Arapahoe": 422829,"Denver": 463353,"Jefferson": 432438}
for county in counties_dict:
    print(county)

counties_dict.keys() = {"Arapahoe": 422829,"Denver": 463353,"Jefferson": 432438}
for county in counties_dict:
    print(county)
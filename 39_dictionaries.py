#39 Dictionaries
#dictionary of states
states = {
    'New Hampshire': 'NH',
    'Massachusetts': 'MA',
    'Maine': 'ME',
    'Vermont': 'VT',
    'Connecticut': 'CT',
    'Rhode Island': 'RI'
}
#dictionary of cities
cities = {
    'NH': 'Milford',
    'MA': 'Boston',
    'VT': 'Burlington'
}
#adding cities to the existing dictionary
cities['ME'] = 'Portland'
cities['CT'] = 'Manchester'
cities['RI'] = 'Providence'

#prints some states' cities
print('-' *10)
print("NH has: ", cities['NH'])
print("MA has: ", cities['MA'])

#print some states
print('-'*10)
print("New Hampshire's abbreviation is: ", states['New Hampshire'])
print("Vermont's abbreviation is: ", states['Vermont'])
print("Rhode Island's abbreviation is: ", states['Rhode Island'])

#print by using the state then cities dict
print('-'*10)
print("Maine has: ", cities[states['Maine']])
print("Connecticut has: ", cities[states['Connecticut']])
print("Massachusetts has: ", cities[states['Massachusetts']])

#print every state abbreviation
print('-'*10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

#print every city in state
print('-'*10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

#fuuuuusion, ha!
print('-'*10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
    print(f"amd has city {cities[abbrev]}")

print('-'*10)
state = states.get('California')

if not state:
    print("Stay in New England")

city = cities.get('CA', 'Does not exist')
print(f"The city for the state 'CA' {city}")

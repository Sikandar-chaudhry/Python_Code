people = [
    {"name":"Sikander","country":"Pakistan"},
    {"name":"Asim","country":"UK"},
    {"name":"Hamza","country":"Pakistan"},
    {"name":"Qasim","country":"UK"}
]
#One way to do sorting because python doesnt know how to do it

# def f(person):
#     return person["country"]

# Usinf lambda
people.sort(key = lambda person: person["name"])

print(people)
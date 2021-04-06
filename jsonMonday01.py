#!/usr/bin/python3

myJSON = {"message": "success", "number": 7, "people": [{"craft": "ISS", "name": "Sergey Ryzhikov"}, {"craft": "ISS", "name": "Kate Rubins"}, {"craft": "ISS", "name": "Sergey Kud-Sverchkov"}, {"craft": "ISS", "name": "Mike Hopkins"}, {"craft": "ISS", "name": "Victor Glover"}, {"craft": "ISS", "name": "Shannon Walker"}, {"craft": "ISS", "name": "Soichi Noguchi"}]}


print(myJSON)


# this should just display 7 on the screen
print(myJSON.get("number"))

# this should display {"craft": "ISS", "name": "Kate Rubins"}
print(myJSON.get("people")[1])

# just display "Kate Rubins"
print(myJSON.get("people")[1].get("name"))

# just display "Kate"
print(myJSON.get("people")[1].get("name").split()[0])

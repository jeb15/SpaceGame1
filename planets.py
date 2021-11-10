#dictionary
#planets = {
#        "Earth": 'Green planet with lots of water.',
#        "CORDS": '0,0'
#}

planets = [ { "name" : "Earth", "xcord" : 0, "ycord": 0, "description" : "Green planet with lots of water." }
          , { "name" : "Alpha Prox", "xcord" : 0, "ycord": 4.765, "description" : "Earth's nearest neighbor" } ]

for p in planets:
    print(p["name"])

for x in planets:
    print(x["xcord"])

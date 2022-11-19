ponds = [
    {"pk": 1, "volume": 10000, "fish": "тунец"},
    {"pk": 192, "volume": 20000, "fish": "морская камбала"},
    {"pk": 206, "volume": 10000, "fish": "треска"},
    {"pk": 322, "volume": 25000, "fish": "тунец"},
    {"pk": 420, "volume": 20000, "fish": "морская камбала"},
    {"pk": 704, "volume": 10000, "fish": "треска"},
    {"pk": 920, "volume": 25000, "fish": "тунец"},
]

pond = []
for i in ponds:
    if i["fish"] == "тунец":
        del i["fish"]
    else:
        pond.append(i)

for i in pond:
    print(i["pk"])

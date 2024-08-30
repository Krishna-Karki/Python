d = {
    "name" : "Krishna",
    "age" : 21,
    "language" : "Nepali"
}
print(d.items())
print(d.keys())
print(d.values())

d.update({"language":"english"})
d.update({"address":"ktm"})

print(d)
print(d["age"])
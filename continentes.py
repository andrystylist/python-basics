archivo = open('countries-continents.csv', 'r')

titles = archivo.readline()

continent_temp = ""
continents = []

# [ { "Africa": 54 }, { "Asia": 20 } ]

while True:
    line = archivo.readline()

    if not line:
        break

    continent, country = line.split(",")
    print(continent, country)

    

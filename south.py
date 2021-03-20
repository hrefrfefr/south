import sys
from Samples.geocoder import geocode


def main():
    cities = sys.argv[1:]
    south_most_lattitude = 100.0
    south_most_city = ""
    for city in cities:
        toponym = geocode(city)
        toponym_coodrinates = toponym["Point"]["pos"]
        toponym_lattitude = float(toponym_coodrinates.split(" ")[1])
        if toponym_lattitude < south_most_lattitude:
            south_most_lattitude = toponym_lattitude
            south_most_city = city
    if south_most_city:
        print(south_most_city)


if __name__ == "__main__":
    main()
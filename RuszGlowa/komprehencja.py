from datetime import datetime


# import pprint

def convert2ampm(time24: str):
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


# if __name__ == "__main__":
# with open('buzzers.csv') as data: #nie ma takiego pliku madafaka
# ignore = data.readline()
# flights = {}
# for line in data:
# k, v = line.strip().split(',')
# flights[k] = v

# pprint.pprint(flights)
# print()

# flights2 = {}
# for k,v in flights.items():
# flights2[convert2ampm(k)] = v.title()

# pprint.pprint(flights2)

if __name__ == "__main__":
    flights3 = {'09:35': 'FREEPORT',
                '9:55': 'WEST END',
                '10:45': 'TREASURE CAY',
                '11:45': 'ROCK SOUND',
                '12:00': 'KUKURUMBA'}

    flights_times = []
    for ft in flights3.keys():
        flights_times.append(convert2ampm(ft))
    print(flights_times)

    destinations = []
    for desc in flights3.values():
        destinations.append(desc.title())
    print(destinations)

    more_dests = []
    more_desc = [dest.title() for dest in flights3.values()]
    print(more_desc)
    just_freeport2 = {convert2ampm(k): v.title() for k, v in flights3.items() if v == 'FREEPORT'}
    print(just_freeport2)
    just_freeport = {}
    for k, v in flights3.items():
        if v == 'FREEPORT':
            just_freeport[convert2ampm(k)] = v.title()
    print(just_freeport)

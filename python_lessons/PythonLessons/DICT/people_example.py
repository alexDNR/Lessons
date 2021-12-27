people = {
    'abogatyr':{
        'first':'aleksandr',
        'last':'bogatyr',
        'location':'donetsk'
        },
    'pserdobinceva':{
        'first':'polina',
        'last':'serdobinceva',
        'location':'donetsk'
        },
    'afriends':{
        'first':'all',
        'last':'friends',
        'location':'zhdanovka'
        }
    }

for unit, people_info in people.items():
    print("\nFriend name: " + unit)
    full_name = people_info['first'] + " " + people_info['last']
    location = people_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

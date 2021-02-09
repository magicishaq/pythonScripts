market_2nd = {'north': 'green' , 'south' : 'red'}

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] == 'green'
    assert 'red' in intersection.values(), 'neither light is red!' + str(intersection)

switchLights(market_2nd)
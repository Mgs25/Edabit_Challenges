def cars(wheels, bodies, figures):
    return min((wheels//4,bodies,figures//2))
    
print(cars(7,1,2))
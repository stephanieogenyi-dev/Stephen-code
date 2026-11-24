def speed (distance,time):
    return distance/time

def force (mass,Acceleration):
    return mass*Acceleration

def density (mass,volume):
    return mass/volume

def work_done (force,distance):
    return force*distance

def pressure (force,area):
    return force/area

print ("speed:", speed(100,2))
print ("force:", force(10,5))
print("density:", density(100,10))
print("workdone:", work_done(10,5))
print("pressure:", pressure(10,2))
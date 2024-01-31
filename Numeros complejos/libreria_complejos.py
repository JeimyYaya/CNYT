import math

def suma(a,b):
    pr = a[0] + b[0]
    pi = a[1] + b[1]
    return (pr, pi)

def multiplicacion(a,b):
    pr = (a[0]*b[0]) - (a[1]*b[1])
    pi = (a[0]*b[1]) + (a[1]*b[0])
    return(pr, pi)

def resta(a, b):
    pr = a[0] - b[0]
    pi = a[1] - b[1]
    return (pr, pi)

def division(a, b):
    denominator = b[0]**2 + b[1]**2
    pr = ((a[0] * b[0]) + (a[1] * b[1])) / denominator
    pi = ((a[1] * b[0]) - (a[0] * b[1])) / denominator
    return (pr, pi)

def modulo(a):
    result = math.sqrt(a[0]**2 + a[1]**2)
    return result

def conjugado(a):
    return(a[0], -a[1])


def fase(a):
    fase = math.degrees(math.atan2(a[1], a[0]))
    return fase

def polar_cartesiano(a):
    pr = a[0] * math.cos(math.radians(a[1]))
    pi = a[0] * math.sin(math.radians(a[1]))
    return(pr, pi)

def cartesiano_polar(a):
    mod = modulo(a)
    tetha = fase(a)
    return (mod, tetha)



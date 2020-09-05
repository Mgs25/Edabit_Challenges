def num_layers(n):
    return str((0.005*(2**n)/10)) +"m"

print(num_layers(5))

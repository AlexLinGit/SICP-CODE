motorcycles = ['honda', 'yamaha', 'fuckcycle']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(0, 'shitzuki')
print(motorcycles)

del motorcycles[0]
del motorcycles[1]
print(motorcycles)

pop_motorcycles = motorcycles.pop(1)
print("I don't own a/an " + pop_motorcycles.title() + 
".")

no_moto = 'suzuki'
motorcycles.remove(no_moto)
print("I can't find a " + no_moto.title() + ".")

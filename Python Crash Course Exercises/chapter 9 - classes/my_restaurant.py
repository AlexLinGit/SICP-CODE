from restaurant import IceCreamStand, Restaurants

richies = IceCreamStand(name='richies', cuisine_type='ice cream stand')
richies.flavors = ['chocolate', 'vanilla', 'tart', 'cookies & cream']
richies.menu()
richies.set_served(46)
richies.increment_served(-98)
richies.customers()

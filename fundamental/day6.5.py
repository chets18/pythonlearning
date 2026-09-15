#args, kwargs examples

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg,end=" ")
    print()
    for key, value in kwargs.items():
        print(f"{key} = {value} ", end=" ")


shipping_label("Dr.", "sakalaka", "boom", "III",
               street="fahh st.", city="kathmandu", state="bagmati", zip="44650")


# AND

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('street')}")


    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")
    
shipping_label("Dr.","sakalaka", "boom", "III",
               street="fahh st.", apt="I",city="kathmandu", state="bagmati", zip="44650")

# **args = (arguments)** you can pass as many as you want
# **kwargs = (keyword arguments)** dictionary arguments 
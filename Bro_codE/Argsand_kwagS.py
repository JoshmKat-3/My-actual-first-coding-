#def add(*args):
#   total = 0
#   for arg in args:
#       total += arg
#   return total
#
#print(add(1, 2, 3, 4, 5, 6, 7, 8, 9))

#def display_name(*args):
#   print(f"Hello", end=" ")
#   for arg in args:
#       print(arg, end=" ")

#display_name("Mr.", "John", "Fitzgerald", "Kennedy",)

#def print_address(**kwargs):
#    for value in kwargs.values():
#        print(value, end=" ")

#print_address(street="Ecc road",
#              pobox="P.O Box 93932",
#              city="Changshu",
#              province="Bengaluru",
#              zip="59322")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Mr.", "John", "Fitzgerald", "Kennedy")
             street="Ecc road",
               pobox="P.O Box 93932",
               city="Changshu",
               province="Bengaluru",
               zip="59322"


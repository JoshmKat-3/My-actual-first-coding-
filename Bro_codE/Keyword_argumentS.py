
#def hello(greeting, title, first, last):
#    print(f"{greeting} {title}{first} {last}")

#hello("Hello", title="Mrs.", last="Lawrence", first="Jennifer")

#for number in range(1, 11):
#    print(number, end="*")

#print()
#print("1", "2", "3", "4", "5", sep="_")

def get_phone(country, first,provider, numbers):
    return f"{country}-{first}-{provider}-{numbers}"

phone_num = get_phone(country="+260", first=9,provider=7, numbers=9374993)
print(phone_num)

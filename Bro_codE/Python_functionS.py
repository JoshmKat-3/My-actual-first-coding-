#def display_invoice(username, amount, due_date):
#   print(f"Hello {username}")
#   print(f"You need to pay ${amount:.2f} back by: {due_date}")

#display_invoice("JorgeFine", 66.66666666667, "21/12")


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("Henry", "Hart")
print(full_name)
from data import *

def input_name():
    name = ""
    while name == "":
        n = input("Enter your name: ").strip().lower()
        if n == "":
            print("Name cannot be empty")
        elif n.isnumeric():
            print("Name can't be a number")
        elif n.isalpha():
            name = n
            return name
        else:
            print(f"Name error: {n}")


def input_drink():
    print_drinks()
    drink = ""
    while drink == "":
        d = input("Choose your drink: ").strip()
        if d == "":
            print("Drink choice cannot be empty")
        elif not d.isnumeric():
            print("Choose one of the numbers")
        elif int(d) >= 0 and int(d) < len(list_of_drinks):
            drink = d
            return list_of_drinks[int(drink)]
        else:
            print(f"Drink error: {d}")


def print_drinks():
    for (index, d) in enumerate(list_of_drinks, start=0):
        print(f"{index}) {d}")


def input_size():
    print_sizes()
    size = ""
    while size == "":
        s = input("Choose your Size: ").strip()
        if s == "":
            print("Size choice cannot be empty")
        elif not s.isnumeric():
            print("Choose one of the numbers")
        elif int(s) >= 0 and int(s) < len(list_of_sizes):
            size = s
            return list_of_sizes[int(size)]
        else:
            print(f"Size error: {s}")


def print_sizes():
    for (index, s) in enumerate(list_of_sizes, start=0):
        print(f"{index}) {s}")


def input_extras():
    print_extras()
    extras = ""
    while extras == "":
        e = input("Choose your Extras: ").strip()
        if e == "":
            print("Extras choice cannot be empty")
        elif not e.isnumeric():
            print("Choose one of the numbers")
        elif int(e) >= 0 and int(e) < len(list_of_extras):
            extras = e
            return list_of_extras[int(extras)]
        else:
            print(f"Extras error: {e}")


def print_extras():
    for (index, e) in enumerate(list_of_extras, start=0):
        print(f"{index}) {e}")


def input_id():
    id = ""
    while id == "":
        i = input("Please input an order ID: ").strip()
        if i == "":
            print("ID cannot be empty")
        elif not i.isnumeric():
            print("Must be a number")
        elif i.isnumeric():
            id = i
            return id
        else:
            print(f"ID error: {i}")
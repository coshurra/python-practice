def greet_all(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}!")

greet_all("Wassup", "Artyom", "Danya")
def make_greeter(greeting):
    def greet(name):
        return f"{greeting}, {name}!"
    return greet

hello = make_greeter("Hello")
wassup = make_greeter("Wassup")

print(hello("Koresh"))
print(wassup("Koreshyha"))
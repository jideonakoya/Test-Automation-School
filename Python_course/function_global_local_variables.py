print("Global and Local variables\n")

name = "Testify"  # Global variable


def greet():
    language = "python"   # local variable
    print("Name", name, "language", language)


def hello():
    framework = "selenium"  # local variable
    print("Name", name, "framework", framework)


greet()
hello()


print("\nVariable shadowing")


platform = "Web"


def print_platform():
    platform = "Mobile"
    print(platform)


print_platform()
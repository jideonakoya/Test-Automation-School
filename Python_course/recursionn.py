print("Compare between while loop and Recursion\n")

def reduce_number_loop(num):
    while num >= 0:
        print(num)
        num -= 1


def reduce_number_recursion(num):
    print(num)
    if num == 0:
        return
    reduce_number_recursion(num-1)


reduce_number_loop(5)
print()  # to add an empty line
reduce_number_recursion(5)


print("RecursionError\n")


def print_hello():
    print("Hello World")
    print_hello()


# print_hello()

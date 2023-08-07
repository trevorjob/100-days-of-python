# def format_name(f_name, l_name):
#        '''''take first letter of name and make it uppercase'''
#        f_n = f_name.title()
#        l_n = l_name.title()
#        return f_n, l_n


# name_1, name_2 = format_name("kumdand", "JOB")


# print(name_1, name_2)

def add(n1, n2):
        return n1 + n2
def mul(n1, n2):
        return n1 * n2
def sub(n1, n2):
        return n1 - n2
def div(n1, n2):
        return n1 / n2

props = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div,
}

num1 = eval(input("first number "))

for i in props:
        print(i)
sign = input("pick a sign ")

num2 = eval(input("second 'number "))
funct = props[sign]
answer = funct(num1, num2)
print(f"{num1} {sign} {num2} = {answer}")










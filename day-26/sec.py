with open("f1.txt") as f1:
        first = f1.readlines()
        
with open("f2.txt") as f2:
        second = f2.readlines()

third = [int(num) for num in first if num in second]
print(third)

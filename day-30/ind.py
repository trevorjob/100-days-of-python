fruits = ["apple", "banana", "orange","pear"]

def make_pie(index):
        try:
                fruit = fruits[index]
        except:
                fruit = "fruit"
        else:
                print(f"{fruit} pie")
        
make_pie(4)
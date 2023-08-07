age :int

def police_check(age:int) -> bool:
        if age > 18:
                return 10
        else:
                return 0
        
        
if police_check(12):
        print("you may pass")
else:
        print("pay fine")
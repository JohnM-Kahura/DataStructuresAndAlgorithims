# Write a program that takes a double x and an integer y and retums x/. You can ignore overflow and
# underflow.

def power(x,y):
    result,power=1.0,y
    if y<0:
        power,x=power                    
    
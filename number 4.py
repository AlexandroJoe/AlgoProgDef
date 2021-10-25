def calc_new_weight():
    x = eval(input("Enter current width: "))
    y = eval(input("Enter current height: "))
    z = eval(input("Enter the desired width: "))
    while z > x:
        z = eval(input("Desire width must be smaller than current width, please re-enter: "))
   
    a = x / z
    b = y / a
    print("The corresponding height is: ", b)



calc_new_weight()
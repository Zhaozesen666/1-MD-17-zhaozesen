color1 = input("Введите первый цвет(red,blue,yellow):")
color2 = input("Введите второй цвет(red,blue,yellow):")
if (color1 == "red" and color2 == "blue") or (color1 == "blue" and color2 == "red"):
    print("mix red and blue got purple")
elif (color1 == "red" and color2 == "yellow") or (color1 == "yellow" and color2 == "red"):
    print("mix red and yellow got orange")
elif (color1 == "blue" and color2 == "yellow") or (color1 == "yellow" and color2 == "blue"):
    print("mix blue and yellow got green")
else:
    print("printed not right color,please print red,blue or yellow again")
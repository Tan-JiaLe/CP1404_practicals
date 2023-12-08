COLOR_NAME = {"Absolute Zero": "#0048ba", "Baby Blue": "#89cff0", "Blond": "#faf0be", "Canary": "#ffff99",
              "Denim": "#1560bd", "Ginger": "#b06500", "Gray": "#bebebe", "Iceberg": "#71a6d2", "Khaki": "#f0e68c",
              "Mango": "#fdbe02"}
color = input("Color name: ").title()
while color != '':
    if color in COLOR_NAME:
        print(f"Code of {color} is {COLOR_NAME[color]}")
    else:
        print("Invalid color")
    color = input("Color name: ").title()
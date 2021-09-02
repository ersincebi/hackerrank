x = {"Red":4/7, "Black":3/7}
y = {"Red":5/9, "Black":4/9}
z = {"Red":4/8, "Black":4/8}

firstPossibility = x["Red"] * y["Red"] * z["Black"]
secondPossibility = x["Red"] * y["Black"] * z["Red"]
thirdPossibility = x["Black"] * y["Red"] * z["Red"]

print(firstPossibility + secondPossibility + thirdPossibility)

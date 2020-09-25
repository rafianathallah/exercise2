print("Input your height: ")
f = int(input("Feet: "))
i = int(input("Inches: "))
i += f * 12
cm = i * 2.54 * 0.88

print("Suggested board length: ",cm)
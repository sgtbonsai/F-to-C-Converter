def convert_temp(scale=None, source_temp=None):
 if (scale == "F") or (scale == "f"):
    return 'C', (source_temp - 32.0) * (5.0/9.0)
 elif (scale == "C") or (scale == "c"):
    return 'F', (source_temp * (9.0/5.0)) + 32.0
 else:
    print("Uh oh, you didn't choose F or C! Please choose either F or C")

scale = input("> F or C? ")
source_temp = int(input("> What is the temperature you want to convert? " ))
s, m = convert_temp(scale, source_temp)
print(">",source_temp, "Degrees", scale.title(), "is", m, "Degrees", s)
print("> Program made by BosnaiSgt")
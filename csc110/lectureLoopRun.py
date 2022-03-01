
t = float(input("Enter Time: "))
d = float(input("Enter Distance: "))

fastest = d/t

i = 1
count = i

while i < 10:
    t = float(input("Enter Time: "))
    d = float(input("Enter Distance: "))

    speed = d / t
    j = 0

    if speed > fastest:
        speed = fastest
        count = i

    i += 1

print(fastest)
print(count)



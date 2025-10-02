sum = 0
num = int(input("Enter a number: "))
while num >= 0:
    sum += num
    print(f"sum is {sum}")
    num = int(input("Enter a number, negative number: "))

print("negative number entered. Program will now exit")
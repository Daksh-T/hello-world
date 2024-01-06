i = int(input("How many hellos are too many hellos? "))
if i == 1:
    print("Aww that's so sad, you don't want to say hello?")
if i <= 0:
    print("You're not making any sense!")
for i in range(i-1):
    print("Hello World!")
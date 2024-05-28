def handler():
    firstName = input("Enter your name: ")
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    name_list = firstName.split()
    for name in name_list:
        vowelCount = 0
        for i in range(0, len(name)):
            if name[i] in vowels:
                vowelCount += 1
        print("The name is", name, "and it contains", vowelCount, "vowels in it")



test = int(input())

for i in range(test):
    string1 = input()
    string2 = input()
    print(string1)
    print(string2)
    output = ""

    for j in range(len(string1)):
        if string1[j] == string2[j]:
            output += "."
        else:
            output += "*"
    
    print(output)
    print("")

n = int(input())

for i in range(0,n):
    Command = input().split()
    if (Command[0] == "Simon") and (Command[1] == "says"):
        Output = Command[2:]
        Formatted_Output = " ".join(Output)
        print(" " + Formatted_Output)	

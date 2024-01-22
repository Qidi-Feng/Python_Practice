def minion_game(string):
    # your code goes here
    stuart = 0
    kevin = 0
    vowels = ['A','E','I','O','U']
    for i in range(0,len(string)):
        if string[i] in vowels:
            kevin += len(string) - i  ###instead of loop from i to len(string)
        else:
            stuart += len(string) - i
        
    if stuart > kevin:
        print("Stuart", stuart)
    elif stuart == kevin:
        print("Draw")
    else:
        print("Kevin", kevin)
if __name__ == '__main__':

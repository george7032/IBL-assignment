
def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    
    else:
        print("Invalid")


def is_valid(s):

    if len(s) <2 or len(s)> 6:
        return False
#the first 2 must be alphabets thus the .isalpha() function
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
#checking if the first number is '0'
    i = 0
    while i < len(s):
        if s[i].isalpha() ==False:
            if s[i] == "o" :
                return False
            else:
                break
        i += 1
#No fullstop, comma, space,question marks
    for c in s:
        if c in [".", ",", " ", "!", "?"]:
            return False
    
    return True

main()   
    
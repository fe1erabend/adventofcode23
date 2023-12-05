sum = 0
with open("input1a.txt") as input:
    for line in input:
        digitstring = ""
        # for char in line:            
        #     if char.isdigit():
        #         digitstring += char

        x = line.find("two")

        #digits = digitstring[0] + digitstring[-1]
        #sum += int(digits)    
print(x)             
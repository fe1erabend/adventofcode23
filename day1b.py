import re

sum = 0

def parser(input):
    if input == 'one':
        return "1"
    elif input == 'two':
        return "2"
    elif input == 'three':
        return "3"
    elif input == 'four':
        return "4"
    elif input == 'five':
        return "5"
    elif input == 'six':
        return "6"
    elif input == 'seven':
        return "7"
    elif input == 'eight':
        return "8"
    elif input == 'nine':
        return "9"
    else:
        return input
    
with open("input1a.txt") as input:
    for line in input:
        findings = {}        
        for expression in ["one","1","two","2","three","3","four","4","five","5","six","6","seven","7","eight","8","nine","9"]:
            matches = [match.start() for match in re.finditer('(?={0})'.format(re.escape(expression)), line)]
            findings[expression] = matches
        filtered_findings = {key: value for key, value in findings.items() if value}            

        first_value = str(min(filtered_findings,key=lambda k: min(filtered_findings[k])))
        last_value = str(max(filtered_findings, key=lambda k: max(filtered_findings[k])))

        value = int(str(parser(first_value)) + str(parser(last_value)))       
        sum += value
print(sum)    
            
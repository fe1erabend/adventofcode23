import re
from word2number import w2n

sum = 0
    
with open("input1a.txt") as input:
    for line in input:
        findings = {}        
        for expression in ["one","1","two","2","three","3","four","4","five","5",
                           "six","6","seven","7","eight","8","nine","9"]:
            matches = [match.start() for match in re.finditer('(?={0})'.format(re.escape(expression)), line)]
            findings[expression] = matches
        filtered_findings = {key: value for key, value in findings.items() if value}            

        first_value = str(min(filtered_findings,key=lambda k: min(filtered_findings[k])))
        last_value = str(max(filtered_findings, key=lambda k: max(filtered_findings[k])))

        value = int(str(w2n.word_to_num(first_value)) + str(w2n.word_to_num(last_value)))       
        sum += value
print(sum)    
            
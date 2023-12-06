import re

sum = 0
total = 0

with open("input2a.txt") as input:
    for line in input:
        id = int((re.search(r"\d+(?=:)", line)).group())
        total += id        
        games = re.split(r";", line)

        for game in games:
            red = re.findall(r"\d+(?= red)",game)
            if red:
                if int(red[0]) > 12:
                    sum += id
                    break

            green = re.findall(r"\d+(?= green)",game)
            if green:
                if int(green[0]) > 13:
                    sum += id
                    break

            blue = re.findall(r"\d+(?= blue)",game)
            if blue:
                if int(blue[0]) > 14:
                    sum += id
                    break

print(total-sum)

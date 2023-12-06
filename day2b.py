import re

sum = 0

with open("input2a.txt") as input:
    for line in input:          
        games = re.split(r";", line)

        red_min = 0
        green_min = 0
        blue_min = 0
        gamepower = 0

        for game in games:
            
            red = re.findall(r"\d+(?= red)",game)
            if red:
                if int(red[0]) > red_min:
                    red_min = int(red[0])
                    

            green = re.findall(r"\d+(?= green)",game)
            if green:
                if int(green[0]) > green_min:
                    green_min = int(green[0])
                    

            blue = re.findall(r"\d+(?= blue)",game)
            if blue:
                if int(blue[0]) > blue_min:
                    blue_min = int(blue[0])
                       
        gamepower = red_min * green_min * blue_min
        #print(gamepower)
        sum += gamepower

print(sum)

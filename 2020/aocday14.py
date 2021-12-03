with open('/Users/andrewemmett/Projects/adventofcode/2020/day14input.txt') as file:
    data = [(line.strip()) for line in file.readlines()]
print(data)

# READ data
# recognise masks
# store mast as string (interable)
#identify location and value
# store address in memory or use as dictionary 
# convert value to binary string and pad with leading 0s to store as 36 bit element
# interate through mask and value string using zip
# apply mask via:
# if x use value
# else use mask
# convert string to binary and to decimal

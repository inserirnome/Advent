txt=open("aoc_day1.txt", "r")
lst=txt.read().splitlines()
res=0
def decode(line):
    s_line=""
    key={"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9", "zero":"0"}
    for char in line:
        s_line+=char
        for num, val in key.items():
            s_line = s_line.replace(num, val)
    return s_line
def get_num1(line):
    for char in line:
        if char.isdigit():
            return int(char)
def get_num2(line):
    for char in reversed(line):
        if char.isdigit():
            return int(char)


for line in lst:

    line=decode(line)
    num=str(get_num1(line))+str(get_num2(line))
    res+=int(num)
    print(num)


print(res)

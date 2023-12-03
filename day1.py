txt=open("aoc_day1.txt", "r")
lst=txt.read().splitlines()
def get_num1(line):
    for char in line:
        if char.isdigit():
            return int(char)
def get_num2(line):
    for char in reversed(line):
        if char.isdigit():
            return int(char)

res=0
for line in lst:

    num=str(get_num1(line))+str(get_num2(line))
    res+=int(num)


print (res)

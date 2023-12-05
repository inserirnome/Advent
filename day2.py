txt=open("aoc_day2.txt", "r")
lst=txt.read().splitlines()
res=0
res2=0
#part1
def get_game(line):
    return line[5:line.index(":")]
def r_check(line):
    s_line=line.split(";")
    r=0
    for roll in s_line:
        if roll.find("red") != -1:
            pos_r = roll.index("red")
            if int(roll[int(pos_r)-3:int(pos_r)-1].strip())>12:
                r+=1
    return r
def g_check(line):
    s_line = line.split(";")
    g=0
    for roll in s_line:
        if roll.find("green") != -1:
            pos_g = roll.index("green")
            if int(roll[int(pos_g)-3:int(pos_g)-1].strip())>13:
                g+=1
    return g
def b_check(line):
    s_line = line.split(";")
    b=0
    for roll in s_line:
        if roll.find("blue") != -1:
            pos_b = roll.index("blue")
            if int(roll[int(pos_b) - 3:int(pos_b) - 1].strip()) > 14:
                b+=1
    return b
for line in lst:
    if r_check(line) == 0 and g_check(line)==0 and b_check(line)==0:
        res+=int(get_game(line))
print("part1", res)
#part2
def get_r(line):
    s_line = line.split(";")
    r = 0
    for roll in s_line:
        if roll.find("red") != -1:
            pos_r = roll.index("red")
            if int(roll[int(pos_r) - 3:int(pos_r) - 1].strip()) > r:
                r =int(roll[int(pos_r) - 3:int(pos_r) - 1].strip())
    return r
def get_g(line):
    s_line = line.split(";")
    g= 0
    for roll in s_line:
        if roll.find("green") != -1:
            pos_g = roll.index("green")
            if int(roll[int(pos_g) - 3:int(pos_g) - 1].strip()) > g:
                g =int(roll[int(pos_g) - 3:int(pos_g) - 1].strip())
    return g
def get_b(line):
    s_line = line.split(";")
    b = 0
    for roll in s_line:
        if roll.find("blue") != -1:
            pos_b = roll.index("blue")
            if int(roll[int(pos_b) - 3:int(pos_b) - 1].strip()) > b:
                b =int(roll[int(pos_b) - 3:int(pos_b) - 1].strip())
    return b


for line in lst:
    res2+=int(get_r(line))*int(get_g(line))*int(get_b(line))
print("prt2", res2)


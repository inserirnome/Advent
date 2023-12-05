txt=open("aoc_day3.txt", "r")
lst=txt.read().splitlines()

l=len(lst)
linelist="".join(lst)
res=0
def get_num(lst):
  num_lst = []

  for line in lst:
    current_number = ""
    for char in line:
      if char.isdigit():
        current_number += char
      elif current_number:
        num_lst.append(int(current_number))
        current_number = ""

  return num_lst
def check_front(lst,x,lx):
  return any(not (char.isdigit() or char == ".") for char in linelist[x+lx])
def check_back(lst,x,lx):
    return True if linelist[x-1] != "." else False
def check_down(lst, x, lx):
  return any(not (char.isdigit() or char == ".") for char in linelist[x+l-1:x + l+lx+1])
def check_top(lst,x,lx):
  return any(not (char.isdigit() or char == ".") for char in linelist[x-l-1:x-l+lx+1])

for num in get_num(lst):
  lx=int(len(str(num)))
  x=int(linelist.find(str(num)))
  if check_top(lst,x,lx) or check_down(lst,x,lx) or check_back(lst,x,lx) or check_front(lst,x,lx):
    res+=int(num)
    print(num,res)

print(res)






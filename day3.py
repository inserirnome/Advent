txt=open("aoc_day11.txt", "r")
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
    if current_number:
      num_lst.append(int(current_number))

  return num_lst
def check_front(lst,x,lx):
  if x <l:
    i= (x+lx, x+lx+l)
  elif  x+l>len(linelist):
    i=(x+lx,x-l+lx)
  else:
    i=(x +lx, x + l +lx, x - l +lx)
  return any(char not in '0123456789.' for char in [linelist[index] for index in i])
def check_back(lst, x, lx):
    if x + l > len(linelist):
      i = (x - 1, x - l - 1)
    elif x <l:
      i = (x -1, x + l -1)
    else:
      i = (x - 1, x - l - 1, x + l - 1)
    return any(
      char not in '0123456789.' for char in [linelist[index] for index in i ])
def check_down(lst, x, lx):
  return any(not (char.isdigit() or char == ".") for char in linelist[x+l:x + l+lx])
def check_top(lst,x,lx):
  return any(not (char.isdigit() or char == ".") for char in linelist[x-l:x-l+lx])

for num in get_num(lst):
  lx=int(len(str(num)))
  x=int(linelist.find(str(num)))
  #print(num,"front",linelist[x+lx],linelist[x+lx+l],linelist[x-l+lx])
  #print(num, "back", linelist[x - 1], linelist[x - l - 1], linelist[x + l - 1])
  #print(num, "up", linelist[x-l:x-l+lx])
  #print(num, "down", linelist[x+l:x + l+lx])
  if x==0 or x%l==0:#encostado à esquerda da matriz---- ler só front
    if check_front(lst,x,lx) or check_top(lst,x,lx) or check_down(lst,x,lx):
      res+=int(num)
      print(num,"esq")
      print("b", check_back(lst, x, lx), "t", check_top(lst, x, lx), "d", check_down(lst, x, lx), "f",
            check_front(lst, x, lx))

  elif (x+lx)==l or (x+lx)%l==1: #encostado à direita, ler só back
    if check_back(lst,x,lx) or check_top(lst,x,lx) or check_down(lst,x,lx):
      res += int(num)
      print(num,"dta")
      print("b", check_back(lst, x, lx), "t", check_top(lst, x, lx), "d", check_down(lst, x, lx), "f",
            check_front(lst, x, lx))
  else:
    if check_back(lst,x,lx) or check_top(lst,x,lx) or check_down(lst,x,lx) or check_front(lst,x,lx):
      res += int(num)
      print(num,"meio")
      print("b",check_back(lst,x,lx),"t",check_top(lst,x,lx),"d",check_down(lst,x,lx),"f",check_front(lst,x,lx))

print(res)
print(get_num(lst))








run = True
t = []
while run:
  ins = input("exit to exit")
  if(ins == "exit"):
    run = False
  else:
    t.append(ins)


for s in t:
  print(s)

input("any key to continue")
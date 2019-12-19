
import matplotlib.pyplot as plt
plt.plot([0,1,2,3,4])
plt.show()
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
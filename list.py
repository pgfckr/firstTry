
import matplotlib.pyplot as plt

run = True
t = []
while run:
  ins = input("exit to exit ")
  if(ins == "exit"):
    run = False
  else:
    t.append(int(ins))


for s in t:
  print(s)

plt.plot(t)
plt.show()

input("any key to continue")
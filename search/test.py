

poses, start = input().split("/")
pos_list = []
for pos in poses.split(","):
   x = float(pos.split()[0])
   y = float(pos.split()[1])
   pos_list.append([x,y])
start = [float(start.split()[0]), float(start.split()[1])]
print(pos_list)
print(start)
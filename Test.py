s='Mohamed Gaye _MHD_'
print('\n'.join([s[:i] for i in range(3,len(s))] + [s[:i] for i in range(len(s), 2, -1)]))




num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = len(num_list)
while i >= 1:
 print(*num_list[0:i])
 i -= 1


for i in range(6, 0, -1):
      for k in range(1, i+1):
           print(k, "", end="")
      print(" ")


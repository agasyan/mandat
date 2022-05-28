file1 = open('res_5.txt', 'r')
Lines = file1.readlines()
  
count = 0
# Strips the newline character
for line in Lines:
    lne = line.strip()
    if lne.startswith("Time:"):
        tmp = lne.split(" ")
        tme = tmp[1]
        tmfl = float(tme)
        count += tmfl
print(count)
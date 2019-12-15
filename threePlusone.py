import functions as f

k=0
totalup=0.
totaldown=0.
#ranging through odd integers
for i in range(1,500000000):
    k+=1
    m=2*i-1
    sizen = f.count(m)
    j=3*m+1
    sizeup = f.count(j)
    sizedown = f.countdown(j)
    totalup+=(sizeup-sizen)
    totaldown+=sizedown
print(m)
print("Total up: ") #average binary digits up
print(totalup/k)
print("\nTotal down: ") #average binary digits down
print(totaldown/k)
print("\nTotal net: ") #average net change
print((totalup-totaldown)/k)

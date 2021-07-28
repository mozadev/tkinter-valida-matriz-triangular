matriz=[[1,2,6,0],[0,5,7,8],[0,0,8,3],[0,0,0,5]]
i=int(0)
band=True

for i in range(3):
    for j in range (3):
        print("\t", matriz[i][j], end=" ")
    print("\n")

while ((band)and (i<3)):
    for j in range(i+1,4):
        if(matriz[i][j]!=0):
            band=False
            break
    i=i+1
if (band==False):
    print(" la matriz es triangular superior")
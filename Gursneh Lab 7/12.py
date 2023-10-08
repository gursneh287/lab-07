N=int(input("enter a number: "))
 
hline="+/" + "\/" *(N-1) + "\+"
vline="|" +   "  "*(N) +   "|"
for i in range(N+2):
    if i==0 or i==N+1:
        print(hline)
    else:
        print(vline)
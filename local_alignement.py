import sys
def local(s1,s2):
    n=len(s1)
    m=len(s2)
    table=[[None]*(m+1) for i in range(n+1)]

    s=-2
    for i in range(n+1):
        for j in range(m+1):
            if i==0 or j==0:
                table[i][j]=0
            else:
                val=max(table[i-1][j]+s,table[i][j-1]+s)
                if s1[i-1]==s2[j-1]:
                    val=max(val,table[i-1][j-1]+1)
                else:
                    val=max(val,table[i-1][j-1]-1)
                table[i][j]=max(val,0)

    maxe=-1
    for i in range(n+1):
        for j in range(m+1):
            if table[i][j]>maxe:
                maxindx,maxindy=i,j
                maxe=table[i][j]

    print(maxe)
    
    i=maxindx
    j=maxindy
    ans=""
    while i>0 and j>0 and table[i][j]!=0:
        ans=ans+s1[i-1]
        i=i-1
        j=j-1

    for i in range(n+1):
        for j in range(m+1):
            print(table[i][j],end=" ")
        print()

    print(ans[::-1])


local("GCGCAATG","GCCCTAGCG")










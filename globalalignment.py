def needle(s1,s2):
    n=len(s1)
    m=len(s2)
    table=[[0]*(m+1) for i in range(n+1)]
    direc=[[None]*(m+1) for i in range(n+1)]

    s=-2
    for i in range(n+1):
        for j in range(m+1):
            if i==0 or j==0:
                if i!=0:
                    table[i][j]=s*i
                if j!=0:
                    table[i][j]=s*j
            else:
                u=table[i-1][j]+s
                l=table[i][j-1]+s
                d=table[i-1][j-1]
                if s1[i-1]==s2[j-1]:
                    d=d+1
                else:
                    d=d-1
                if u>d or l>d:
                    if u>l:
                        direc[i][j]='u'
                        table[i][j]=u
                    else:
                        direc[i][j]='l'
                        table[i][j]=l
                else:
                    direc[i][j]='d'
                    table[i][j]=d
    
    for i in range(n+1):
        for j in range(m+1):
            print(table[i][j],end=" ")
        print()

    i=n
    j=m
    ans1=""
    ans2=""
    while i>0 and j>0:
        if direc[i][j]=='d':
            ans1=ans1+s1[i-1]
            ans2=ans2+s2[j-1]
            i=i-1
            j=j-1
        elif direc[i][j]=='u':
            ans2=ans2+'-'
            ans1=ans1+s1[i-1]
            i=i-1
        elif direc[i][j]=='l':
            ans1=ans1+'-'
            ans2=ans2+s2[j-1]
            j=j-1

    print(ans1[::-1])
    print(ans2[::-1])


needle("GCGCAATG","GCCCTAGCG")
                


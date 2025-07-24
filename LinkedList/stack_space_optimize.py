def remove_pairs(s,a,b,gain):
    s=list(s)
    score=0
    write=0 #consider as a top of stack

    for read in range(len(s)):
        s[write]=s[read] #add character into a stack
        write+=1

        if write>=2 and s[write-2]==a and s[write-1]==b:
            score+=gain
            write-=2  #remove the pair
        
    return "".join(s[:write]),score

s="cdbcbbaaabab"
x=4
y=5
if x>y:
    s,sc1=remove_pairs(s,"a","b",x)
    s,sc2=remove_pairs(s,"b","a",y)
else:
    s,sc1=remove_pairs(s,"b","a",y)
    s,sc2=remove_pairs(s,"a","b",x)

print(sc1+sc2)


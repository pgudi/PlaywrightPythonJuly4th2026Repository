fn=0
sn=1
print(fn)
print(sn)

for i in range(1,9):
    tn=(fn + sn)
    print(tn)
    fn=sn
    sn=tn

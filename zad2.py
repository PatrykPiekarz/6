import random

n=raw_input("ilosc uczestnikow: ")
n=int(n)
random.seed()

class player:
    def __init__(self,p1,p2,p3):
        self.nr=p1
        self.pkt=p2
        self.id=p3
    def __lt__(self,other):
        return self.nr<other.nr

lst=[]
r=range(1,n+1)
random.shuffle(r)
for i in range(0,n):
    lst.append(player((r[i]),0,i))

kolo=range(-10,10)
f1=open("plik.txt","r")
f2=open("pliku.txt","w")
pom=f1.readline()
hasla=pom.split()
f1.seek(0)
haslo=random.choice(hasla)
haslo=str(haslo)
k=0

while 1==1:
    if k==0:
        print "losoje nowe haslo"
        haslo=random.choice(hasla)
        haslo=str(haslo)
        dlg=haslo.__len__()
        k=1
        print "haslo to \"%s\"" % (haslo)
    for i in lst:
        print "tura gracza %i" % (i.id)
        r=random.choice(kolo)
        print "wylosowano %i" % (r)
        if r==0:
            print "BANKRUT"
            i.pkt=0
            break
        c=raw_input("wpisz litere")
        c=str(c)
        if haslo.count(c)>0:
            dlg-=haslo.count(c)
            print "litera znajduje sie w hasle"
            if(r>0):
                i.pkt+=r
                print "dodano %i punkow, gracz %i ma w sumie %i punktow" % (r,i.id,i.pkt)
        c=raw_input("czy chcesz zgadnac haslo y/n?")
        c=str(c)
        if c=='y':
            s=raw_input("wpisz haslo")
            s=str(s)
            if(s==haslo):
                print "odgadnieto haslo: %s" % (haslo)
                i.pkt*=dlg
                print "gracz %i ma w sumie %i punktow" % (i.id,i.pkt)
                print "zapisuje wyniki do pliku txt"
                for j in lst:
                    print "gracz %i: %i pkt\n" % (j.id,j.pkt)
                    f2.write(("gracz %i: %i pkt\n") % (j.id,j.pkt))

                f2.close()
                print "koncze gre"
                break
        else:
            if c=='n':
                print "nie podjeto proby zgadniecia hasla"
            else:
                print "...uznam to za nie"

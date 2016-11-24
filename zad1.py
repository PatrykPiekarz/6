#tabliczka mnozenia d pliku
f1=open("plik1.txt","wb")
for x in range (1,11):
    f1.write("%3i" % (x),)
    for y in range (2,11):
        f1.write( "%3i" % (x*y),)

    f1.write("\n")
print "\n"
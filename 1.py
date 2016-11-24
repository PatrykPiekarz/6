#pliki

#utworzenie i otwarcie do zapisu pliku "plik1.txt"
f1=open("plik1.txt","wb")

#3 podstawowe aktrybuty
#name nazwa pliku
print f1.name

#mode okresla tryb otwarcia pliku
print f1.mode

#ckised okresla czy zamnkiety
print f1.closed

#metody do osblugi pliku
#write zapisuje do pliku napis
f1.write("Pierwszy plik")

#flush zapisuje dane do bufora pliku
#przydaje sie w windowsie
f1.flush()

#\n nowa linia pliku
f1.write("\nnowa linia")

#close zapisuje dane z bufora do pliku i zamyka go
f1.close()

#otwarcie do modyfikacji
f1=open("plik1.txt","r+b")

#read odczytuje z pliku napis
print f1.read()

#tell podaje aktualna pozycje pliku
print f1.tell()

#seek ustawia pozycje w pliku na podana
f1.seek(0)

#nadpisanie zawartosci pliku
f1.write("Nowy poczatek")

#przesuniecie na wzgledna pozycje pliku od aktualnej
f1.seek(14,1)

#przesuniecie fragmentu zawartosci pliku o okreslonej dlugosci
print f1.read(14)

#writelines zaousyhe do pliku sekwencje napisow
#bez dodwania automatycznie separatorow
f1.writelines(["\n3 linia","\n4 linia,\n5 linia"])

#readlines wczytuje sekwencje napisow
f1.seek(0)
print f1.readlines()

#trunctate skraca do podanej pozycji
f1.truncate(30)
f1.seek(0)
print f1.read()

#iosatty true jesli plik jest dolaczony do urzadzenia terminalowego
print f1.isatty()

#przyklad strumienie sys stdout i sys stdin
import sys
print sys.stdout.isatty()

#przyklad przekierowania wewnatrz programu
import sys
ekran = sys.stdout
sys.stdout = open("wyjscie.txt","w")
print "jestem tutaj"
print "gdzie ty poszedles?"
sys.stdout = ekran
print open("wyjscie.txt.","r").read()
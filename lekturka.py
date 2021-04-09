opisyslownik = str(input("Podaj nazwe plkiu z słowniczka: "))
f = open("input.txt",'r', encoding='utf-8')
cytaty = open("cytaty.txt",'w', encoding='utf-8')
a = f.read()
a = a.lower()
b = a.split('.')
c = len(b)
print("Liczba zdań, które zostały wykryte: " +str(c))
szukano = open("slowniczek/"+opisyslownik,'r', encoding='utf-8')
def szukanko(szukano):
    znalezionecytaty = 0
    print("dla "+szukano)
    for kwk in range(c):
        y = b[kwk].split(' ')
        for i in y:
            slowa = i.rstrip(',')
            slowa = slowa.rstrip(';')
            slowa = slowa.rstrip('?')
            slowa = slowa.rstrip('!')
            slowa = slowa.rstrip(':')
            slowa = slowa.rstrip('"')
            slowa = slowa.lstrip('„')
            if slowa == szukano:
                kwkk = kwk
                print("^><><><><><><><><><><><><><><><><><><><><><><><><><><><><^")
                print("---------------------------------------------------------")
                print("Znaleziono "+'<'+slowa+'>'+' '+"w zdaniu"+' '+str(kwkk+1))
                print("Cytat:"+b[kwkk-2]+b[kwkk-1]+b[kwkk]+b[kwkk+1]+b[kwkk+2])
                znalezionecytaty = znalezionecytaty +1
                print("---------------------------------------------------------")
                print("^><><><><><><><><><><><><><><><><><><><><><><><><><><><><^")
                cytaty.write("^><><><><><><><><><><><><><><><><><><><><><><><><><><><><^\n")
                cytaty.write("---------------------------------------------------------\n")
                cytaty.write("dla "+szukano+'\n')
                cytaty.write("Znaleziono "+'<'+slowa+'>'+' '+"w zdaniu"+' '+str(kwkk+1)+"\n")
                cytaty.write("Cytat:"+b[kwkk-2]+b[kwkk-1]+b[kwkk]+b[kwkk+1]+b[kwkk+2]+"\n")
                cytaty.write("---------------------------------------------------------\n")
                cytaty.write("^><><><><><><><><><><><><><><><><><><><><><><><><><><><><^\n")
    print("Znaleziono cytatów: "+str(znalezionecytaty))
                
slowniczek = szukano.readlines()
slownictwo = []
for slowo in slowniczek:
    slownictwo = slownictwo + [slowo]
for kaka in range(len(slownictwo)):
    slownictwo[kaka]=slownictwo[kaka].replace('\n',"")
    aka = szukanko(slownictwo[kaka])




f.close()
cytaty.close()
szukano.close()

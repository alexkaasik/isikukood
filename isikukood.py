k=0

while 1:
    k+=1
    print(k)
    ik=""
    while len(ik)!=11:
        try:
            ik=input("put iskukood: ")
        except:
            ValueError
    print("11 symbols")
    print("Try again")
    ik1=int(ik[0])
    if 1<=ik1<=9:
        if ik1%2==0:
            gender="Female"
        else:
            gender="Male"
        print("Your gender:")
        print(gender)
        ik12=int(ik[1]+ik[2]) #year
        ik34=int(ik[3]+ik[4]) #month
        ik56=int(ik[5]+ik[6]) #day
        if 0<=ik12<=99 and 1<=ik34<=12 and 1<=ik56<=31:
            print("Date of birth:")
            data=str(ik56)+"."+str(ik34)+"."+str(ik12)
            print(data)
            print("Isikukoodi:")
            control=[-1]
            n=1
            summa=0
            ikk=str(int(ik)//10)
            print(ikk)
            for i in ikk:
                if n==10: n=1
                summa+=int(i)*n
                n+=1
            print(summa)
            kontroll=summa-(summa//11)*11


            if 1<=summa<=10:
                test="Kuressaare Haigla"
            elif 11<=summa<=19:
                text="Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
            elif 20<=summa<=220:
                text="Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
            elif 221<=summa<=270:
                text="Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi"
            elif 271<=summa<=370:
                text="Maarjamõisa Kliinikum (Tartu), Jõgeva Haigl"
            elif 371<=summa<=420:
                text="Narva Haigla"
            elif 421<=summa<=470:
                text="Pärnu Haigla"
            elif 471<=summa<=490:
                text="Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla"
            elif 491<=summa<=520:
                text="Järvamaa Haigla (Paide)"
            elif 521<=summa<=570:
                text="Rakvere, Tapa haigla"
            elif 571<=summa<=600:
                text="Valga Haigla"
            elif 601<=summa<=650:
                tezt="Viljandi Haigla"
            else:
                text="Lõuna-Eesti Haigla (Võru), Põlva Haigla"
                
            print(f"Your hospital name {text}")

            print("Your last digit:")
            print(kontroll)

            print("Done")
           
    else:
        arvud.append(ik)
    if k==3: break
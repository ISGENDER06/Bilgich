bir="""     

                     1  3  5  7  9 11 13 15
                    17 19 21 23 25 27 29 31
                    33 35 37 39 41 43 45 47
                    49 51 53 55 57 59 61 63
"""
iki="""     

                     2  3  6  7 10 11 14 15
                    18 19 22 23 26 27 30 31
                    34 35 38 39 42 43 46 47
                    50 51 54 55 58 59 62 63
"""
dort="""    

                     4  5  6  7 12 13 14 15
                    20 21 22 23 28 29 30 31
                    36 37 38 39 44 45 46 47
                    52 53 54 55 60 61 62 63
"""
sekiz="""   

                     8  9 10 11 12 13 14 15
                    24 25 26 27 28 29 30 31
                    40 41 42 43 44 45 46 47
                    56 57 58 59 60 61 62 63
"""
onalty="""  

                    16 17 18 19 20 21 22 23
                    24 25 26 27 28 29 30 31
                    48 49 50 51 52 53 54 55
                    56 57 58 59 60 61 62 63
"""
otuziki=""" 

                    32 33 34 35 36 37 38 39
                    40 41 42 43 44 45 46 47
                    48 49 50 51 52 53 54 55
                    56 57 58 59 60 61 62 63
"""
a="bar"
b="yok"
while True:
    jemi=0
    jogap=input("""
                
                    Yadynda bir san tutyan menem 6 sorag berip biljek bolyan.
                    Jogap Bereninde 'bar' bilen 'yok' jogabyny dogry yaz.
                    Soralan soraga dogry jogap bermesen yalnyş çykarar.

                    Yadynda 1-dan başlap 64-e çenli bir san tut. (0<sanyn<64)

                    Tutdynmy:""").lower()
    if jogap=="howa" or jogap=="hawa" or jogap=="howwa":
        while True:
            print(bir)
            jogap1=input("""
                        
                    Yat tutan sanyn yokardaky sanlaryn ichinde barmy:""")
            if jogap1==a:
                jemi+=1
                next
            elif jogap1==b:
                next
            else:
                print("Dogry yaz!")
                continue
            while True:
                print(iki)
                jogap2=input("""
                        
                    Yat tutan sanyn yokardaky sanlaryn ichinde barmy:""")
                if jogap2==a:
                    jemi+=2
                    next
                elif jogap2==b:
                    next
                else:
                    print("Dogry yaz!")
                    continue
                while True:
                    print(dort)
                    jogap3=input("""
                                
                    Yat tutan sanyn yokardaky sanlaryn ichinde barmy:""")
                    if jogap3==a:
                        jemi+=4
                        next
                    elif jogap3==b:
                        next
                    else:
                        print("Dogry yaz!")
                        continue
                    while True:
                        print(sekiz)
                        jogap4=input("""
                                    
                    Yat tutan sanyn yokardaky sanlaryn ichinde barmy:""")
                        if jogap4==a:
                            jemi+=8
                            next
                        elif jogap4==b:
                            next
                        else:
                            print("Dogry yaz!")
                            continue
                        while True:
                            print(onalty)
                            jogap5=input("""
                                        
                    Yat tutan sanyn yokardaky sanlaryn ichinde barmy:""")
                            if jogap5==a:
                                jemi+=16
                                next
                            elif jogap5==b:
                                next
                            else:
                                print("Dogry yaz!")
                                continue
                            while True:
                                print(otuziki)
                                jogap6=input("""
                                            
                    Yat tutan sanyn yokardaky sanlaryn ichinde barmy:""")
                                if jogap6==a:
                                    jemi+=32
                                    next
                                elif jogap6==b:
                                    next
                                else:
                                    print("Dogry yaz!")
                                    continue
                                break
                            break
                        break
                    break
                break
            break
        print(f"""         
                      --------------------------------
                      --  Senin Yat Tutan Sanyn:{jemi}
                      --------------------------------
                      
                      
                      
                      
                      
                      
                      
                      """)
        input()
    elif jogap==b:
        print("Sagbol Onda!")
        input()
        break
    else:
        print("Dogry Yaz!")
        continue




































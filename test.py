from gpiozero import Button
from signal import pause
from datetime import datetime
from time import sleep, time
import tkinter as tk
from tkinter import ttk
import cups
from fpdf import FPDF
import shutil
from PIL import Image, ImageTk
from tkcalendar import *
import sys
import smbus
import os

#from tkinter import *


###BASINC ADRESİ###
address = 0x09
##########
button = Button( 23,pull_up = False,bounce_time= None)
refbutton = Button( 24,pull_up = False,bounce_time= None) 

######Yüzdelik Hata Payi########
yuzdelik1 = 0
yuzdelik2 = 0
yuzdelik3 = 0
yuzdelik4 = 0
yuzdelik5 = 0
####Süre Farkları####
reftestfark1 = 0
reftestfark2 = 0
reftestfark3 = 0
reftestfark4 = 0
reftestfark5 = 0
####Standartlar######
threshold=.4;
pressedTime=0;
releasedTime=0;
diffTime = 0;
i = 0;
refi = 0;
refpressedTime=0;
refreleasedTime=0;
refdiffTime = 0;
########Listeler#######
pulsetimelist = []
difftimelist = []
listei = []
datesystem = []
serinoliste = []
refpulsetimelist=[]
refdifftimelist=[]
reflistei=[]
refdatesystem=[]
tarihliste=[]
saatliste=[]
basinclist=[]
pulsebasinc=[]
cihazsicaklikdegerleri= []
basincsicaklikdegerleri = []
acikhavabasinci= []
####Pulse Süreleri####
fark1b = 0
fark2b = 0
fark3b = 0
fark4b = 0
fark5b = 0
reffark1b = 0
reffark2b = 0
reffark3b = 0
reffark4b = 0
reffark5b = 0
ortalamayuzdelik = 0
ortalamapulse= 0
ortalamarefpulse= 0 
ortalamahiz = 0
ortalamarefhiz= 0
ortalamahizfark = 0
pressuresonuc= 0
saatbilgisi = 0
tarihbilgisi = 0
expression = ""
pressure2= 0
pressuresonuc2 = 0
cihazsicaklik = 0
tempDataRaw = 0
basincsicaklik = 0
hatadegeri= 0
gercekbasinc= 0

def main():
    global datesystem
    sistemtarihial=datetime.now()
    datesystem+=[sistemtarihial]
    global serinoliste
    global serino
    print("Uygulama işleme başladı")
    bas=tk.Tk()
    bas.title("SAYEKS")
    bas.geometry('500x500')
    bas.config(bg='#dadadb')
    bas.minsize(800,480)
    bas.maxsize(800,480)


    logo = ImageTk.PhotoImage(Image.open('/home/pi/vhs.png'))
    logo1=tk.Label(bas, text='Logo', image=logo)
    logo1.place(x=1,y=1)
    
    
    #serinogir.config(width=200)
    serinogir=tk.Label(bas, text='!Gaz bağlantılarını yapmayınız, \n !Giriş ve çıkış hortumunu bağlayınız, \n !Vanaları açınız, \n 1)Sayaç Seri No Giriniz ',fg='black', bg='#dadadb')
    serinogir.config(font=("Courier", 12))
    serinogir.place(x=120,y=110)
    
   
    

    def adim1():
        global serinoliste
        global serinumarasi
        global anlikveri
        global tarih
        global pressuresonuc
        global acikhavabasinci
        global address
        global cihazsicaklikdegerleri
        global cihazsicaklik
        serinumarasi=serino.get()
        

        

        if len(serino.get()) == 0:
            
            anlikveri=tk.Label(bas, text='Sayaç Seri No Giriniz!                             ',fg='red', bg='#dadadb')
            anlikveri.config(font=("Courier", 12))
            anlikveri.place(x=320,y=390)
        else:
            
            serinoliste+=[serinumarasi]
            ##GİZLEME##
            serinogir.place_forget()
            serino.place_forget()
            onay1.place_forget()
            
            button1.place_forget()
            button2.place_forget()
            button3.place_forget()
            button4.place_forget()
            button5.place_forget()
            button6.place_forget()
            button7.place_forget()
            button8.place_forget()
            button9.place_forget()
            button0.place_forget()
            clear.place_forget()
            Decimal.place_forget()
            ##BURAYA GEL
            
            
                
            
           
            anlikveri=tk.Label(bas, text='Sayaç Seri No:'+str(serinumarasi)+'          ',fg='green', bg='#dadadb')
            anlikveri.config(font=("Courier", 12))
            anlikveri.place(x=320,y=390)

            tarih=tk.Label(bas, text='!!!Giriş gaz bağlantısını yapınız çıkış vanası kapalı olmalı!!!\n\n2)Sistem Tarihi yanlışsa "Tarih Gir" \n butonuna basınız. Doğru ise onaylayınız.',fg='black', bg='#dadadb')
            tarih.config(font=("Courier", 12))
            tarih.place(x=140,y=150)

            def tarihisteme():
            
                global tarihgir
                global cal
                global tarih
                global expression
                expression = ""

                onay2.place_forget()
                tarihbuton.place_forget()
                tarih.place_forget()

                cal = Calendar(bas, selectmode="day", year=2022, month=1, day=13)
                cal.place(x=150, y=50, height=200, width=300)

                saatgir=tk.Label(bas, text='Saat Bilgisini Giriniz(Saat:Dakika)',fg='black', bg='#dadadb')
                saatgir.config(font=("Courier", 12))
                saatgir.place(x=150, y=260)
                #tarihgir=tk.Entry(width=20)
                #tarihgir.place(x=150,y=220)

                def pressb(num):

                    # point out the global expression variable
                    
                    global expression

                    # concatenation of string
                    expression = expression + str(num)

                    # update the expression by using set method
                    equation2.set(expression)
                    
                    
                    
                    #Decimal.place(x=-locx,y=-locy)

                def clearb():
                    global expression
                    expression = ""
                    equation2.set("")
                equation2 = tk.StringVar()
                tarihgir = tk.Entry(bas, textvariable=equation2)
                tarihgir.place(x=150,y=280, height=30, width=200) 


                button1b = tk.Button(bas, text=' 1 ', fg='black', bg='#299584',command=lambda: pressb(1), height=3, width=5)
                button1b.place(x=550, y=40)

                button2b = tk.Button(bas, text=' 2 ', fg='black', bg='#299584',command=lambda: pressb(2), height=3, width=5)
                button2b.place(x=620, y=40)

                button3b = tk.Button(bas, text=' 3 ', fg='black', bg='#299584',command=lambda: pressb(3), height=3, width=5)
                button3b.place(x=690, y=40)

                button4b = tk.Button(bas, text=' 4 ', fg='black', bg='#299584',command=lambda: pressb(4), height=3, width=5)
                button4b.place(x=550, y=110)

                button5b = tk.Button(bas, text=' 5 ', fg='black', bg='#299584',command=lambda: pressb(5), height=3, width=5)
                button5b.place(x=620, y=110)

                button6b = tk.Button(bas, text=' 6 ', fg='black', bg='#299584',command=lambda: pressb(6), height=3, width=5)
                button6b.place(x=690, y=110)
                
                button7b = tk.Button(bas, text=' 7 ', fg='black', bg='#299584',command=lambda: pressb(7), height=3, width=5)
                button7b.place(x=550, y=180)

                button8b = tk.Button(bas, text=' 8 ', fg='black', bg='#299584',command=lambda: pressb(8), height=3, width=5)
                button8b.place(x=620, y=180)

                button9b = tk.Button(bas, text=' 9 ', fg='black', bg='#299584',command=lambda: pressb(9), height=3, width=5)
                button9b.place(x=690, y=180)

                button0b = tk.Button(bas, text=' 0 ', fg='black', bg='#299584',command=lambda: pressb(0), height=3, width=5)
                button0b.place(x=620, y=250)

                clearb = tk.Button(bas, text='Clear', fg='black', bg='#299584',command=clearb, height=3, width=5)
                clearb.place(x=690, y=250)

                Decimalb= tk.Button(bas, text=':', fg='black', bg='#299584',command=lambda: pressb(':'), height=3, width=5)
                Decimalb.place(x=550, y=250)

                
                
                def tarihalma():
                    global saatbilgisi
                    global tarihbilgisi
                    global tarihliste
                    global tarihgir
                    global cal
                    global saatliste
                    global anlikveri
                    global tarih
                    
                    

                    if len(tarihgir.get()) == 0:
                        anlikveri=tk.Label(bas, text='Saat Bilgisi Giriniz                     ',fg='red', bg='#dadadb')
                        anlikveri.config(font=("Courier", 12))
                        anlikveri.place(x=320,y=390)
                    else:
                        
                        ### Gizleme
                        anlikveri.place_forget()
                        tarihal.place_forget()
                        cal.place_forget()
                        saatgir.place_forget()
                        tarihgir.place_forget()
                        tarih.place_forget()

                        button1b.place_forget()
                        button2b.place_forget()
                        button3b.place_forget()
                        button4b.place_forget()
                        button5b.place_forget()
                        button6b.place_forget()
                        button7b.place_forget()
                        button8b.place_forget()
                        button9b.place_forget()
                        button0b.place_forget()
                        clearb.place_forget()
                        Decimalb.place_forget()

                        saatbilgisi=tarihgir.get()
                        saatliste+=[saatbilgisi]
                        tarihbilgisi=cal.get_date()
                        tarihliste+=[cal.get_date()]

                        

                        anlikveri=tk.Label(bas, text='Sistem Tarihi:'+str(tarihbilgisi)+ " " + str(saatbilgisi)+'    ',fg='green', bg='#dadadb')
                        anlikveri.config(font=("Courier", 12))
                        anlikveri.place(x=280,y=390)

                        print(str(saatbilgisi))
                        print(saatliste[0])
                        hatbasinc()
                        
                        
                    

                tarihal=tk.Button(bas, text='Onayla', fg='black', bg='#299584',height=1, width=6, command=tarihalma)
                tarihal.place(x=350,y=280,height=30, width=110)


            tarihbuton=tk.Button(bas, text='Tarih Gir', fg='black', bg='#299584',height=1, width=6, command=tarihisteme)
            tarihbuton.place(x=280,y=240,height=50, width=110)
            
            def hatbasinc():
            
                global anlikveri
                global cal
                global saatgir
                global tarihgir
                global tarih
                global datesystem
                
                
                #anlikveri=tk.Label(bas, text='   sadsdsa                               ',fg='green', bg='#dadadb')
                
                
                tarih.place_forget()
                onay2.place_forget()
                tarihbuton.place_forget()
                print("Hat basıncına geldi")



                basincgir=tk.Label(bas, text='3)ÇIKIŞ VANASINI KAPATIP "Basınç Testi"ne basınız.',fg='red', bg='#dadadb')
                basincgir.config(font=("Bold", 12))
                basincgir.place(x=200,y=180)


                def baslangic():
                    
                    global serinoliste
                    global tarihliste
                    global saatliste
                    global address
                    global basinclist
                    global pressure
                    global pressuresonuc
                    global serino
                    global cal
                    global tarihgir
                    global islembaslat
                    global kacaktestbutonu
                    ##Baslat butonunu kaybetme###
                    islembaslat.place_forget()
                    basincgir.place_forget()
                    #shutil.copy("/home/pi/PULSE.pdf", "/home/pi/Desktop/PULSE/")

                    def arayuz1():
                        
                        form=tk.Tk()
                        form.title("SAYAC EKSPERT")
                        form.geometry('500x500')
                        form.config(bg='#dadadb')
                        form.minsize(800,480)
                        form.maxsize(800,480)
                        #logovhs = ImageTk.PhotoImage(Image.open('vhs.png'))
                        bilgi=tk.Label(form, text='',fg='black', bg='#dadadb')
                        bilgi.config(font=("Courier", 10))
                        bilgi.place(x=300,y=300)

                        logtext=tk.Label(form, text='',fg='black', bg='#dadadb')
                        logtext.config(font=("Courier", 10))
                        logtext.place(x=200,y=300)

                        global fark1b
                        global fark2b
                        global fark3b
                        global fark4b
                        global fark5b
                        global reffark1b
                        global reffark2b
                        global reffark3b
                        global reffark4b
                        global reffark5b
                        global tarihliste
                        global saatliste
                    
                        label1=tk.Label(form, text='Logları USB Belleğe kopyalamadan önce \n USB Bellek takınızve gelen uyarıyı kapatabilirsiniz, \n sonrasında LOG Kopyala butonu ile Logları kaydedebilirsiniz.',fg='Green', font='bold')
                        label1.place(x=120,y=230)
                        def hesapla():
                            global fark1b
                            global fark2b
                            global fark3b
                            global fark4b
                            global fark5b
                            global reffark1b
                            global reffark2b
                            global reffark3b
                            global reffark4b
                            global reffark5b
                            global tarihliste 
                            global saatliste
                            global refdifftimelist
                            global refpulsetimelist
                            global refdatesystem
                            
                            global difftimelist
                            global pulsetimelist
                            global datesystem
                            global serinoliste
                            global yuzdelik1
                            global yuzdelik2
                            global yuzdelik3
                            global yuzdelik4
                            global yuzdelik5
                            global ortalamayuzdelik
                            global basinclist
                            global ortalamapulse
                            global ortalamarefpulse
                            global ortalamahiz
                            global ortalamarefhiz
                            global ortalamahizfark
                            global pulsebasinc
                            global releasedTime
                            global hatadegeri
                            global cihazsicaklikdegerleri
                            global basincsicaklikdegerleri
                            global acikhavabasinci
                            global gercekbasinc
                            

                            label1=tk.Label(form, text='Sayaç Seri No:'+serinumarasi,fg='green', bg='#dadadb')
                            label1.place(x=65,y=350)
                            label1=tk.Label(form, text='Uygulama Tarihi:'+str(tarihbilgisi)+ " " + str(saatbilgisi),fg='green', bg='#dadadb')
                            label1.place(x=65,y=370)
                            label1=tk.Label(form, text='Sistem Tarihi:'+str(datesystem[0])+ " ",fg='green', bg='#dadadb')
                            label1.place(x=65,y=390)
                            
                            #1. PULSE
                        
                            label1=tk.Label(form, text='1.Pulse(sn):',fg='black')
                            label1.place(x=65,y=50)
                            label1=tk.Label(form, text=str(fark1b),fg='black',bg='#dadadb')
                            label1.place(x=145,y=50)
                    
                    
                            #2. PULSE
                            
                            label1=tk.Label(form, text='2.Pulse(sn):',fg='black')
                            label1.place(x=65,y=80)
                            label1=tk.Label(form, text=str(fark2b),fg='black')
                            label1.place(x=145,y=80)
                            #3. PULSE
                        
                            label1=tk.Label(form, text='3.Pulse(sn):',fg='black')
                            label1.place(x=65,y=110)
                            label1=tk.Label(form, text=str(fark3b),fg='black',bg='#dadadb')
                            label1.place(x=145,y=110)
                            #4. PULSE
                        
                            label1=tk.Label(form, text='4.Pulse(sn):',fg='black')
                            label1.place(x=65,y=140)
                            label1=tk.Label(form, text=str(fark4b),fg='black',bg='#dadadb')
                            label1.place(x=145,y=140)
                            #5. PULSE
                        
                            label1=tk.Label(form, text='5.Pulse(sn):',fg='black')
                            label1.place(x=65,y=170)
                            label1=tk.Label(form, text=str(fark5b),fg='black',bg='#dadadb')
                            label1.place(x=145,y=170)


                            #Ortalama Pulse

                            label1=tk.Label(form, text='Ort. P. (sn):',fg='black')
                            label1.place(x=65,y=200)
                            label1=tk.Label(form, text=str(round(ortalamapulse, 3)),fg='black',bg='#dadadb')
                            label1.place(x=145,y=200)

                            #Referans 1. PULSE
                            
                            label1=tk.Label(form, text='R1.Pulse(sn):',fg='black')
                            label1.place(x=200,y=50)
                            label1=tk.Label(form, text=str(reffark1b),fg='black',bg='#dadadb')
                            label1.place(x=287,y=50)
                            #Referans 2. PULSE
                        
                            label1=tk.Label(form, text='R2.Pulse(sn):',fg='black')
                            label1.place(x=200,y=80)
                            label1=tk.Label(form, text=str(reffark2b),fg='black',bg='#dadadb')
                            label1.place(x=287,y=80)
                            #Referans 3. PULSE
                        
                            label1=tk.Label(form, text='R3.Pulse(sn):',fg='black')
                            label1.place(x=200,y=110)
                            label1=tk.Label(form, text=str(reffark3b),fg='black')
                            label1.place(x=287,y=110)
                            #Referans 4. PULSE
                            
                            label1=tk.Label(form, text='R4.Pulse(sn):',fg='black')
                            label1.place(x=200,y=140)
                            label1=tk.Label(form, text=str(reffark4b),fg='black',bg='#dadadb')
                            label1.place(x=287,y=140)
                            #Referans 5. PULSE
                            
                            label1=tk.Label(form, text='R5.Pulse(sn):',fg='black')
                            label1.place(x=200,y=170)
                            label1=tk.Label(form, text=str(reffark5b),fg='black',bg='#dadadb')
                            label1.place(x=287,y=170)

                            if ortalamayuzdelik>=(-hatadegeri) and ortalamayuzdelik<=hatadegeri:
                                label1=tk.Label(form, text='TESTTEN GEÇTİ',fg='Green', font='bold')
                                label1.place(x=320,y=350)
                            else:
                                
                                label1=tk.Label(form, text='TESTTEN KALDI',fg='Red', font='bold')
                                label1.place(x=320,y=350)


                            ### REFERANS SAYAÇ REFERANS DEĞERLERİ
                            if ortalamarefhiz <= 1800 and ortalamarefhiz >= 200:
                                label1=tk.Label(form, text='BAŞARILI TEST',fg='Green', font='bold')
                                label1.place(x=320,y=370)
                                
                            else:
                                label1=tk.Label(form, text='BAŞARISIZ TEST',fg='Red', font='bold')
                                label1.place(x=320,y=370)


                            #Ortalama Pulse

                            label1=tk.Label(form, text='Ort. R. (sn):',fg='black')
                            label1.place(x=200,y=200)
                            label1=tk.Label(form, text=str(round(ortalamarefpulse, 3)),fg='black',bg='#dadadb')
                            label1.place(x=287,y=200)

                            ###YÜZDELİK HATA####
                            label1=tk.Label(form, text='Q1 Hata (%):',fg='black')
                            label1.place(x=350,y=50)
                            label1=tk.Label(form, text=str(round(yuzdelik1, 3)),fg='black',bg='#dadadb')
                            label1.place(x=450,y=50)
                            #hata2
                        
                            label1=tk.Label(form, text='Q2 Hata (%):',fg='black')
                            label1.place(x=350,y=80)
                            label1=tk.Label(form, text=str(round(yuzdelik2, 3)),fg='black',bg='#dadadb')
                            label1.place(x=450,y=80)
                            #Hata3
                        
                            label1=tk.Label(form, text='Q3 Hata (%):',fg='black')
                            label1.place(x=350,y=110)
                            label1=tk.Label(form, text=str(round(yuzdelik3, 3)),fg='black')
                            label1.place(x=450,y=110)
                            #Hata4
                            
                            label1=tk.Label(form, text='Q4 Hata (%):',fg='black')
                            label1.place(x=350,y=140)
                            label1=tk.Label(form, text=str(round(yuzdelik4, 3)),fg='black',bg='#dadadb')
                            label1.place(x=450,y=140)
                            #Hata5
                            
                            label1=tk.Label(form, text='Q5 Hata (%):',fg='black')
                            label1.place(x=350,y=170)
                            label1=tk.Label(form, text=str(round(yuzdelik5, 3)),fg='black',bg='#dadadb')
                            label1.place(x=450,y=170)

                            #Ortalama Hata
                            
                            label1=tk.Label(form, text='Ort. Hata (%):',fg='black')
                            label1.place(x=350,y=200)
                            label1=tk.Label(form, text=str(round(ortalamayuzdelik, 3)),fg='black',bg='#dadadb')
                            label1.place(x=450,y=200)


                            ### 4. sekme


                            label1=tk.Label(form, text='Basınç (Bar):',fg='black')
                            label1.place(x=520,y=50)
                            label1=tk.Label(form, text=str(gercekbasinc),fg='black',bg='#dadadb')
                            label1.place(x=625,y=50)
                            ### 4. sekm  test ort hız


                            label1=tk.Label(form, text='Test Hız (L/h):',fg='black')
                            label1.place(x=520,y=80)
                            label1=tk.Label(form, text=str(round(ortalamahiz, 3)),fg='black',bg='#dadadb')
                            label1.place(x=625,y=80)
                            ### 4. sekm  ref ort hız


                            label1=tk.Label(form, text='Ref. Hız (L/h):',fg='black')
                            label1.place(x=520,y=110)
                            label1=tk.Label(form, text=str(round(ortalamarefhiz, 3)),fg='black',bg='#dadadb')
                            label1.place(x=625,y=110)
                            ### 4. sekm  Ort hız fark


                            label1=tk.Label(form, text='Hız Fark (L/h):',fg='black')
                            label1.place(x=520,y=140)
                            label1=tk.Label(form, text=str(round(ortalamahizfark, 3)),fg='black',bg='#dadadb')
                            label1.place(x=625,y=140)

                            ### Cihaz Sıcaklık Değerleri
                            label1=tk.Label(form, text='C.Sıcaklığı (C):',fg='black')
                            label1.place(x=520,y=170)
                            label1=tk.Label(form, text=str(round(cihazsicaklikdegerleri[0],3)),fg='black',bg='#dadadb')
                            label1.place(x=625,y=170)
                             ### Basınç Sıcaklık Değerleri
                            label1=tk.Label(form, text='G.Sıcaklığı (C):',fg='black')
                            label1.place(x=520,y=200)
                            label1=tk.Label(form, text=str(round(basincsicaklikdegerleri[0],3)),fg='black',bg='#dadadb')
                            label1.place(x=625,y=200)

                        #ARAYUZ SONUC BUTTON
                        buton=tk.Button(form, text='Sonuç', fg='black', bg='#299584', command=hesapla)
                        buton.place(x=130,y=1)
                        
                        def logcopy():
                            try:
                                logtext.config(text='', fg='red')
                                
                                shutil.copy("/home/pi/log.txt", "/media/pi/TAKTES")
                                bilgi.config(text='LOG Kopyalandı',fg='black')  
                            except:
                                bilgi.config(text='',fg='black')  

                                #bilgi.place_forget()
                                logtext.config(text='LOG Kopyalanamadı! \n USB Belleğin bağlantısını kontrol ediniz!', fg='red')
                                
                        
                        #ARAYUZ LOG BUTTON
                        export=tk.Button(form, text='Log Kopyala', fg='black', bg='#299584', command=logcopy)
                        export.place(x=310,y=1)


                        reset2=tk.Button(form,text='Yeni Test', fg='black',bg='#299584',command=yenidentest)
                        reset2.place(x=210,y=1)
                        def resettxt():
                            #label1=tk.Label(form, text='LOG temizlenmiştir.',fg='black', bg='red')
                            # label1.place(x=200,y=390)
                            bilgi.config(text='Log Temizlenmiştir!!', fg='red',bg='#dadadb')
                            f = open('log.txt','w')
                            f.write(str(datesystem[0])+"  tarihinde veriler temizlenmiştir.\n\n\n\n")
                            f.close()
                            shutil.copy("/home/pi/log.txt", "/home/pi/Desktop/")
                        #ARAYUZ RES BUTTON   
                        export=tk.Button(form, text='LOG Temizle', fg='red', bg='#299584', command=resettxt)
                        export.place(x=430,y=1)
                        #ARAYUZ PRİNT BUTTON
                        def printer():
                            #label1=tk.Label(form, text='Yazıcıya Gonderildi',fg='black', bg='yellow')
                            #label1.place(x=200,y=410)
                            bilgi.config(text='Yazıcıya Gönderildi',fg='black')
                            conn = cups.Connection()
                            printers = conn.getPrinters ()
                            prin = conn.getDefault()
                            myfile = "/home/pi/PULSE.pdf"
                            conn.printFile (prin, myfile, "Project Report", {"Page Left":"0","cpi":"15"})


                        ##PRİNTER BUTON
                        export=tk.Button(form, text='YAZDIR', fg='black', bg='#299584', command=printer)
                        export.place(x=550,y=1)
                
                        form.mainloop()
                        pause()
                    def yenidentest():
                        os.system('reboot')
                    def bitis():
                        global refdifftimelist
                        global refpulsetimelist
                        global refdatesystem
                        
                        global difftimelist
                        global pulsetimelist
                        global datesystem
                        global serinoliste
                        global fark1b
                        global fark2b
                        global fark3b
                        global fark4b
                        global fark5b
                        
                        global reffark1b
                        global reffark2b
                        global reffark3b
                        global reffark4b
                        global reffark5b
                        
                        global tarihliste
                        global saatliste
                        global fark1
                        global fark2
                        global fark3
                        global fark4
                        global fark5
                        global reffark1
                        global reffark2
                        global reffark3
                        global reffark4
                        global reffark5
                        global yuzdelik1
                        global yuzdelik2
                        global yuzdelik3
                        global yuzdelik4
                        global yuzdelik5
                        global ortalamayuzdelik
                        global basinclist
                        global ortalamapulse
                        global ortalamarefpulse
                        global ortalamahiz
                        global ortalamarefhiz
                        global ortalamahizfark
                        global pulsebasinc
                        global hatadegeri
                        global cihazsicaklik
                        global basincsicaklik
                        global cihazsicaklikdegerleri
                        global basincsicaklikdegerleri
                        global acikhavabasinci
                        global gercekbasinc
                        
                        gercekbasinc= round((basinclist[0]-acikhavabasinci[0]),4)
                        f = open('log.txt','a')
                        f.write("SAYEKS TEST SONUCLARI\n\n")
                        f = open('log.txt','a')
                        f.write("Sayaç Seri Numarası:"+str(serinoliste[0])+"\n\n\n")
                        f = open('log.txt','a')
                        
                        f.write("Sistem Tarih Bilgisi:"+str(datesystem[0])+"\n\n")
                    
                    
                    
                        f = open('log.txt','a')
                        f.write("Uygulama Tarihi:"+str(tarihliste[0])+"  "+ str(saatliste[0])+"\n\n")
                        
                        f = open('log.txt','a')
                        f.write("Basınç (Bar):"+str(gercekbasinc)+"\n\n")
                    
                    
                    
                        #PULSE FARKLARI TXT
                        f.write("Pulse Süreleri\n\n")
                        f = open('log.txt','a')
                        f.write("I1. Pulse Arası Süre (sn):  ")
                        f = open('log.txt','a')
                        f.write(str(fark1b)+" Hata Oranı %"+str(round(yuzdelik1, 3))+"\n")
                    
                        f.write("I2. Pulse Arası Süre (sn):  ")
                        f = open('log.txt','a')
                        f.write(str(fark2b)+" Hata Oranı %"+str(round(yuzdelik2, 3))+"\n")
                    
                        f.write("I3. Pulse Arası Süre (sn):  ")
                        f = open('log.txt','a')
                        f.write(str(fark3b)+" Hata Oranı %"+str(round(yuzdelik3, 3))+"\n")
                    
                        f.write("I4. Pulse Arası Süre (sn):  ")
                        f = open('log.txt','a')
                        f.write(str(fark4b)+" Hata Oranı %"+str(round(yuzdelik4, 3))+"\n")
                    
                        f.write("I5. Pulse Arası Süre (sn):  ")
                        f = open('log.txt','a')
                        f.write(str(fark5b)+" Hata Oranı %"+str(round(yuzdelik5,3))+"\n\n")


                        #REFERANS FARKLARI TEXT#
                        f.write("Referans Pulse Süreleri\n\n")
                        f = open('log.txt','a')
                        f.write("R1. Pulse Arası Süre (sn):  ")
                        f = open('log.txt','a')
                        f.write(str(reffark1b)+ " R1.Basınç(Bar):"+str(round(pulsebasinc[0],4))+"\n")
                    
                        f.write("R2. Pulse Arası Süre (sn):  ")
                        f = open('log.txt','a')
                        f.write(str(reffark2b)+ " R2.Basınç(Bar):"+str(round(pulsebasinc[1],4))+"\n")
                    
                        f.write("R3. Pulse Arası Süre (sn):  ")
                        f = open('log.txt','a')
                        f.write(str(reffark3b)+" R3.Basınç(Bar):"+str(round(pulsebasinc[2],4))+"\n")
                    
                        f.write("R4. Pulse Arası Süre (sn):  ")
                        f = open('log.txt','a')
                        f.write(str(reffark4b)+" R4.Basınç(Bar):"+str(round(pulsebasinc[3],4))+"\n")
                    
                        f.write("R5. Pulse Arası Süre (sn):  ")
                        f = open('log.txt','a')
                        f.write(str(reffark5b)+" R5.Basınç(Bar):"+str(round(pulsebasinc[4],4))+"\n\n")

                        ############# ORTALAMA DEĞERLER

                        f.write("Ortalama Test Pulse (sn):")
                        f = open('log.txt','a')
                        f.write(str(round(ortalamapulse, 3))+"\n")

                        f.write("Ortalama Ref Pulse (sn):  ")
                        f = open('log.txt','a')
                        f.write(str(round(ortalamarefpulse, 3))+"\n")
                        
                        f.write("Ortalama Hata Oranı(%):  ")
                        f = open('log.txt','a')
                        f.write(str(round(ortalamayuzdelik, 3))+"\n")
                        
                        f.write("Test Ort. Hız (L/h):  ")
                        f = open('log.txt','a')
                        f.write(str(round(ortalamahiz, 3))+"\n")

                        f.write("Ref Ort. Hız (L/h):  ")
                        f = open('log.txt','a')
                        f.write(str(round(ortalamarefhiz, 3))+"\n")

                        f.write("Ort. Hız Farkı (L/h):  ")
                        f = open('log.txt','a') 
                        f.write(str(round(ortalamahizfark,3))+"\n")

                        f.write("Cihaz Sıcaklığı (C):  ")
                        f = open('log.txt','a') 
                        f.write(str(round(cihazsicaklikdegerleri[0],2))+"\n")
                        
                        f.write("Ortam (Gaz) Sıcaklığı (C):  ")
                        f = open('log.txt','a') 
                        f.write(str(round(basincsicaklikdegerleri[0],2))+"\n\n\n")
                        
                        
                        
                        
                        


                        if ortalamayuzdelik>=(-hatadegeri) and ortalamayuzdelik<=hatadegeri:
                            f.write("TESTTEN GEÇTİ")
                            f = open('log.txt','a')
                            f.write("  % "+ str(round(ortalamayuzdelik, 3))+"\n\n\n")
                        else:
                            f.write("TESTTEN KALDI")
                            f = open('log.txt','a')
                            f.write("  % "+ str(round(ortalamayuzdelik, 3))+"\n\n\n")

                        ### REFERANS SAYAÇ REFERANS DEĞERLERİ
                        if ortalamarefhiz <= 1800 and ortalamarefhiz >= 200:
                            f.write("Başarılı Test (Referans Değer): ")
                            f = open('log.txt','a')
                            f.write("200 < "+ str(round(ortalamarefhiz, 3))+" L/h < 1800\n\n\n")
                        else:
                            f.write("Başarısız Test (Referans Değer): ")
                            f = open('log.txt','a')
                            f.write(str(round(ortalamarefhiz, 3))+" L/h \nReferans Aralığı(L/h): 200 < x < 1800\n\n\n")

                        f.close()
                        shutil.copy("/home/pi/log.txt", "/home/pi/Desktop/")
                        #TEST

                        pulsef1 =  pulsetimelist[1]-pulsetimelist[0]
                        
                        #test bitis

                        #PDF OLUSTURMA
                        pdf = FPDF()
                        pdf.add_page()
                        pdf.image('/home/pi/vhs.png',0,8,30)
                        pdf.set_xy(30,0)
                        pdf.set_font('Arial', 'B', 15)
                        pdf.cell(10, 40, 'SAYEKS')
                        
                        #PULSE TARİHLERİ
                        pdf.set_xy(0,10)
                        pdf.set_font('Times', 'B', 11)
                        pdf.cell(10, 50, 'UYGULAMA TARIHLERI')
                        ###SERİ NO###
                        pdf.set_xy(0,15)
                        pdf.set_font('Times', 'B', 10)
                        pdf.cell(10, 50, 'Sayac Seri No:')
                        pdf.set_xy(25,15)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str(serinoliste[0]))
                        
                        pdf.set_xy(0,20)
                        pdf.set_font('Times', 'B', 10)
                        pdf.cell(10, 50, 'Uygulama Tarihi:')

                        pdf.set_xy(30,20)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str(tarihliste[0])+"  "+ str(saatliste[0]))
                        
                        pdf.set_xy(0,25)
                        pdf.set_font('Times', 'B', 10)
                        pdf.cell(10, 50, 'Basinc (Bar):')

                        pdf.set_xy(30,25)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str(gercekbasinc))

                        pdf.set_xy(0,30)
                        pdf.set_font('Times', 'B', 10)
                        pdf.cell(10, 50, 'Sistem Tarihi:')

                        pdf.set_xy(30,30)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str(datesystem[0]))

                        pdf.set_xy(0,35)
                        pdf.set_font('Times', 'B', 10)
                        pdf.cell(10, 50, 'Cihaz Sicakligi (C):')

                        pdf.set_xy(30,35)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str(round(cihazsicaklikdegerleri[0],2)))

                        pdf.set_xy(0,40)
                        pdf.set_font('Times', 'B', 10)
                        pdf.cell(10, 50, 'O. (Gaz) Sicakligi (C):')

                        pdf.set_xy(35,40)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str(round(basincsicaklikdegerleri[0],2)))
                        
                    
                        #PULSE FARKLARI
                        pdf.set_xy(0,50)
                        pdf.set_font('Times', 'B', 11)
                        pdf.cell(10, 50, 'PULSE FARKLARI')
                        

                        #1-2 fark
                        pdf.set_xy(0,55)
                        pdf.set_font('Times', 'I', 10)
                        pdf.cell(10, 50, '1. Pulse Suresi(sn):')

                        pdf.set_xy(30,55)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str(fark1b))
                        
                        pdf.set_xy(43,55)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str("Hata %"))
                        
                        pdf.set_xy(55,55)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str(round(yuzdelik1, 3)))
                        #2-3 fark
                        pdf.set_xy(0,60)
                        pdf.set_font('Times', 'I', 10)
                        pdf.cell(10, 50, '2. Pulse Suresi (sn):')

                        pdf.set_xy(30,60)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str(fark2b))
                        
                        pdf.set_xy(43,60)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str("Hata %"))
                        
                        pdf.set_xy(55,60)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str(round(yuzdelik2, 3)))
                        #3-4 fark
                        pdf.set_xy(0,65)
                        pdf.set_font('Times', 'I', 10)
                        pdf.cell(10, 50, '3. Pulse Suresi (sn):')

                        pdf.set_xy(30,65)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str(fark3b))
                        
                        pdf.set_xy(43,65)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str("Hata %"))
                        
                        pdf.set_xy(55,65)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str(round(yuzdelik3, 3)))
                        #4-5 Fark
                        pdf.set_xy(0,70)
                        pdf.set_font('Times', 'I', 10)
                        pdf.cell(10, 50, '4. Pulse Suresi (sn):')

                        pdf.set_xy(30,70)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str(fark4b))

                        pdf.set_xy(43,70)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str("Hata %"))
                        
                        pdf.set_xy(55,70)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str(round(yuzdelik4, 3)))
                        #5-6 fark
                        pdf.set_xy(0,75)
                        pdf.set_font('Times', 'I', 10)
                        pdf.cell(10, 50, '5. Pulse Suresi (sn):')

                        pdf.set_xy(30,75)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str(fark5b))

                        pdf.set_xy(43,75)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str("Hata %"))
                        
                        pdf.set_xy(55,75)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str(round(yuzdelik5, 3)))
                        #Referans Fark 1-0
                        pdf.set_xy(0,80)
                        pdf.set_font('Times', 'I', 10)
                        pdf.cell(10, 50, 'R1. Pulse Suresi (sn):')

                        pdf.set_xy(32,80)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str(reffark1b))

                        pdf.set_xy(43,80)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str("P (Bar)"))
                        
                        pdf.set_xy(55,80)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str(round(pulsebasinc[0], 4)))
                        #Referans Fark 1-2
                        pdf.set_xy(0,85)
                        pdf.set_font('Times', 'I', 10)
                        pdf.cell(10, 50, 'R2. Pulse Suresi (sn):')

                        pdf.set_xy(32,85)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str(reffark2b))

                        pdf.set_xy(43,85)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str("P (Bar)"))
                        
                        pdf.set_xy(55,85)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str(round(pulsebasinc[1], 4)))
                        #Referans Fark 2-3
                        pdf.set_xy(0,90)
                        pdf.set_font('Times', 'I', 10)
                        pdf.cell(10, 50, 'R3. Pulse Suresi (sn):')

                        pdf.set_xy(32,90)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str(reffark3b))

                        pdf.set_xy(43,90)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str("P (Bar)"))
                        
                        pdf.set_xy(55,90)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str(round(pulsebasinc[2], 4)))
                        #Referans Fark 3-4
                        pdf.set_xy(0,95)
                        pdf.set_font('Times', 'I', 10)
                        pdf.cell(10, 50, 'R4. Pulse Suresi (sn):')

                        pdf.set_xy(32,95)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str(reffark4b))

                        pdf.set_xy(43,95)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str("P (Bar)"))
                        
                        pdf.set_xy(55,95)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str(round(pulsebasinc[3], 4)))
                        #Referans Fark 4-5
                        pdf.set_xy(0,100)
                        pdf.set_font('Times', 'I', 10)
                        pdf.cell(10, 50, 'R5. Pulse Suresi (sn):')

                        pdf.set_xy(32,100)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str(reffark5b))

                        pdf.set_xy(43,100)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str("P (Bar)"))
                        
                        pdf.set_xy(55,100)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str(round(pulsebasinc[4], 4)))

                        #########Ortalama Değerler###
                        pdf.set_xy(0,115)
                        pdf.set_font('Times', 'B', 11)
                        pdf.cell(10, 50, 'ORTALAMA DEGERLER')

                        #######ORTALAMA HIZ ##########
                        pdf.set_xy(0,120)
                        pdf.set_font('Times', 'I', 10)
                        pdf.cell(10, 50, 'Test Ort. Hiz (L/h):')

                        pdf.set_xy(32,120)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str(round(ortalamahiz, 3)))

                        pdf.set_xy(0,125)
                        pdf.set_font('Times', 'I', 10)
                        pdf.cell(10, 50, 'Ref Ort. Hiz (L/h):')

                        pdf.set_xy(32,125)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str(round(ortalamarefhiz, 3)))

                        ###### Ortalama Hız Farkı ##########

                        pdf.set_xy(0,130)
                        pdf.set_font('Times', 'I', 10)
                        pdf.cell(10, 50, 'Ort. Hiz Farki (L/h):')

                        pdf.set_xy(32,130)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str(round(ortalamahizfark, 3)))


                        pdf.set_xy(0,135)
                        pdf.set_font('Times', 'I', 10)
                        pdf.cell(10, 50, 'Ort. Pulse(sn):')

                        pdf.set_xy(32,135)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str(round(ortalamapulse, 3)))

                        pdf.set_xy(0,140)
                        pdf.set_font('Times', 'I', 10)
                        pdf.cell(10, 50, 'Ort. Ref Pulse(sn):')

                        pdf.set_xy(32,140)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str(round(ortalamarefpulse, 3)))



                        #######ORTALAMA HATA ##########
                        pdf.set_xy(0,145)
                        pdf.set_font('Times', 'I', 10)
                        pdf.cell(10, 50, 'Ort. Hata (%):')

                        pdf.set_xy(32,145)
                        pdf.set_font('Arial', '', 9)
                        pdf.cell(10, 50, str(round(ortalamayuzdelik, 3)))
                        
                        if ortalamayuzdelik>=(-hatadegeri) and ortalamayuzdelik<=(hatadegeri):
                            pdf.set_xy(15,160)
                            pdf.set_font('Times', 'B', 10)
                            pdf.cell(10, 50, 'TESTTEN GECTI')
                        else:
                            pdf.set_xy(15,160)
                            pdf.set_font('Times', 'B', 10)
                            pdf.cell(10, 50, 'TESTTEN KALDI')
                        
                        ### REFERANS SAYAÇ REFERANS DEĞERLERİ
                        
                        if ortalamarefhiz <= 1800 and ortalamarefhiz >= 200:
                            pdf.set_xy(0,170)
                            pdf.set_font('Times', 'B', 10)
                            pdf.cell(10, 50, 'Basarili Test (R.Deger): ')
                            pdf.set_xy(42,170)
                            pdf.set_font('Times', 'B', 10)
                            pdf.cell(10, 50, str(round(ortalamarefhiz, 3)) )
                            pdf.set_xy(0,175)
                            pdf.set_font('Times', 'I', 10)
                            pdf.cell(10, 50, 'Referans Araligi(L/h): 200 < x < 1800 ')
                        else:
                            pdf.set_xy(0,170)
                            pdf.set_font('Times', 'B', 10)
                            pdf.cell(10, 50, 'Basarisiz Test (R.Deger): ')
                            pdf.set_xy(42,170)
                            pdf.set_font('Times', 'B', 10)
                            pdf.cell(10, 50, str(round(ortalamarefhiz, 3)) )
                            pdf.set_xy(0,175)
                            pdf.set_font('Times', 'I', 10)
                            pdf.cell(10, 50, 'Referans Araligi(L/h): 200 < x < 1800 ')

                        pdf.output('PULSE.pdf', 'F')
                        print("Pulse Okuma Tamamlanmıştır")
                        shutil.copy("/home/pi/PULSE.pdf", "/home/pi/Desktop/")
                        page=tk.Button(bas, text='Sonuc', fg='black', bg='#299584', command=arayuz1)
                        page.place(x=300,y=170, width=80, height=40)

                        reset=tk.Button(bas,text='Yeni Test', fg='black',bg='#299584',command=yenidentest)
                        reset.place(x=400,y=170, width=80, height=40)
                        arayuz1()
                    
                    def litrehiz():
                        global refdifftimelist
                        global difftimelist
                        global fark1
                        global fark2
                        global fark3
                        global fark4
                        global fark5
                        global reffark1
                        global reffark2
                        global reffark3
                        global reffark4
                        global reffark5
                        global reftestfark1
                        global reftestfark2
                        global reftestfark3
                        global reftestfark4
                        global reftestfark5
                        global fark1b
                        global fark2b
                        global fark3b
                        global fark4b
                        global fark5b
                        global reffark1b
                        global reffark2b
                        global reffark3b
                        global reffark4b
                        global reffark5b
                        global yuzdelik1
                        global yuzdelik2
                        global yuzdelik3
                        global yuzdelik4
                        global yuzdelik5
                        global basinclist
                        global ortalamayuzdelik
                        global ortalamapulse
                        global ortalamarefpulse
                        global ortalamahiz
                        global ortalamarefhiz
                        global ortalamahizfark
                        global basincsicaklikdegerleri
                        global cihazsicaklikdegerleri
                        global hatadegeri
                        

                        ######Fark Hesaplamaları 4 basamak####
                        fark1=pulsetimelist[1]-pulsetimelist[0]
                        fark1b=round(fark1,3)
                        fark2=pulsetimelist[2]-pulsetimelist[1]
                        fark2b=round(fark2,3)
                        fark3=pulsetimelist[3]-pulsetimelist[2]
                        fark3b=round(fark3,3)
                        fark4=pulsetimelist[4]-pulsetimelist[3]
                        fark4b=round(fark4,3)
                        fark5=pulsetimelist[5]-pulsetimelist[4]
                        fark5b=round(fark5,3)
                        ######FARK REFERANS 4 Basamak#####
                        reffark1=refpulsetimelist[1]-refpulsetimelist[0]
                        reffark1b=round(reffark1,3)
                        reffark2=refpulsetimelist[2]-refpulsetimelist[1]
                        reffark2b=round(reffark2,3)
                        reffark3=refpulsetimelist[3]-refpulsetimelist[2]
                        reffark3b=round(reffark3,3)
                        reffark4=refpulsetimelist[4]-refpulsetimelist[3]
                        reffark4b=round(reffark4,3)
                        reffark5=refpulsetimelist[5]-refpulsetimelist[4]
                        reffark5b=round(reffark5,3)
                        #### hata farkı######
                        reftestfark1 = reffark1-fark1
                        reftestfark2 = reffark2-fark2
                        reftestfark3 = reffark3-fark3
                        reftestfark4 = reffark4-fark4
                        reftestfark5 = reffark5-fark5
                        ######Yüzdelik Hesap########
                        yuzdelik1 = 100*(reftestfark1/reffark1)
                        yuzdelik2 = 100*(reftestfark2/reffark2)
                        yuzdelik3 = 100*(reftestfark3/reffark3)
                        yuzdelik4 = 100*(reftestfark4/reffark4)
                        yuzdelik5 = 100*(reftestfark5/reffark5)

                        print("%"+str(yuzdelik1))
                        ortalamayuzdelik=(yuzdelik1+yuzdelik2+yuzdelik3+yuzdelik4+yuzdelik5)/5
                        print("Ortalama Yüzdelik : "+ str(ortalamayuzdelik))
                        
                        
                        ortalamapulse = (fark1+fark2+fark3+fark4+fark5)/5
                        ortalamarefpulse = (reffark1+reffark2+reffark3+reffark4+reffark5)/5

                        ####### Ortalamada saatlik hızı
                        ortalamahiz= (60*60*10)/(ortalamapulse)
                        ortalamarefhiz= (60*60*10)/(ortalamarefpulse)

                        ortalamahizfark= ortalamarefhiz-ortalamahiz
                        ###Sıcaklığa göre hata oranı çıkartma
                        if (cihazsicaklikdegerleri[0]-basincsicaklikdegerleri[0]) <=15 and (cihazsicaklikdegerleri[0]-basincsicaklikdegerleri[0])>=(-15):
                            hatadegeri=5

                        else:
                            hatadegeri=7
                        print("Hata Değeri:")
                        print(hatadegeri)
                        bitis()
                    #############TESTGPIO############
                        
                    def checkPressed():
                        global pressedTime
                        pressedTime = datetime.now()        
                        print(pressedTime, " pressed")
                        
                    def checkReleased():
                        global pressedTime
                        global releasedTime
                        releasedTime = datetime.now()
                        print(releasedTime, " released")
                
                        if pressedTime :
                            diffTime = releasedTime - pressedTime
                            
                            print("diffTime => ", diffTime.total_seconds())
                    
                            if diffTime.total_seconds() > threshold:
                                print(pressedTime," Pulse occured")
                                a = datetime.timestamp(pressedTime)
                                
                                global pulsetimelist
                                global difftimelist
                                global listei
                                global datesystem
                                global i
                        
                                pulsetimelist+=[a]
                                difftimelist+=[diffTime.total_seconds()]
                                listei+=[i]        
                                datesystem+=[pressedTime]
                                i=i+1
                                
                                anlikveri.config(text="Durum:"+str(i)+". Pulse Okundu",fg='Black', bg='#dadadb',font=("Courier", 14))
                                anlikveri.place(x=280, y=230)
                                if i>=6 and refi>=6:
                                    print(pulsetimelist[5])
                                    litrehiz()
                                        
                            
                            else:
                        
                                print("noise")
                                
                                anlikveri.config(text='Durum: Noise               ',fg='Black', bg='#dadadb',font=("Courier", 14))
                                anlikveri.place(x=300, y=230)
                    
                    
                        ####Seri no import####
                    ###########REFGPIO###############

                    def refPressed():
                        global refpressedTime
                        refpressedTime = datetime.now()        
                        print(refpressedTime, " pressed")

                        

                    def refReleased():
                        global refpressedTime
                        global refreleasedTime
                        
                        refreleasedTime = datetime.now()
                        print(refreleasedTime, " released")
                
                        if refpressedTime :
                            refdiffTime = refreleasedTime - refpressedTime
                    
                            print("diffTime => ", refdiffTime.total_seconds())
                    
                            if refdiffTime.total_seconds() > threshold:
                                print(refpressedTime," Pulse occured")
                                refa = datetime.timestamp(refpressedTime)
                        
                                global refpulsetimelist
                                global refdifftimelist
                                global reflistei
                                global refdatesystem
                                global refi
                                global pulsebasinc
                                global pressure
                                global pressuresonuc
                                global basincsicaklik
                                global basincsicaklikdegerleri

                                ###HESAPLAMALAR##
                                refpulsetimelist+=[refa]
                                refdifftimelist+=[refdiffTime.total_seconds()]
                                reflistei+=[refi]        
                                refdatesystem+=[refpressedTime]
                                refi=refi+1
                                ####
                                try:  ##BASINÇ DEĞERİ HATA VERMESİN DİYE OKUYAMAZSA 0 DEĞERİ VERİYOR

                                    ##BASINÇ HESABI##
                                    bus = smbus.SMBus(1)

                                    pressure=bus.read_i2c_block_data(address, 0xAA, 7)
                                    pressuresonuc=((pressure[3] | (pressure[1] <<16) | (pressure[2]<<8))-3260274.9)/5050000
                                    sleep(1)
                                    pressure=bus.read_i2c_block_data(address, 0xAA, 7)
                                    pressuresonuc=((pressure[3] | (pressure[1] <<16) | (pressure[2]<<8))-3260274.9)/5050000
                                    ##Basınç Sıcaklığı
                                    basincsicaklik= (((pressure[4] <<16) | (pressure[5]<<8) | pressure[6])-4603703)/116593
                                    print(pressuresonuc)
                                    print(basincsicaklik)

                                    basincsicaklikdegerleri+=[basincsicaklik]
                                    pulsebasinc+=[pressuresonuc]
                                    print(pulsebasinc[0]) 

                                    anlikveri.config(text="Durum:"+str(refi)+". Referans Pulse Okundu",fg='black', bg='#dadadb',font=("Courier", 14))
                                    anlikveri.place(x=280,  y=230)
                                    if refi>=6 and i>=6:
                                        print(refpulsetimelist[5])
                                        litrehiz()

                                except:
                                    pulsebasinc+=[0]
                                    basincsicaklikdegerleri+=[0]
                                    anlikveri.config(text="Durum:"+str(refi)+". Referans Pulse Okundu",fg='black', bg='#dadadb',font=("Courier", 14))
                                    anlikveri.place(x=280,  y=230)
                                    if refi>=6 and i>=6:
                                        print(refpulsetimelist[5])
                                        litrehiz()
                                            
                            
                            else:
                        
                                print("noise")
                                
                                anlikveri.config(text='Durum: Noise               ',fg='Black', bg='#dadadb',font=("Courier", 14))
                                anlikveri.place(x=300, y=230)
                    #####################################
                    
                    
                
                    
                    label2=tk.Label(bas, text='Islem Başlamıştır Lütfen Bitene Kadar Bekleyiniz',fg='black', bg='#299584')
                    label2.config(font=("Courier", 12))
                    label2.place(x=200,y=390)
                    
                    #basincgir.config(fg='green', bg='#dadadb')
                    ####
                    ####### İnterup olarak okuduğumuz için released ve pressed değişti
                    button.when_pressed = checkReleased 
                    button.when_released = checkPressed
                    refbutton.when_pressed = refReleased
                    refbutton.when_released = refPressed
                    print(serinoliste[0])
                    try:
                        shutil.copy("/home/pi/PULSE.pdf", "/home/pi/Desktop/")
                    except:
                        print("yedek kopyalanamadı")
                def kacaktestiyap():
                    global basinclist
                    global address
                    global pressure
                    global pressuresonuc
                    global anlikveri
                    global islembaslat
                    global kacaktestbutonu
                    global pressuresonuc2
                    global pressure2
                    
                    

                    anlikveri.place_forget()
                    #####BASINC HESAPLAMA####
                    bus = smbus.SMBus(1)
                    
                    sleep(10)
                   
                    try:

                        pressure=bus.read_i2c_block_data(address, 0xAA, 7)
                        pressuresonuc=((pressure[3] | (pressure[1] <<16) | (pressure[2]<<8))-3260274.9)/5050000
                        sleep(1)
                        pressure=bus.read_i2c_block_data(address, 0xAA, 7)
                        pressuresonuc=((pressure[3] | (pressure[1] <<16) | (pressure[2]<<8))-3260274.9)/5050000
                        print(pressuresonuc)
                        if pressuresonuc<(0.8):
                                print("Basınç Yanlış")
                                kacaktestiyap()
                        else:
                            print("İkinci Basınç Okundu")
                            basinclist+=[pressuresonuc]
                           

                            
                            
                            anlikveri=tk.Label(bas, text='İkinci basınç okundu (Bar): '+str(round(basinclist[1], 4))+"   ",fg='green', bg='#dadadb')
                            anlikveri.config(font=("Courier", 12))
                            anlikveri.place(x=280,y=390)


                            if basinclist[0]-basinclist[1] < 0.01 and basinclist[0]-basinclist[1] > -(0.01):
                                basincgir.config(text="KAÇAK YOK \n !!!GİRİŞ VE ÇIKIŞ VANALARINI AÇIN, GAZI İMHA EDİN!!! \n Pulse Modülünü Bağlayın ve Testi Başlatınız", fg='green', bg='#dadadb')
                                basincgir.place(x=170,y=150)
                                ###buton gizleme
                                kacaktestbutonu.place_forget()
                                ###########
                                islembaslat=tk.Button(bas, text='Testi Baslat', fg='black', bg='#299584', command=baslangic)
                                islembaslat.place(x=320,y=220, width=130, height=50)
                            else:
                                basincgir.config(text="KAÇAK ALGILANDI! \n TAKTES Servisinizle Görüşün veya Tekrar Test Ediniz\n"+ "Basınç Farkı:"+str(round((basinclist[0]-basinclist[1]), 5))+" Bar", fg='red', bg='#dadadb')
                                basincgir.place(x=170,y=180)
                                kacaktestbutonu.place_forget()

                                def servis():
                                    print("Yeniden Başlatılacak")
                                    os.system('reboot')

                                reset2=tk.Button(bas,text='Yeni Test', fg='black',bg='#299584',command=servis)
                                reset2.place(x=320,y=240, width=130, height=40)




                            
                    except:
            
                        anlikveri=tk.Label(bas, text='İkinci basınç değeri okunamadı tekrar deneyiniz.',fg='red', bg='#dadadb')
                        anlikveri.config(font=("Courier", 12))
                        anlikveri.place(x=180,y=390)

                def basinchesaplama():

                    global basinclist
                    global address
                    global pressure
                    global pressuresonuc
                    global anlikveri
                    global islembaslat
                    global kacaktestbutonu
                    global cihazsicaklik
                    global tempDataRaw
                    global cihazsicaklikdegerleri

                    
                    anlikveri.place_forget()
                    #####BASINC HESAPLAMA####
                    bus = smbus.SMBus(1)
                    try:
                        ##Sıcaklık değeri
                        #cihazsicaklik=bus.read_i2c_block_data(0x49, 0x00, 2)
                        #sleep(1)

                        pressure=bus.read_i2c_block_data(address, 0xAA, 7)
                        pressuresonuc=((pressure[3] | (pressure[1] <<16) | (pressure[2]<<8))-3260274.9)/5050000
                        
                        sleep(1)

                        #cihazsicaklik=bus.read_i2c_block_data(0x49, 0x00, 2)
                        #sleep(1)
                        
                        pressure=bus.read_i2c_block_data(address, 0xAA, 7)
                        pressuresonuc=((pressure[3] | (pressure[1] <<16) | (pressure[2]<<8))-3260274.9)/5050000
                        

                        print(pressuresonuc)
                        if pressuresonuc<(0.8):
                                print("Basınç Yanlış")
                                basinchesaplama()
                        else:
                            print("Basınç Okundu")
                            basinclist+=[pressuresonuc]
                            basincgir.config(text='4)Giriş Vanasını da KAPATIP "Kaçak Testi"ne tıklayın ve 10 saniye bekleyiniz..', fg='red', bg='#dadadb')
                            basincgir.config(font=("Bold", 12))
                            basincgir.place(x=120,y=180)
                            
                            #tempDataRaw = int.from_bytes(cihazsicaklik, 'big')
                            #if tempDataRaw >= 0x8000:
                                #tempDataRaw=(-256.0) + (tempDataRaw - 0x8000) * 7.8125e-3 # One LSB equals 7.812 mdegC
                            #else:
                                #tempDataRaw=tempDataRaw * 7.8125e-3 # One LSB equals 7.812 mdegC

                            #print(tempDataRaw)
                            
                            



                            
                            
                            anlikveri=tk.Label(bas, text='İlk basınç okundu(Bar): '+str(round(basinclist[0],4))+", Cihaz Sıcaklık(C): "+str(round(cihazsicaklikdegerleri[0], 2)),fg='green', bg='#dadadb')
                            anlikveri.config(font=("Courier", 12))
                            anlikveri.place(x=170,y=390)
                            
                            ###buton gizleme
                            ac.place_forget()
                            ###########


                            
                            kacaktestbutonu=tk.Button(bas, text='Kaçak Testi', fg='black', bg='#299584', command=kacaktestiyap)
                            kacaktestbutonu.place(x=320,y=210, height=40, width=110)
                    except:
            
                        anlikveri=tk.Label(bas, text='Birinci basınç değeri okunamadı!',fg='red', bg='#dadadb')
                        anlikveri.config(font=("Courier", 12))
                        anlikveri.place(x=220,y=390)
                

                ac=tk.Button(bas, text='Basınç Testi', fg='black', bg='#299584', command=basinchesaplama)
                ac.place(x=320,y=210, height=40, width=110)

                
            def adim2():
                global anlikveri
                global cal
                global saatgir
                global tarihgir
                global tarih
                global datesystem
                global tarihbilgisi
                global saatbilgisi
                global saatliste
                global tarihliste

                anlikveri.place_forget()
                tarih.place_forget()

                onay2.place_forget()
                tarihbuton.place_forget()

                
                saatliste+=[saatbilgisi]
                
                tarihliste+=[tarihbilgisi]
                
                anlikveri=tk.Label(bas, text='Sistem Tarihi:'+str(datesystem[0])+'     ',fg='green', bg='#dadadb')
                anlikveri.config(font=("Courier", 12))
                anlikveri.place(x=240,y=390)
                hatbasinc()

                
                
            
            onay2=tk.Button(bas, text='Onayla', fg='black', bg='#299584',height=1, width=6, command=adim2)
            onay2.place(x=400,y=240,height=50, width=110)

            bus = smbus.SMBus(1)
            

            try:

                pressure=bus.read_i2c_block_data(address, 0xAA, 7)
                
                sleep(1)
                
                pressure=bus.read_i2c_block_data(address, 0xAA, 7)
                pressuresonuc=((pressure[3] | (pressure[1] <<16) | (pressure[2]<<8))-3260274.9)/5050000
                cihazsicaklik= (((pressure[4] <<16) | (pressure[5]<<8) | pressure[6])-4603703)/116593
                
                
                cihazsicaklikdegerleri+=[cihazsicaklik]
                acikhavabasinci+=[pressuresonuc]
                
                anlikveri=tk.Label(bas, text='Açık Hava Basıncı(Bar): '+str(round(acikhavabasinci[0], 4))+ ', Cihaz Sıcaklık(C):'+ str(round(cihazsicaklikdegerleri[0],2)),fg='green', bg='#dadadb')
                anlikveri.config(font=("Courier", 12))
                anlikveri.place(x=160,y=370)
            except:

                acikhavabasinci+=[0]
                cihazsicaklikdegerleri+=[0]
                anlikveri=tk.Label(bas, text='Bir sorun var!\n İşleme devam ederseniz kabul edilebilir hata %7 olacak. \n'+'Açık Hava Basıncı(Bar): '+str(acikhavabasinci[0])+ ', Cihaz Sıcaklık(C):'+ str(cihazsicaklikdegerleri[0]),fg='red', bg='#dadadb')
                anlikveri.config(font=("Courier", 12))
                anlikveri.place(x=150,y=320)

            print("devam ediyor")



        

        

    ####Serino onayla butonu
    onay1=tk.Button(bas,text='Onayla',fg='black',bg='#299584',height=1, width=6, command=adim1)
    onay1.place(x=280,y=240,height=50, width=80)
    #serino.insert(0,"Seri Numarası Giriniz")    
    


    
    #######SİSTEM TARİHİ ANA EKRAN####
    sistemtarihi=tk.Label(bas, text='Sistem Tarihi:'+"\n"+ str(datesystem[0]),fg='#299584', bg='#dadadb')
    sistemtarihi.config(font=("Courier", 12))
    sistemtarihi.place(x=500,y=0)
    #######SİSTEM TARİHİ ANA EKRAN####

    


    def press(num):
        # point out the global expression variable
        
        global expression

        # concatenation of string
        expression = expression + str(num)

        # update the expression by using set method
        equation.set(expression)
        
        
        
        #Decimal.place(x=-locx,y=-locy)

        


    # Function to evaluate the final expression

    def clear():
        global expression
        expression = ""
        equation.set("")





    equation = tk.StringVar()

    # create the text entry box for
    # showing the expression .
    #serino=tk.Entry(width=20)
    #serino.place(x=150,y=20)
    serino = tk.Entry(bas, textvariable=equation)
    

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    serino.place(x=220,y=200,width=200,height=30)
   


    button1 = tk.Button(bas, text=' 1 ', fg='black', bg='#299584',command=lambda: press(1), height=3, width=5)
    button1.place(x=550, y=40)

    button2 = tk.Button(bas, text=' 2 ', fg='black', bg='#299584',command=lambda: press(2), height=3, width=5)
    button2.place(x=620, y=40)

    button3 = tk.Button(bas, text=' 3 ', fg='black', bg='#299584',command=lambda: press(3), height=3, width=5)
    button3.place(x=690, y=40)

    button4 = tk.Button(bas, text=' 4 ', fg='black', bg='#299584',command=lambda: press(4), height=3, width=5)
    button4.place(x=550, y=110)

    button5 = tk.Button(bas, text=' 5 ', fg='black', bg='#299584',command=lambda: press(5), height=3, width=5)
    button5.place(x=620, y=110)

    button6 = tk.Button(bas, text=' 6 ', fg='black', bg='#299584',command=lambda: press(6), height=3, width=5)
    button6.place(x=690, y=110)
    
    button7 = tk.Button(bas, text=' 7 ', fg='black', bg='#299584',command=lambda: press(7), height=3, width=5)
    button7.place(x=550, y=180)

    button8 = tk.Button(bas, text=' 8 ', fg='black', bg='#299584',command=lambda: press(8), height=3, width=5)
    button8.place(x=620, y=180)

    button9 = tk.Button(bas, text=' 9 ', fg='black', bg='#299584',command=lambda: press(9), height=3, width=5)
    button9.place(x=690, y=180)

    button0 = tk.Button(bas, text=' 0 ', fg='black', bg='#299584',command=lambda: press(0), height=3, width=5)
    button0.place(x=620, y=250)

    clear = tk.Button(bas, text='Clear', fg='black', bg='#299584',command=clear, height=3, width=5)
    clear.place(x=690, y=250)

    Decimal= tk.Button(bas, text=':', fg='black', bg='#299584',command=lambda: press(':'), height=3, width=5)
    Decimal.place(x=550, y=250)


   


    bas.mainloop()
    
if __name__ == "__main__":
    main()





from tkinter import*
import mysql.connector
from PIL import Image,ImageTk
top=Tk()
top.geometry("1500x1000")
top.title("AGRO INDIA")

i0=Image.open(r"C:\Users\chand\Documents\RTP\images\welcome.jpg")
p0=ImageTk.PhotoImage(i0)

l=Label(top,image=p0)
l.place(x=0,y=0)

global soil
soil=IntVar()
water=IntVar()
season=IntVar()
global s
global z
global x
global y
z=0
x=0
y=0

#home page_____________________________________________________________________________________________________________________________



l=Label(top,text="AGRO INDIA",font="helvetica 30 bold",bg="lightblue",padx=600).place(x=20,y=40)

i=Image.open(r"C:\Users\chand\Documents\RTP\images\happy_farmer.jpg")
p=ImageTk.PhotoImage(i)

l=Label(top,image=p)
l.place(x=100,y=110)

ii=Image.open(r"C:\Users\chand\Documents\RTP\images\logo.jpg")
pp=ImageTk.PhotoImage(ii)

l=Label(top,image=pp)
l.place(x=570,y=110)

ii1=Image.open(r"C:\Users\chand\Documents\RTP\images\drone.jpg")
pp1=ImageTk.PhotoImage(ii1)

l=Label(top,image=pp1)
l.place(x=900,y=110)

l=Label(top,text="Welcome to our cutting-edge agricultural software solution!\n Our mission is to empower farmers with advanced technology to optimize crop yields, reduce resource wastage, and enhance overall productivity.\n Explore our intuitive tools, real-time data analytics, and expert recommendations to revolutionize your farming practices and cultivate a sustainable future.",font="arial 12 bold")
l.place(x=140,y=400)

l=Label(top,text="SELECT THE FIELD:",font="helvetica 15 bold")
l.place(x=680,y=520)


#crop suggestion section______________________________________________________________________________________________________________________
def crop():
    
    top1=Toplevel()
    top1.geometry("1500x1000")
    top1.title("AGRO INDIA")
    
    
    i40=Image.open(r"C:\Users\chand\Documents\RTP\images\bg_crop.jpg")
    p40=ImageTk.PhotoImage(i40)
    l=Label(top1,image=p40).place(x=0,y=0)
    l=Label(top1,text="SELECT SOIL TYPE:",font="arial 15 bold").place(x=100,y=20)


    soil=IntVar()

    def selectred():
        global z
        
        
        if z==0:
            z=1
            #global s
            soil.set(1)
            s=soil.get()
            i1=Image.open(r"C:\Users\chand\Documents\RTP\images\tickmark.png")
            p1=ImageTk.PhotoImage(i1)
            b=Button(top1,image=p1).place(x=210,y=100)
            top1.mainloop()
            
    def selectblack():
        global z
        if z==0:
            z=2
            
            soil.set(2)
            s=soil.get()
            #print(soil)
            i1=Image.open(r"C:\Users\chand\Documents\RTP\images\tickmark.png")
            p1=ImageTk.PhotoImage(i1)
            b=Button(top1,image=p1).place(x=550,y=100)
            top1.mainloop()

    def selectaluvial():
        global z
        if z==0:
            z=3
            
            soil.set(3)
            i1=Image.open(r"C:\Users\chand\Documents\RTP\images\tickmark.png")
            p1=ImageTk.PhotoImage(i1)
            b=Button(top1,image=p1).place(x=850,y=100)
            top1.mainloop()

    def selectclayey():
        global z
        if z==0:
            z=4
            soil.set(4)
        
            i1=Image.open(r"C:\Users\chand\Documents\RTP\images\tickmark.png")
            p1=ImageTk.PhotoImage(i1)
            b=Button(top1,image=p1).place(x=1150,y=100)
            top1.mainloop()
            
    #soil selection
    
    i1=Image.open(r"C:\Users\chand\Documents\RTP\images\redsoil.jpg")
    p1=ImageTk.PhotoImage(i1)
    b=Button(top1,image=p1,command=selectred).place(x=150,y=70)
    l=Label(top1,text="RED SOIL").place(x=250,y=250)
    
    i2=Image.open(r"C:\Users\chand\Documents\RTP\images\blacksoil.jpg")
    p2=ImageTk.PhotoImage(i2)
    b=Button(top1,image=p2,command=selectblack).place(x=450,y=70)
    l=Label(top1,text="BLACK SOIL").place(x=545,y=250)

    i3=Image.open(r"C:\Users\chand\Documents\RTP\images\aluvialsoil.jpg")
    p3=ImageTk.PhotoImage(i3)
    b=Button(top1,image=p3,command=selectaluvial).place(x=750,y=70)
    l=Label(top1,text="ALUVIAL SOIL").place(x=840,y=250)

    i4=Image.open(r"C:\Users\chand\Documents\RTP\images\claveysoil.jpg")
    p4=ImageTk.PhotoImage(i4)
    b=Button(top1,image=p4,command=selectclayey).place(x=1050,y=70)
    l=Label(top1,text="CLAYEY SOIL").place(x=1140,y=250)


    #water availability selection
    l=Label(top1,text="WATER AVAILABILITY:",font="arial 15 bold",fg="black").place(x=100,y=285)

    def selecthigh():
        global x
        if x==0:
            x=1
            water.set(1)
    
            i1=Image.open(r"C:\Users\chand\Documents\RTP\images\tickmark.png")
            p1=ImageTk.PhotoImage(i1)
            b=Button(top1,image=p1).place(x=230,y=375)
            top1.mainloop()
    def selectmedium():
        global x
        if x==0:
            x=2
            water.set(2)
            i1=Image.open(r"C:\Users\chand\Documents\RTP\images\tickmark.png")
            p1=ImageTk.PhotoImage(i1)
            b=Button(top1,image=p1).place(x=520,y=375)
            top1.mainloop()

    def selectlow():
        global x
        if x==0:
            x=3
            water.set(3)
            i1=Image.open(r"C:\Users\chand\Documents\RTP\images\tickmark.png")
            p1=ImageTk.PhotoImage(i1)
            b=Button(top1,image=p1).place(x=820,y=375)
            top1.mainloop()
    
    i5=Image.open(r"C:\Users\chand\Documents\RTP\images\high.png")
    p5=ImageTk.PhotoImage(i5)
    b=Button(top1,image=p5,command=selecthigh).place(x=170,y=335)
    
    
    i6=Image.open(r"C:\Users\chand\Documents\RTP\images\medium.png")
    p6=ImageTk.PhotoImage(i6)
    b=Button(top1,image=p6,command=selectmedium).place(x=450,y=335)
    

    i7=Image.open(r"C:\Users\chand\Documents\RTP\images\low.png")
    p7=ImageTk.PhotoImage(i7)
    b=Button(top1,image=p7,command=selectlow).place(x=750,y=335)
    
    #SEASON SELECTION
    l=Label(top1,text="SELECT SEASON:",font="arial 15 bold",fg="black").place(x=100,y=550)

    def selectrainy():
        global y
        if y==0:
            y=1
            season.set(1)
            i1=Image.open(r"C:\Users\chand\Documents\RTP\images\tickmark.png")
            p1=ImageTk.PhotoImage(i1)
            b=Button(top1,image=p1).place(x=270,y=620)
            top1.mainloop()
            
    def selectsummer():
        global y
        if y==0:
            y=1
            season.set(2)
            i1=Image.open(r"C:\Users\chand\Documents\RTP\images\tickmark.png")
            p1=ImageTk.PhotoImage(i1)
            b=Button(top1,image=p1).place(x=550,y=620)
            top1.mainloop()

    def selectwinter():
        global y
        if y==0:
            y=1
            season.set(3)
            i1=Image.open(r"C:\Users\chand\Documents\RTP\images\tickmark.png")
            p1=ImageTk.PhotoImage(i1)
            b=Button(top1,image=p1).place(x=850,y=620)
            top1.mainloop()
    
    i8=Image.open(r"C:\Users\chand\Documents\RTP\images\rainy.jpg")
    p8=ImageTk.PhotoImage(i8)
    b=Button(top1,image=p8,command=selectrainy).place(x=170,y=600)
    
    
    i9=Image.open(r"C:\Users\chand\Documents\RTP\images\summer.jpg")
    p9=ImageTk.PhotoImage(i9)
    b=Button(top1,image=p9,command=selectsummer).place(x=450,y=600)
    

    i10=Image.open(r"C:\Users\chand\Documents\RTP\images\winter.jpg")
    p10=ImageTk.PhotoImage(i10)
    b=Button(top1,image=p10,command=selectwinter).place(x=780,y=600)
    
    
    #crop suggestion
    
    def seedsuggestion():
        
        global s
        
        s=soil.get()
        w=water.get()
        sea=season.get()
        top2=Toplevel()
        top2.geometry("1500x1000")
        top2.title("AGRO INDIA")
        i41=Image.open(r"C:\Users\chand\Documents\RTP\images\welcome.jpg")
        p41=ImageTk.PhotoImage(i41)
        l=Label(top2,image=p41).place(x=0,y=0)
        
        l=Label(top2,text="RECOMENDATIONS FOR CROPS AND SEEDS:                                                                   ",font="helvetica 25 bold",bg="lightblue",padx=50).place(x=60,y=50)
        l=Label(top2,text=" SUITABLE CROP :",font="helvetica 15 bold",bg="lightgreen").place(x=100,y=200)
        l=Label(top2,text=" SEED RECOMENDATION:",font="helvetica 15 bold",bg="lightgreen").place(x=900,y=200)
     
        #paddy
        if s==4 :
            if w==1 and sea==2:
                i11=Image.open(r"C:\Users\chand\Documents\RTP\images\paddy.jpg")
                p11=ImageTk.PhotoImage(i11)

                l=Label(top2,image=p11)
                l.place(x=230,y=300)
                l=Label(top2,text="paddy",font="helvetica 15 bold").place(x=380,y=590)

                i12=Image.open(r"C:\Users\chand\Documents\RTP\images\paddy seeds.png")
                p12=ImageTk.PhotoImage(i12)

                l1=Label(top2,image=p12)
                l1.place(x=1030,y=300)
                
              
                top2.mainloop()       
                
            elif w==2 and sea==1:
                i13=Image.open(r"C:\Users\chand\Documents\RTP\images\paddy.jpg")
                p13=ImageTk.PhotoImage(i13)

                l1=Label(top2,image=p13)
                l1.place(x=230,y=300)
                l=Label(top2,text="PADDY",font="helvetica 15 bold").place(x=380,y=590)

                i14=Image.open(r"C:\Users\chand\Documents\RTP\images\paddy seeds.png")
                p14=ImageTk.PhotoImage(i14)

                l1=Label(top2,image=p14)
                l1.place(x=1030,y=300)
                

                top2.mainloop()
                
        #maize
        if s==1 and w==2 and sea==1:
            i15=Image.open(r"C:\Users\chand\Documents\RTP\images\maize.jpeg")
            p15=ImageTk.PhotoImage(i15)

            l1=Label(top2,image=p15)
            l1.place(x=230,y=300)
            l=Label(top2,text="MAIZE",font="helvetica 15 bold").place(x=380,y=590)

            i16=Image.open(r"C:\Users\chand\Documents\RTP\images\maize seeds.jpg")
            p16=ImageTk.PhotoImage(i16)

            l1=Label(top2,image=p16)
            l1.place(x=1030,y=300)
                
               
            top2.mainloop()
            
        #cotton
            
        if s==2 and w==2 and sea==1:
            i17=Image.open(r"C:\Users\chand\Documents\RTP\images\Cotton.JPG")
            p17=ImageTk.PhotoImage(i17)

            l1=Label(top2,image=p17)
            l1.place(x=230,y=300)
            l=Label(top2,text="COTTON",font="helvetica 15 bold").place(x=380,y=590)

            i18=Image.open(r"C:\Users\chand\Documents\RTP\images\cotton seeds.jpeg")
            p18=ImageTk.PhotoImage(i18)

            l1=Label(top2,image=p18)
            l1.place(x=1030,y=300)
            
                
            top2.mainloop()
            
            
        #pulses
        if s==1 and w==3 and sea==1:
            i19=Image.open(r"C:\Users\chand\Documents\RTP\images\groundnut.jpeg")
            p19=ImageTk.PhotoImage(i19)

            l1=Label(top2,image=p19)
            l1.place(x=230,y=300)
            l=Label(top2,text="GROUNDNUT",font="helvetica 15 bold").place(x=380,y=590)

            i20=Image.open(r"C:\Users\chand\Documents\RTP\images\groundnut seeds.jpeg")
            p20=ImageTk.PhotoImage(i20)

            l1=Label(top2,image=p20)
            l1.place(x=1030,y=300)
                
                
            top2.mainloop()
            
        #sunflower
        if s==2 and w==3 and sea==2:
            i21=Image.open(r"C:\Users\chand\Documents\RTP\images\sunflower.jpg")
            p21=ImageTk.PhotoImage(i21)

            l1=Label(top2,image=p21)
            l1.place(x=230,y=300)
            l=Label(top2,text="SUNFLOWER",font="helvetica 15 bold").place(x=380,y=590)

            i22=Image.open(r"C:\Users\chand\Documents\RTP\images\sunflower seeds.jpeg")
            p22=ImageTk.PhotoImage(i22)

            l1=Label(top2,image=p22)
            l1.place(x=1030,y=300)
                             
            top2.mainloop()
            
        #wheat
        if s==3:
            if w==1 and sea==2:
                i23=Image.open(r"C:\Users\chand\Documents\RTP\images\wheat.jpeg")
                p23=ImageTk.PhotoImage(i23)

                l1=Label(top2,image=p23)
                l1.place(x=230,y=300)
                l=Label(top2,text="WHEAT",font="helvetica 15 bold").place(x=380,y=590)

                i24=Image.open(r"C:\Users\chand\Documents\RTP\images\wheat seeds.jpg")
                p24=ImageTk.PhotoImage(i24)

                l1=Label(top2,image=p24)
                l1.place(x=1030,y=300)
            
                
                top2.mainloop()
                
            elif w==2 and sea==1:
                i25=Image.open(r"C:\Users\chand\Documents\RTP\images\wheat.jpeg")
                p25=ImageTk.PhotoImage(i25)

                l1=Label(top2,image=p25)
                l1.place(x=230,y=300)
                l=Label(top2,text="WHEAT",font="helvetica 15 bold").place(x=380,y=590)

                i26=Image.open(r"C:\Users\chand\Documents\RTP\images\wheat seeds.jpg")
                p26=ImageTk.PhotoImage(i26)

                l1=Label(top2,image=p26)
                l1.place(x=1030,y=300)

                
                top2.mainloop()
                
    
    b=Button(top1,text="show suggestion",font="arial 15 bold",bg="lightgreen",command=seedsuggestion).place(x=1200,y=590)
    top1.mainloop()


#fertilizers suggestion section__________________________________________________________________________________________________



def fertilizer():
    
    top4=Toplevel()
    top4.geometry("1500x1000")
    
    top4.title("AGRO INDIA")
    l=Label(top4,text="          FERTILIZERS                ",font="arial 25 bold",fg="black",bg="lightblue",padx=500).place(x=10,y=20)
    l=Label(top4,text="SELECT THE CROP:",font="arial 16 bold",fg="black").place(x=50,y=90)
    l=Label(top4,text="FERTILIZER:",font="arial 16 bold",fg="black").place(x=50,y=400)
    l=Label(top4,text="FERTILIZER DETAILS:",font="arial 16 bold",fg="black").place(x=850,y=400)


    def paddyfertilizer():

        i34=Image.open(r"C:\Users\chand\Documents\RTP\images\whitebg.jpg")
        p34=ImageTk.PhotoImage(i34)

        l=Label(top4,image=p34)
        l.place(x=230,y=450)

        i35=Image.open(r"C:\Users\chand\Documents\RTP\images\whitebg.jpg")
        p35=ImageTk.PhotoImage(i35)

        l=Label(top4,image=p35)
        l.place(x=830,y=450)

        i34=Image.open(r"C:\Users\chand\Documents\RTP\images\paddy_fertilizer_det.jpg")
        p34=ImageTk.PhotoImage(i34)

        l=Label(top4,image=p34)
        l.place(x=830,y=450)
        
        i33=Image.open(r"C:\Users\chand\Documents\RTP\images\paddy_fertilizer.jpg")
        p33=ImageTk.PhotoImage(i33)

        l=Label(top4,image=p33)
        l.place(x=230,y=450)
        
        top4.mainloop()


    def maizefertilizer():
        i34=Image.open(r"C:\Users\chand\Documents\RTP\images\whitebg.jpg")
        p34=ImageTk.PhotoImage(i34)

        l=Label(top4,image=p34)
        l.place(x=230,y=450)

        i35=Image.open(r"C:\Users\chand\Documents\RTP\images\whitebg.jpg")
        p35=ImageTk.PhotoImage(i35)

        l=Label(top4,image=p35)
        l.place(x=830,y=450)


        i34=Image.open(r"C:\Users\chand\Documents\RTP\images\maize_fertilizer_det.png")
        p34=ImageTk.PhotoImage(i34)

        l=Label(top4,image=p34)
        l.place(x=830,y=450)
        
        i33=Image.open(r"C:\Users\chand\Documents\RTP\images\maize_fertilizer.png")
        p33=ImageTk.PhotoImage(i33)

        l=Label(top4,image=p33)
        l.place(x=230,y=450)
        
        top4.mainloop()

    def groundnutfertilizer():
        i34=Image.open(r"C:\Users\chand\Documents\RTP\images\whitebg.jpg")
        p34=ImageTk.PhotoImage(i34)

        l=Label(top4,image=p34)
        l.place(x=230,y=450)

        i35=Image.open(r"C:\Users\chand\Documents\RTP\images\whitebg.jpg")
        p35=ImageTk.PhotoImage(i35)

        l=Label(top4,image=p35)
        l.place(x=830,y=450)

        i34=Image.open(r"C:\Users\chand\Documents\RTP\images\groundnut_fertilizer_det.png")
        p34=ImageTk.PhotoImage(i34)

        l=Label(top4,image=p34)
        l.place(x=830,y=450)
        
        i33=Image.open(r"C:\Users\chand\Documents\RTP\images\groundnut_fertilizer.png")
        p33=ImageTk.PhotoImage(i33)

        l=Label(top4,image=p33)
        l.place(x=230,y=450)
        
        top4.mainloop()

    def cottonfertilizer():

        i34=Image.open(r"C:\Users\chand\Documents\RTP\images\whitebg.jpg")
        p34=ImageTk.PhotoImage(i34)

        l=Label(top4,image=p34)
        l.place(x=230,y=450)

        i35=Image.open(r"C:\Users\chand\Documents\RTP\images\whitebg.jpg")
        p35=ImageTk.PhotoImage(i35)

        l=Label(top4,image=p35)
        l.place(x=830,y=450)
        
        i34=Image.open(r"C:\Users\chand\Documents\RTP\images\cotton_fetilizer_det.png")
        p34=ImageTk.PhotoImage(i34)

        l=Label(top4,image=p34)
        l.place(x=830,y=450)
        
        
        i33=Image.open(r"C:\Users\chand\Documents\RTP\images\cotton_fertilizer.png")
        p33=ImageTk.PhotoImage(i33)

        l=Label(top4,image=p33)
        l.place(x=230,y=450)
        
        top4.mainloop()

    def sunflowerfertilizer():
        i34=Image.open(r"C:\Users\chand\Documents\RTP\images\whitebg.jpg")
        p34=ImageTk.PhotoImage(i34)

        l=Label(top4,image=p34)
        l.place(x=230,y=450)

        i35=Image.open(r"C:\Users\chand\Documents\RTP\images\whitebg.jpg")
        p35=ImageTk.PhotoImage(i35)

        l=Label(top4,image=p35)
        l.place(x=830,y=450)

        i34=Image.open(r"C:\Users\chand\Documents\RTP\images\sunflower_fertilizer_det.png")
        p34=ImageTk.PhotoImage(i34)

        l=Label(top4,image=p34)
        l.place(x=830,y=450)
        
        i33=Image.open(r"C:\Users\chand\Documents\RTP\images\sunflower_fertilizer.png")
        p33=ImageTk.PhotoImage(i33)

        l=Label(top4,image=p33)
        l.place(x=230,y=450)
        
        top4.mainloop()

    def wheatfertilizer():
        i34=Image.open(r"C:\Users\chand\Documents\RTP\images\whitebg.jpg")
        p34=ImageTk.PhotoImage(i34)

        l=Label(top4,image=p34)
        l.place(x=230,y=450)

        i35=Image.open(r"C:\Users\chand\Documents\RTP\images\whitebg.jpg")
        p35=ImageTk.PhotoImage(i35)

        l=Label(top4,image=p35)
        l.place(x=830,y=450)

        i34=Image.open(r"C:\Users\chand\Documents\RTP\images\wheat_fertilizer_det.png")
        p34=ImageTk.PhotoImage(i34)

        l=Label(top4,image=p34)
        l.place(x=830,y=450)
        
        i33=Image.open(r"C:\Users\chand\Documents\RTP\images\wheat_fertilizer.png")
        p33=ImageTk.PhotoImage(i33)

        l=Label(top4,image=p33)
        l.place(x=230,y=450)
        
        top4.mainloop()
    
    
    i27=Image.open(r"C:\Users\chand\Documents\RTP\images\fertilizers section\paddy.jpg")
    p27=ImageTk.PhotoImage(i27)
    b=Button(top4,image=p27,command=paddyfertilizer)
    b.place(x=50,y=150)
    
    
    i28=Image.open(r"C:\Users\chand\Documents\RTP\images\fertilizers section\maize.jpg")
    p28=ImageTk.PhotoImage(i28)
    b=Button(top4,image=p28,command=maizefertilizer)
    b.place(x=300,y=160)
    
    
    i29=Image.open(r"C:\Users\chand\Documents\RTP\images\fertilizers section\groundnut.jpg")
    p29=ImageTk.PhotoImage(i29)
    b=Button(top4,image=p29,command=groundnutfertilizer)
    b.place(x=550,y=150)
    
    
    i30=Image.open(r"C:\Users\chand\Documents\RTP\images\fertilizers section\cotton.jpg")
    p30=ImageTk.PhotoImage(i30)
    b=Button(top4,image=p30,command=cottonfertilizer)
    b.place(x=800,y=150)

    i31=Image.open(r"C:\Users\chand\Documents\RTP\images\fertilizers section\sunflower.jpg")
    p31=ImageTk.PhotoImage(i31)
    b=Button(top4,image=p31,command=sunflowerfertilizer)
    b.place(x=1050,y=150)

    i32=Image.open(r"C:\Users\chand\Documents\RTP\images\fertilizers section\wheat.jpg")
    p32=ImageTk.PhotoImage(i32)
    b=Button(top4,image=p32,command=wheatfertilizer)
    b.place(x=1300,y=150)
    
    l=Label(top4,text="PADDY",font="arial 12 bold").place(x=120,y=290)
    l=Label(top4,text="MAIZE",font="arial 12 bold").place(x=370,y=290)
    
    l=Label(top4,text="GROUNDNUT",font="arial 12 bold").place(x=600,y=290)
    l=Label(top4,text="COTTON",font="arial 12 bold").place(x=850,y=290)
    l=Label(top4,text="SUNFLOWER",font="arial 12 bold").place(x=1100,y=290)
    l=Label(top4,text="WHEAT",font="arial 12 bold").place(x=1350,y=290)

    top4.mainloop()

    #pesticide
def pesticide():
    
    top4=Toplevel()
    top4.geometry("1500x1000")
    
    top4.title("AGRO INDIA")
    l=Label(top4,text="          PESTICIDES                ",font="arial 25 bold",fg="black",bg="lightblue",padx=500).place(x=10,y=20)
    l=Label(top4,text="SELECT THE CROP:",font="arial 16 bold",fg="black").place(x=50,y=90)
    l=Label(top4,text="MAJOR PESTS:",font="arial 16 bold",fg="black").place(x=50,y=400)
    l=Label(top4,text="PESTICIDE DETAILS:",font="arial 16 bold",fg="black").place(x=550,y=400)


    def paddypesticide():

        i34=Image.open(r"C:\Users\chand\Documents\RTP\images\whitebgpest.png")
        p34=ImageTk.PhotoImage(i34)

        l=Label(top4,image=p34)
        l.place(x=10,y=450)

        i36=Image.open(r"C:\Users\chand\Documents\RTP\images\paddy_pesticide.png")
        p36=ImageTk.PhotoImage(i36)

        l=Label(top4,image=p36)
        l.place(x=600,y=450)

        i37=Image.open(r"C:\Users\chand\Documents\RTP\images\paddy_pesticide_det.png")
        p37=ImageTk.PhotoImage(i37)

        l=Label(top4,image=p37)
        l.place(x=880,y=480)
        
        i38=Image.open(r"C:\Users\chand\Documents\RTP\images\Paddy_insect.png")
        p38=ImageTk.PhotoImage(i38)

        l=Label(top4,image=p38)
        l.place(x=130,y=450)
        
        top4.mainloop()


    def maizepesticide():
        
        i34=Image.open(r"C:\Users\chand\Documents\RTP\images\whitebgpest.png")
        p34=ImageTk.PhotoImage(i34)

        l=Label(top4,image=p34)
        l.place(x=10,y=450)

        i37=Image.open(r"C:\Users\chand\Documents\RTP\images\maize_pesticide_det.png")
        p37=ImageTk.PhotoImage(i37)

        l=Label(top4,image=p37)
        l.place(x=900,y=450)
        


        i34=Image.open(r"C:\Users\chand\Documents\RTP\images\maize_pesticide.png")
        p34=ImageTk.PhotoImage(i34)

        l=Label(top4,image=p34)
        l.place(x=600,y=450)
        
        i33=Image.open(r"C:\Users\chand\Documents\RTP\images\maize_pest.jpg")
        p33=ImageTk.PhotoImage(i33)

        l=Label(top4,image=p33)
        l.place(x=230,y=450)
        
        top4.mainloop()

    def groundnutpesticide():
        
        i34=Image.open(r"C:\Users\chand\Documents\RTP\images\whitebgpest.png")
        p34=ImageTk.PhotoImage(i34)

        l=Label(top4,image=p34)
        l.place(x=10,y=450)


        i36=Image.open(r"C:\Users\chand\Documents\RTP\images\groundnut_pesticide.png")
        p36=ImageTk.PhotoImage(i36)

        l=Label(top4,image=p36)
        l.place(x=600,y=450)

        

        i34=Image.open(r"C:\Users\chand\Documents\RTP\images\groundnut_pesticide_det.png")
        p34=ImageTk.PhotoImage(i34)

        l=Label(top4,image=p34)
        l.place(x=890,y=450)
        
        i33=Image.open(r"C:\Users\chand\Documents\RTP\images\groundnut_pest.jpg")
        p33=ImageTk.PhotoImage(i33)

        l=Label(top4,image=p33)
        l.place(x=230,y=450)
        
        top4.mainloop()

    def cottonpesticide():

        i34=Image.open(r"C:\Users\chand\Documents\RTP\images\whitebgpest.png")
        p34=ImageTk.PhotoImage(i34)

        l=Label(top4,image=p34)
        l.place(x=10,y=450)

        i36=Image.open(r"C:\Users\chand\Documents\RTP\images\cotton_pesticide.png")
        p36=ImageTk.PhotoImage(i36)

        l=Label(top4,image=p36)
        l.place(x=600,y=450)
        
        
        i34=Image.open(r"C:\Users\chand\Documents\RTP\images\cotton_pesticide_det.png")
        p34=ImageTk.PhotoImage(i34)

        l=Label(top4,image=p34)
        l.place(x=890,y=450)
        
        
        i33=Image.open(r"C:\Users\chand\Documents\RTP\images\cotton_pest.jpg")
        p33=ImageTk.PhotoImage(i33)

        l=Label(top4,image=p33)
        l.place(x=230,y=450)
        
        top4.mainloop()

    def sunflowerpesticide():
        i34=Image.open(r"C:\Users\chand\Documents\RTP\images\whitebgpest.png")
        p34=ImageTk.PhotoImage(i34)

        l=Label(top4,image=p34)
        l.place(x=10,y=450)
        

        i36=Image.open(r"C:\Users\chand\Documents\RTP\images\sunflower_pesticide.png")
        p36=ImageTk.PhotoImage(i36)

        l=Label(top4,image=p36)
        l.place(x=600,y=450)
        

        i34=Image.open(r"C:\Users\chand\Documents\RTP\images\sunflower_pesticide_det.png")
        p34=ImageTk.PhotoImage(i34)

        l=Label(top4,image=p34)
        l.place(x=860,y=450)
        
        i33=Image.open(r"C:\Users\chand\Documents\RTP\images\sunflower_pest.jpeg")
        p33=ImageTk.PhotoImage(i33)

        l=Label(top4,image=p33)
        l.place(x=230,y=450)
        
        top4.mainloop()

    def wheatpesticide():
        i34=Image.open(r"C:\Users\chand\Documents\RTP\images\whitebgpest.png")
        p34=ImageTk.PhotoImage(i34)

        l=Label(top4,image=p34)
        l.place(x=10,y=450)

        i36=Image.open(r"C:\Users\chand\Documents\RTP\images\wheat_pesticide.png")
        p36=ImageTk.PhotoImage(i36)

        l=Label(top4,image=p36)
        l.place(x=600,y=450)

        i34=Image.open(r"C:\Users\chand\Documents\RTP\images\wheat_pesticide_det.png")
        p34=ImageTk.PhotoImage(i34)

        l=Label(top4,image=p34)
        l.place(x=900,y=480)
        
        i33=Image.open(r"C:\Users\chand\Documents\RTP\images\wheat_pest.jpg")
        p33=ImageTk.PhotoImage(i33)

        l=Label(top4,image=p33)
        l.place(x=230,y=450)
        
        top4.mainloop()
    
    i27=Image.open(r"C:\Users\chand\Documents\RTP\images\fertilizers section\paddy.jpg")
    p27=ImageTk.PhotoImage(i27)
    b=Button(top4,image=p27,command=paddypesticide)
    b.place(x=50,y=150)
    
    
    i28=Image.open(r"C:\Users\chand\Documents\RTP\images\fertilizers section\maize.jpg")
    p28=ImageTk.PhotoImage(i28)
    b=Button(top4,image=p28,command=maizepesticide)
    b.place(x=300,y=160)
    
    
    i29=Image.open(r"C:\Users\chand\Documents\RTP\images\fertilizers section\groundnut.jpg")
    p29=ImageTk.PhotoImage(i29)
    b=Button(top4,image=p29,command=groundnutpesticide)
    b.place(x=550,y=150)
    
    
    i30=Image.open(r"C:\Users\chand\Documents\RTP\images\fertilizers section\cotton.jpg")
    p30=ImageTk.PhotoImage(i30)
    b=Button(top4,image=p30,command=cottonpesticide)
    b.place(x=800,y=150)

    i31=Image.open(r"C:\Users\chand\Documents\RTP\images\fertilizers section\sunflower.jpg")
    p31=ImageTk.PhotoImage(i31)
    b=Button(top4,image=p31,command=sunflowerpesticide)
    b.place(x=1050,y=150)

    i32=Image.open(r"C:\Users\chand\Documents\RTP\images\fertilizers section\wheat.jpg")
    p32=ImageTk.PhotoImage(i32)
    b=Button(top4,image=p32,command=wheatpesticide)
    b.place(x=1300,y=150)
    
    l=Label(top4,text="PADDY",font="arial 12 bold").place(x=120,y=290)
    l=Label(top4,text="MAIZE",font="arial 12 bold").place(x=370,y=290)
    
    l=Label(top4,text="GROUNDNUT",font="arial 12 bold").place(x=600,y=290)
    l=Label(top4,text="COTTON",font="arial 12 bold").place(x=850,y=290)
    l=Label(top4,text="SUNFLOWER",font="arial 12 bold").place(x=1100,y=290)
    l=Label(top4,text="WHEAT",font="arial 12 bold").place(x=1350,y=290)

    
    top4.mainloop()


   #crop market___________________________________________________________________________________________________________
def cropmarket():
    top5=Toplevel()
    top5.geometry("1500x1000")


    i=Image.open(r"C:\Users\chand\Documents\RTP\images\top5_bg.jpg")
    p=ImageTk.PhotoImage(i)

    l=Label(top5,image=p)
    l.image=p
    l.place(x=0,y=0)
    
    top5.title("AGRO INDIA")
    l=Label(top5,text="MARKET RATES",font="billyargel 24 bold",fg="black",bg="lightblue",padx=600).place(x=20,y=40)
    l=Label(top5,text="SELECT CROP:",font="billyargel 16 bold",fg="black",bg="lightgreen").place(x=20,y=116)

    selected_state=StringVar()
    states = ["ANDHRA PRADESH", "ASSAM","BIHAR","CHATTSIGARH","GUJARAT","HARYANA","JARKHAND","KARNATAKA","KERELA","MADHYA PRADESH","MAHARASTRA","ODHISA","PUNJAB","RAJASTHAN","TAMIL NADU","TELANGANA","UTTARPRADESH","UTTARKAND","WEST BENGAL"]
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="MARKETERATESDATA")
    mycursor=mydb.cursor()
    mycursor.execute("SELECT * FROM RATES_REAL")
    res= mycursor.fetchall()


    def display_rates(crop_rate,crop):

        name_label=Label(top5,text="CROP NAME:",bg="black",fg="white",font="billyargel 17 bold",width=16).place(x=450,y=280)

        crop_name_label=Label(top5,text=crop,bg="black",fg="white",font="billyargel 17 bold",width=16).place(x=700,y=280)

        rates_label=Label(top5,text="MARKET RATE/QUINTAL:",bg="black",fg="white",font="billyargel 17 bold",width=30).place(x=480,y=380)

        crop_rate_label=Label(top5,text="Rs."+str(crop_rate)+"/-",bg="black",fg="yellow",font="billyargel 30 bold",width=20).place(x=450,y=440)
    
    def fetch_marketrate_paddy(value):
        
        state = str(value)
        crop_rate=0
        for i in range(0,19):
            if res[i][0]==state :
                
                crop_rate=res[i][1]
                break

        display_rates(crop_rate,'PADDY')

    def fetch_marketrate_maize(value):
        
        state = str(value)

        crop_rate=1
        for i in range(0,19):
            if res[i][0]==state :
                
                crop_rate=res[i][2]
                break

        display_rates(crop_rate,'MAIZE')

    def fetch_marketrate_groundnut(value):
        
        state = str(value)

        crop_rate=1
        for i in range(0,19):
            if res[i][0]==state :
                
                crop_rate=res[i][3]
                break

        display_rates(crop_rate,'GROUNDNUT')

    def fetch_marketrate_cotton(value):
        
        state = str(value)

        crop_rate=1
        for i in range(0,19):
            if res[i][0]==state :
                
                crop_rate=res[i][4]
                break

        display_rates(crop_rate,'COTTON')

    def fetch_marketrate_sunflower(value):
        
        state = str(value)

        crop_rate=1
        for i in range(0,19):
            if res[i][0]==state :
                crop_rate=res[i][5]
                break

        display_rates(crop_rate,'SUNFLOWER')

    def fetch_marketrate_wheat(value):

        state = str(value)

        crop_rate=1
        for i in range(0,19):
            if res[i][0]==state :
                
                crop_rate=res[i][6]
                break

        display_rates(crop_rate,'WHEAT')

    def paddyprice():

        l=Label(top5,text="SELECT STATE:",bg="lightgreen",font="billyargel 12 bold",width=15).place(x=450,y=180)
        selected_state.set(states[0])  
        dropdown =OptionMenu(top5,selected_state, *states, command=fetch_marketrate_paddy)
        dropdown.config(width=20)
        dropdown.place(x=620,y=180)
        top5.mainloop()

    def maizeprice():
        l=Label(top5,text="SELECT STATE:",bg="lightgreen",font="billyargel 12 bold",width=15).place(x=450,y=180)
        selected_state.set(states[0])  
        dropdown =OptionMenu(top5,selected_state, *states, command=fetch_marketrate_maize)
        dropdown.config(width=20)
        dropdown.place(x=620,y=180)

        top5.mainloop()
        
    def groundnutprice():

        l=Label(top5,text="SELECT STATE:",bg="lightgreen",font="billyargel 12 bold",width=15).place(x=450,y=180)
        selected_state.set(states[0])  
        dropdown =OptionMenu(top5,selected_state, *states, command=fetch_marketrate_groundnut)
        dropdown.config(width=20)
        dropdown.place(x=620,y=180)

        top5.mainloop()

    def cottonprice():

        l=Label(top5,text="SELECT STATE:",bg="lightgreen",font="billyargel 12 bold",width=15).place(x=450,y=180)
        selected_state.set(states[0])  
        dropdown =OptionMenu(top5,selected_state, *states, command=fetch_marketrate_cotton)
        dropdown.config(width=20)
        dropdown.place(x=620,y=180)

        top5.mainloop()

    def sunflowerprice():

        l=Label(top5,text="SELECT STATE:",bg="lightgreen",font="billyargel 12 bold",width=15).place(x=450,y=180)
        selected_state.set(states[0])  
        dropdown =OptionMenu(top5,selected_state, *states, command=fetch_marketrate_sunflower)
        dropdown.config(width=20)
        dropdown.place(x=620,y=180)

        top5.mainloop()

    def wheatprice():

        l=Label(top5,text="SELECT STATE:",bg="lightgreen",font="billyargel 12 bold",width=15).place(x=450,y=180)
        selected_state.set(states[0])  
        dropdown =OptionMenu(top5,selected_state, *states, command=fetch_marketrate_wheat)
        dropdown.config(width=20)
        dropdown.place(x=620,y=180)

        top5.mainloop()
    
    b=Button(top5,text="PADDY",bg="black",fg="white",font="billyargel 15 bold",width=20,command=paddyprice).place(x=60,y=170)
    b=Button(top5,text="MAIZE",bg="black",fg="white",font="billyargel 15 bold",width=20,command=maizeprice).place(x=60,y=270)
    b=Button(top5,text="GROUNDNUT",bg="black",fg="white",font="billyargel 15 bold",width=20,command=groundnutprice).place(x=60,y=370)
    
    b=Button(top5,text="COTTON",bg="black",fg="white",font="billyargel 15 bold",width=20,command=cottonprice).place(x=60,y=470)
    b=Button(top5,text="SUNFLOWER",bg="black",fg="white",font="billyargel 15 bold",width=20,command=sunflowerprice).place(x=60,y=570)
    
    b=Button(top5,text="WHEAT",bg="black",fg="white",font="billyargel 15 bold",width=20,command=wheatprice).place(x=60,y=670)

    i=Image.open(r"C:\Users\chand\Documents\RTP\images\market_image.jpg")
    p=ImageTk.PhotoImage(i)

    l=Label(top5,image=p)
    l.place(x=1000,y=215)

    top5.mainloop()


    #modern techniques_____________________________________________________________________________________________________________________________
def modern():
    top6=Toplevel()
    top6.geometry("1500x1000")
    top6.title("AGRO INDIA")
    l=Label(top6,text="MODERN TECHNOLOGY IN THE FIELD OF AGRICULTURE",font="billyargel 24 bold",fg="black",bg="lightgreen",padx=400).place(x=10,y=40)
    l=Label(top6,text="SELECT THE FIELD:",font="billyargel 16 bold",fg="black").place(x=20,y=116)

    def seeding():

        i36=Image.open(r"C:\Users\chand\Documents\RTP\images\whitebg1.jpg")
        p36=ImageTk.PhotoImage(i36)
        l=Label(top6,image=p36)
        l.place(x=400,y=130)
        l=Label(top6,text="SEED DRILL",font="arial 20 bold",padx=10,width=20,bg="black",fg="white").place(x=750,y=200)

        i38=Image.open(r"C:\Users\chand\Documents\RTP\images\seeding_technique.jpg")
        p38=ImageTk.PhotoImage(i38)
        l=Label(top6,image=p38)
        l.place(x=680,y=250)
        l=Label(top6,text="ADVANTAGES :\n\n Precision Planting,Time Efficiency,reduced labour cost,\n\n increased productivity,customization options,sustainability ",font="helvetica 15 bold",width=70,bg="black",fg="white",pady=10).place(x=490,y=590)
        top6.mainloop()

    def irrigation():

        i36=Image.open(r"C:\Users\chand\Documents\RTP\images\whitebg1.jpg")
        p36=ImageTk.PhotoImage(i36)
        l=Label(top6,image=p36)
        l.place(x=400,y=130)
        l=Label(top6,text="SPRINKLERS",font="arial 20 bold",padx=10,width=20,bg="black",fg="white").place(x=750,y=200)

        i38=Image.open(r"C:\Users\chand\Documents\RTP\images\irrigation_technique.jpg")
        p38=ImageTk.PhotoImage(i38)
        l=Label(top6,image=p38)
        l.place(x=680,y=250)
        l=Label(top6,text="ADVANTAGES :\n\n Efficient Water Distribution,Time-Saving,Consistent Watering,\n\n Water Conservation,Improved Plant Health,sustainability ",width=70,bg="black",fg="white",font="helvetica 15 bold",pady=10).place(x=490,y=590)
        top6.mainloop()

    def spraying():
        
        i36=Image.open(r"C:\Users\chand\Documents\RTP\images\whitebg1.jpg")
        p36=ImageTk.PhotoImage(i36)
        l=Label(top6,image=p36)
        l.place(x=400,y=130)
        l=Label(top6,text="DRONES",font="arial 20 bold",padx=10,width=20,bg="black",fg="white").place(x=750,y=200)

        i38=Image.open(r"C:\Users\chand\Documents\RTP\images\spraying_technique.jpg")
        p38=ImageTk.PhotoImage(i38)
        l=Label(top6,image=p38)
        l.place(x=680,y=250)
        
        l=Label(top6,text="ADVANTAGES :\n\n Precision Application,Time Efficiency,Cost Savings,\n\n Environmental Benefits,Improved Crop Health Monitoring,Reduced Human Exposure ",width=70,bg="black",fg="white",font="helvetica 15 bold",pady=10).place(x=490,y=590)
        top6.mainloop()

    def harvesting():
        
        i36=Image.open(r"C:\Users\chand\Documents\RTP\images\whitebg1.jpg")
        p36=ImageTk.PhotoImage(i36)
        l=Label(top6,image=p36)
        l.place(x=400,y=130)
        l=Label(top6,text="MULTI-USE HARVESTORS",font="arial 20 bold",padx=10,width=20,bg="black",fg="white").place(x=750,y=200)

        i38=Image.open(r"C:\Users\chand\Documents\RTP\images\harvesting_technique.jpg")
        p38=ImageTk.PhotoImage(i38)
        l=Label(top6,image=p38)
        l.place(x=680,y=250)
        
        l=Label(top6,text="ADVANTAGES :\n\n Labor Savings,Cost Efficiency,Versatility,\n\n Enhanced Productivity,Technological Integration,Reduced Human Exposure ",font="helvetica 15 bold",pady=10,width=70,bg="black",fg="white").place(x=490,y=590)
        top6.mainloop()
    
    b=Button(top6,text="SEEDING TECCHNIQUES",bg="lightblue",font="billyargel 15 bold",width=30,command=seeding).place(x=20,y=170)
    b=Button(top6,text="IRRIGATION TECHNIQUES",bg="lightblue",font="billyargel 15 bold",width=30,command=irrigation).place(x=20,y=270)
    b=Button(top6,text="SPRAYING TECHNIQUES",bg="lightblue",font="billyargel 15 bold",width=30,command=spraying).place(x=20,y=370)
    b=Button(top6,text="HARVESTING TECHNIQUES",bg="lightblue",font="billyargel 15 bold",width=30,command=harvesting).place(x=20,y=470)

b=Button(top,text="crop suggestion",font="arial 15 bold",width=20,bg="lightblue",command=crop).place(x=120,y=570)
b=Button(top,text="fertilizers ",font="arial 15 bold",width=20,bg="lightblue",command=fertilizer).place(x=490,y=570)
b=Button(top,text="pesticides",font="arial 15 bold",width=20,bg="lightblue",command=pesticide).place(x=830,y=570)

b=Button(top,text="crop market",font="arial 15 bold",width=20,bg="lightblue",command=cropmarket).place(x=1150,y=570)
b=Button(top,text="modern techniques",font="arial 15 bold",width=20,bg="lightblue",command=modern).place(x=650,y=670)

top.mainloop()

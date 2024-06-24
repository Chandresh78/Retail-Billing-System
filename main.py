from tkinter import *  #tkinter is used for GUI
from tkinter import messagebox  #for showing message box if any error occurs
import random, os, tempfile, smtplib

### Functionality Part


#Clear Button
def clear():
    bathsoapEntry.delete(0,0)
    facecreamEntry.delete(0,0)
    hairgelEntry.delete(0,0)
    hairsprayEntry.delete(0,0)
    bodylotionEntry.delete(0,0)
    facewashEntry.delete(0,0)

    dalEntry.delete(0,0)
    wheatEntry.delete(0,0)
    riceEntry.delete(0,0)
    oilEntry.delete(0,0)
    SugarEntry.delete(0,0)
    TeaEntry.delete(0,0)

    maazaEntry.delete(0,0)
    pepsiEntry.delete(0,0)
    dewEntry.delete(0,0)
    spriteEntry.delete(0,0)
    frootiEntry.delete(0,0)
    cocacolaEntry.delete(0,0)



    bathsoapEntry.insert(0,0)
    facecreamEntry.insert(0,0)
    hairgelEntry.insert(0,0)
    hairsprayEntry.insert(0,0)
    bodylotionEntry.insert(0,0)
    facewashEntry.insert(0,0)

    dalEntry.insert(0,0)
    wheatEntry.insert(0,0)
    riceEntry.insert(0,0)
    oilEntry.insert(0,0)
    SugarEntry.insert(0,0)
    TeaEntry.insert(0,0)

    maazaEntry.insert(0,0)
    pepsiEntry.insert(0,0)
    dewEntry.insert(0,0)
    spriteEntry.insert(0,0)
    frootiEntry.insert(0,0)
    cocacolaEntry.insert(0,0)

    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    billnumberEntry.delete(0,END)

    textarea.delete(1.0,END)


#Printing the bill
def print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is Empty')
    else:
        file = tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')

#Sending Mail
def send_email():
 def send_gmail():
    try:
         ob = smtplib.SMTP('smtp.gmail.com',587)
         ob.starttls()
         ob.login(senderEntry.get(),passwordEntry.get())
         message = email_textarea.get(1.0,END)
         ob.sendmail(senderEntry.get(), receiverEntry.get(),message)
         ob.quit()
         messagebox.showinfo('Success','Bill is successfully sent',parent=root1)
         root1.destroy()
    except:
        messagebox.showerror('Error','Something went wrong, Please try again',parent=root1)

    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is Empty')
    else:
        root1=Toplevel()
        root1.grab_set()
        root1.title('Send Mail')
        root1.config(bg = 'gray20')
        root1.resizable(0,0)
        root1.mainloop()

        senderFrame = LabelFrame(root1,text='SENDER',FONT=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
        senderFrame.grid(row=0,column=0,padx=40,pady=20)

        senderLabel = Label(senderFrame,text="Sender's Email",font=('arial',14,'bold'),bg='gray20',fg='white')
        senderLabel.grid(row=0,coloumn=0,padx=10,pady=8)

        senderEntry = Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        senderEntry.grid(row=0,coloumn=1,padx=10,pady=8)

        passwordLabel = Label(senderFrame,text="Password",font=('arial',14,'bold'),bg='gray20',fg='white')
        passwordLabel.grid(row=1,coloumn=0,padx=10,pady=8)

        passwordEntry = Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE,show='*')
        passwordEntry.grid(row=1,coloumn=1,padx=10,pady=8)

        recipientFrame = LabelFrame(root1,text='RECIPIENT',FONT=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
        recipientFrame.grid(row=1,column=0,padx=40,pady=20)

        receiverLabel = Label(recipientFrame,text="E-mail Address",font=('arial',14,'bold'),bg='gray20',fg='white')
        receiverLabel.grid(row=0,coloumn=0,padx=10,pady=8)

        receiverEntry = Entry(recipientFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        receiverEntry.grid(row=0,coloumn=1,padx=10,pady=8)

        messageLabel = Label(recipientFrame,text="Message",font=('arial',14,'bold'),bg='gray20',fg='white')
        messageLabel.grid(row=1,coloumn=0,padx=10,pady=8)

        email_textarea = Text(recipientFrame,font=('arial',14,'bold'),bd=2,relief=SUNKEN,
                              width = 42, height = 11)
        email_textarea.grid(row=2,coloumn=0,columnspan=2)
        email_textarea.delete(1.0,END)
        email_textarea.insert(END,textarea.get(1.0,END).replace('=','').replace('-','').replace('\t\t\t','\t\t'))


        sendButton = Button(root1,text = 'SEND',font=('arial',16,'bold'),width=15,command = send_gmail)
        sendButton.grid(row=2,coloumn=0,pady=20)











def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0]==billnumberEntry.get():
            f = open(f'bills/{i}','r')
            textarea.delete(1.0,END)
            for data in f:
                textarea.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror('Error','Invalid Bill Number')



if not os.path.exists('bills'):
    os.makedirs('bills')

def save_bill():
    global billnumber
    result = messagebox.askyesno('Confirm','Do you want to save the bill?')
    if result:
        bill_content = textarea(1.0,END)
        file = open(f'bills/{billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'Bill Number {billnumber} is saved successfully')
        billnumber = random.randint(500,1000)



billnumber = random.randint(500,1000)
def bill_area():
    #textarea.delete(1.0,END)
    if nameEntry.get()== '' or phoneEntry.get()=='':
        messagebox.showerror('Error','Customer details are required')
    elif cosmeticpriceEntry.get()=='' and grocerypriceEntry.get()=='' and drinkspriceEntry.get()=='':
        messagebox.showerror('Error','No Products are selected')
    elif cosmeticpriceEntry.get()=='0 Rs' and grocerypriceEntry.get()=='0 Rs' and drinkspriceEntry.get()=='0 Rs':
        messagebox.showerror('Error','No Products are selected')
    else:
        textarea.insert(END,'\t\t**Welcome Customer\n**')
        textarea.insert(END,f'\nBill Number: {billnumber}\n')
        textarea.insert(END,f'\nCustomer Name: {nameEntry.get()}\n')
        textarea.insert(END,f'\nCustomer Phone Number: {phoneEntry.get()}\n')
        textarea.insert(END,'\n==================================================')
        textarea.insert(END,'Product\t\t\tQuantity\t\t\tPrice')
        textarea.insert(END,'\n===================================================')
        if bathsoapEntry.get()!=0:
            textarea.insert(END,f'\nBath Soap\t\t\t{bathsoapEntry.get()}\t\t\t{soapprice} Rs')
        if hairsprayEntry.get()!=0:
            textarea.insert(END,f'\nHair Spray\t\t\t{hairsprayEntry.get()}\t\t\t{hairsprayprice} Rs')
        if hairgelEntry.get()!=0:
            textarea.insert(END,f'\nHair Gel\t\t\t{hairgelEntry.get()}\t\t\t{hairgelprice} Rs')
        if facecreamEntry.get()!=0:
            textarea.insert(END,f'\nFace Cream\t\t\t{facecreamEntry.get()}\t\t\t{facecreamprice} Rs')
        if facewashEntry.get()!=0:
            textarea.insert(END,f'\nFace Wash\t\t\t{facewashEntry.get()}\t\t\t{facewashprice} Rs')
        
        if riceEntry.get()!=0:
            textarea.insert(f'\nRice\t\t\t{riceEntry.get()}\t\t\t{riceprice} Rs')
        if oilEntry.get()!=0:
            textarea.insert(f'\nOil\t\t\t{oilEntry.get()}\t\t\t{oilprice} Rs')
        if dalEntry.get()!=0:
            textarea.insert(f'\nDal\t\t\t{dalEntry.get()}\t\t\t{dalprice} Rs')
        if wheatEntry.get()!=0:
            textarea.insert(f'\nWheat\t\t\t{wheatEntry.get()}\t\t\t{wheatprice} Rs')
        if SugarEntry.get()!=0:
            textarea.insert(f'\nSugar\t\t\t{SugarEntry.get()}\t\t\t{sugarprice} Rs')
        if TeaEntry.get()!=0:
            textarea.insert(f'\nTea\t\t\t{TeaEntry.get()}\t\t\t{teaprice} Rs')
        
        if maazaEntry.get()!=0:
            textarea.insert(END,f'\nMaaza\t\t\t{maazaEntry.get()}\t\t\t{maazaprice} Rs')
        if frootiEntry.get()!=0:
            textarea.insert(END,f'\nFrooti\t\t\t{frootiEntry.get()}\t\t\t{frootiprice} Rs')
        if spriteEntry.get()!=0:
            textarea.insert(END,f'\nSprite\t\t\t{spriteEntry.get()}\t\t\t{spriteprice} Rs')
        if cocacolaEntry.get()!=0:
            textarea.insert(END,f'\nCoca Cola\t\t\t{cocacolaEntry.get()}\t\t\t{cocacolaprice} Rs')
        if pepsiEntry.get()!=0:
            textarea.insert(END,f'\nPepsi\t\t\t{pepsiEntry.get()}\t\t\t{pepsiprice} Rs')
        if dewEntry.get()!=0:
            textarea.insert(END,f'\nDew\t\t\t{dewEntry.get()}\t\t\t{dewprice} Rs')
        textarea.insert(END,'\n-------------------------------------------------------')

        if cosmetictaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\nCosmetic Tax\t\t\t{cosmetictaxEntry.get()}')
        if grocerytaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\nGrocery Tax\t\t\t{grocerytaxEntry.get()}')
        if drinkstaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\nDrinks Tax\t\t\t{drinkstaxEntry.get()}')








    



def total():
    #cosmetic price calculation (12 % tax)
    global totalbill
    global soapprice
    global facecreamprice
    global hairgelprice
    global facewashprice
    global hairsprayprice
    global bodylotionprice
    soapprice = int(bathsoapEntry.get())*20
    facecreamprice = int(facecreamEntry.get())*50
    facewashprice = int(facewashEntry.get())*100
    hairsprayprice = int(hairsprayEntry.get())*150
    hairgelprice = int(hairgelEntry.get())*80
    bodylotionprice = int(bodylotionEntry.get())*60

    totalcosmeticprice = soapprice+facecreamprice+facewashprice+hairsprayprice+hairgelprice+bodylotionprice
    cosmeticpriceEntry.delete(0,END)
    cosmeticpriceEntry.insert(0,f'{totalcosmeticprice} Rs')
    cosmetictax = totalcosmeticprice*0.12
    cosmetictaxEntry.delete(0,END)
    cosmetictaxEntry.insert(0,f'{cosmetictax} Rs')

    #grocery price calculation (5 % tax)
    global riceprice
    global oilprice
    global dalprice
    global wheatprice
    global sugarprice
    global teaprice
    riceprice = int(riceEntry.get())*30
    oilprice = int(oilEntry.get())*100
    dalprice = int(dalEntry.get())*120
    wheatprice = int(wheatEntry.get())*50
    sugarprice = int(SugarEntry.get())*140
    teaprice = int(TeaEntry.get())*80
    
    totalgroceryprice = riceprice+oilprice+dalprice+wheatprice+sugarprice+teaprice
    grocerypriceEntry.delete(0,END)
    grocerypriceEntry.insert(0,f'{totalgroceryprice} Rs')
    grocerytax = totalgroceryprice*0.05
    grocerytaxEntry.delete(0,END)
    grocerytaxEntry.insert(0,f'{grocerytax} Rs')

    #cold drink price calculation (8 % tax)
    global maazaprice
    global frootiprice
    global dewprice
    global pepsiprice
    global spriteprice
    global cocacolaprice
    maazaprice = int(maazaEntry.get()) * 50
    frootiprice = int(frootiEntry.get()) * 20
    dewprice = int(dewEntry.get()) * 30
    pepsiprice = int(pepsiEntry.get()) * 20
    spriteprice = int(spriteEntry.get()) * 45
    cocacolaprice = int(cocacolaEntry.get()) * 90

    totaldrinksprice = maazaprice+frootiprice+dewprice+pepsiprice+spriteprice+cocacolaprice
    drinkspriceEntry.delete(0,END)
    drinkspriceEntry.insert(0,f'{totaldrinksprice} Rs')
    drinkstax = totaldrinksprice*0.08
    drinkstaxEntry.delete(0,END)
    drinkstaxEntry.insert(0,f'{drinkstax} Rs')

    totalbill = totalcosmeticprice+totalgroceryprice+totaldrinksprice+cosmetictax+grocerytax+drinkstax


#GUI Part
root = Tk()
root.title('Retail Billing System')
root.geometry('1270x685')
root.iconbitmap('icon.ico') #always use 'ico' file
headingLabel = Label(root,text='Retail Billing System',font=('times new roman', 30, 'bold')
                     ,bg='gray20',fg='gold',bd=12,relief=GROOVE)
headingLabel.pack(fill=X)

customer_details_frame = LabelFrame(root,text='Customer Details',font=('times new roman',15,'bold'),fg='gold'
                                    ,bd=8,relief=GROOVE,bg='gray20')
customer_details_frame.pack(fill=X)
###
nameLabel = Label(customer_details_frame,text='Name',font=('times new roman',15,'bold'),
                  bg='gray20',fg='white')
nameLabel.grid(row=0,column=0,padx=20)

nameEntry = Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)
###
phoneLabel = Label(customer_details_frame,text='Phone Number',font=('times new roman',15,'bold'),
                  bg='gray20',fg='white')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)

phoneEntry = Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
phoneEntry.grid(row=0,column=3,padx=8)
###
billnumberLabel = Label(customer_details_frame,text='Bill Number',font=('times new roman',15,'bold'),
                  bg='gray20',fg='white')
billnumberLabel.grid(row=0,column=4,padx=20,pady=2)

billnumberEntry = Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
billnumberEntry.grid(row=0,column=5,padx=8)

searchButton = Button(customer_details_frame,text='SEARCH',font=('arial',12,'bold'),
                      bd=7,width=10, command = search_bill)
searchButton.grid(row=0,column=6,padx=20,pady=8)

#Prducts FRAME
productsFrame=Frame(root)
productsFrame.pack()

cosmeticFrame = LabelFrame(productsFrame,text='Cosmetics',font=('times new roman',15,'bold'),fg='gold'
                                    ,bd=8,relief=GROOVE,bg='gray20')
cosmeticFrame.grid(row=0,column=0)
###
bathsoapLabel = Label(cosmeticFrame,text='Bath Soap',font=('times new roman',15,'bold'),
                  bg='gray20',fg='white')
bathsoapLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
bathsoapEntry = Entry(cosmeticFrame,font=('times new roman',15,'bold'),
                  width=10,bd=5)
bathsoapEntry.grid(row=0,column=1,pady=9,padx=10)
bathsoapEntry.insert(0,0)
###
facecreamLabel = Label(cosmeticFrame,text='Face Cream',font=('times new roman',15,'bold'),
                  bg='gray20',fg='white')
facecreamLabel.grid(row=1,column=0,pady=9,padx=10)
facecreamEntry = Entry(cosmeticFrame,font=('times new roman',15,'bold'),
                  width=10,bd=5)
facecreamEntry.grid(row=1,column=1,pady=9,padx=10,sticky='w')
facecreamEntry.insert(0,0)
###
facewashLabel = Label(cosmeticFrame,text='Face Wash',font=('times new roman',15,'bold'),
                  bg='gray20',fg='white')
facewashLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
facewashEntry = Entry(cosmeticFrame,font=('times new roman',15,'bold'),
                  width=10,bd=5)
facewashEntry.grid(row=2,column=1,pady=9,padx=10)
facewashEntry.insert(0,0)
###
hairsprayLabel = Label(cosmeticFrame,text='Hair Spray',font=('times new roman',15,'bold'),
                  bg='gray20',fg='white')
hairsprayLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
hairsprayEntry = Entry(cosmeticFrame,font=('times new roman',15,'bold'),
                  width=10,bd=5)
hairsprayEntry.grid(row=3,column=1,pady=9,padx=10)
hairsprayEntry.insert(0,0)
###
hairgelLabel = Label(cosmeticFrame,text='Hair Gel',font=('times new roman',15,'bold'),
                  bg='gray20',fg='white')
hairgelLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
hairgelEntry = Entry(cosmeticFrame,font=('times new roman',15,'bold'),
                  width=10,bd=5)
hairgelEntry.grid(row=4,column=1,pady=9,padx=10)
hairgelEntry.insert(0,0)
###
bodylotionLabel = Label(cosmeticFrame,text='Body Lotion',font=('times new roman',15,'bold'),
                  bg='gray20',fg='white')
bodylotionLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')
bodylotionEntry = Entry(cosmeticFrame,font=('times new roman',15,'bold'),
                  width=10,bd=5)
bodylotionEntry.grid(row=5,column=1,pady=9,padx=10)
bodylotionEntry.insert(0,0)

#Grocery FRAME
groceryFrame = LabelFrame(productsFrame,text='Grocery',font=('times new roman',15,'bold'),fg='gold'
                                    ,bd=8,relief=GROOVE,bg='gray20')
groceryFrame.grid(row=0,column=1)
#
riceLabel = Label(groceryFrame,text='Rice',font=('times new roman',15,'bold'),
                  bg='gray20',fg='white')
riceLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

riceEntry = Entry(groceryFrame,font=('times new roman',15,'bold'),
                  width=10,bd=5)
riceEntry.grid(row=0,column=1,pady=9,padx=10)
riceEntry.insert(0,0)
#
oilLabel = Label(groceryFrame,text='Oil',font=('times new roman',15,'bold'),
                  bg='gray20',fg='white')
oilLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

oilEntry = Entry(groceryFrame,font=('times new roman',15,'bold'),
                  width=10,bd=5)
oilEntry.grid(row=1,column=1,pady=9,padx=10)
oilEntry.insert(0,0)
#
dalLabel = Label(groceryFrame,text='Dal',font=('times new roman',15,'bold'),
                  bg='gray20',fg='white')
dalLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

dalEntry = Entry(groceryFrame,font=('times new roman',15,'bold'),
                  width=10,bd=5)
dalEntry.grid(row=2,column=1,pady=9,padx=10)
dalEntry.insert(0,0)
#
wheatLabel = Label(groceryFrame,text='Wheat',font=('times new roman',15,'bold'),
                  bg='gray20',fg='white')
wheatLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

wheatEntry = Entry(groceryFrame,font=('times new roman',15,'bold'),
                  width=10,bd=5)
wheatEntry.grid(row=3,column=1,pady=9,padx=10)
wheatEntry.insert(0,0)
#
SugarLabel = Label(groceryFrame,text='Sugar',font=('times new roman',15,'bold'),
                  bg='gray20',fg='white')
SugarLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

SugarEntry = Entry(groceryFrame,font=('times new roman',15,'bold'),
                  width=10,bd=5)
SugarEntry.grid(row=4,column=1,pady=9,padx=10)
SugarEntry.insert(0,0)
#
TeaLabel = Label(groceryFrame,text='Tea',font=('times new roman',15,'bold'),
                  bg='gray20',fg='white')
TeaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

TeaEntry = Entry(groceryFrame,font=('times new roman',15,'bold'),
                  width=10,bd=5)
TeaEntry.grid(row=5,column=1,pady=9,padx=10)
TeaEntry.insert(0,0)

#Cold Drink FRAME
drinksFrame = LabelFrame(productsFrame,text='Cold Drinks',font=('times new roman',15,'bold'),fg='gold'
                                    ,bd=8,relief=GROOVE,bg='gray20')
drinksFrame.grid(row=0,column=2)
#
maazaLabel = Label(drinksFrame,text='Maaza',font=('times new roman',15,'bold'),
                  bg='gray20',fg='white')
maazaLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

maazaEntry = Entry(drinksFrame,font=('times new roman',15,'bold'),
                  width=10,bd=5)
maazaEntry.grid(row=0,column=1,pady=9,padx=10)
maazaEntry.insert(0,0)
#
pepsiLabel = Label(drinksFrame,text='Pepsi',font=('times new roman',15,'bold'),
                  bg='gray20',fg='white')
pepsiLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

pepsiEntry = Entry(drinksFrame,font=('times new roman',15,'bold'),
                  width=10,bd=5)
pepsiEntry.grid(row=1,column=1,pady=9,padx=10)
pepsiEntry.insert(0,0)
#
spriteLabel = Label(drinksFrame,text='Sprite',font=('times new roman',15,'bold'),
                  bg='gray20',fg='white')
spriteLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

spriteEntry = Entry(drinksFrame,font=('times new roman',15,'bold'),
                  width=10,bd=5)
spriteEntry.grid(row=2,column=1,pady=9,padx=10)
spriteEntry.insert(0,0)
#
dewLabel = Label(drinksFrame,text='Dew',font=('times new roman',15,'bold'),
                  bg='gray20',fg='white')
dewLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

dewEntry = Entry(drinksFrame,font=('times new roman',15,'bold'),
                  width=10,bd=5)
dewEntry.grid(row=3,column=1,pady=9,padx=10)
dewEntry.insert(0,0)
#
frootiLabel = Label(drinksFrame,text='Frooti',font=('times new roman',15,'bold'),
                  bg='gray20',fg='white')
frootiLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

frootiEntry = Entry(drinksFrame,font=('times new roman',15,'bold'),
                  width=10,bd=5)
frootiEntry.grid(row=4,column=1,pady=9,padx=10)
frootiEntry.insert(0,0)
#
cocacolaLabel = Label(drinksFrame,text='Coca Cola',font=('times new roman',15,'bold'),
                  bg='gray20',fg='white')
cocacolaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

cocacolaEntry = Entry(drinksFrame,font=('times new roman',15,'bold'),
                  width=10,bd=5)
cocacolaEntry.grid(row=5,column=1,pady=9,padx=10)
cocacolaEntry.insert(0,0)

#Bill Frame
billframe = Frame(productsFrame,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3,padx=10)

billareaLabel = Label(billframe, text='Bill Area',font=('times new roman',15,'bold')
                      ,bd=7,relief=GROOVE)
billareaLabel.pack(fill=X)

scrollbar = Scrollbar(billframe,orient=VERTICAL)   #Scroll Bar
scrollbar.pack(side=RIGHT,fill=Y)

textarea = Text(billframe,height=18, width=55, yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

#Bill Menu Frame
billmenuFrame = LabelFrame(productsFrame,text='Bill Menu',font=('times new roman',15,'bold'),fg='gold'
                                    ,bd=8,relief=GROOVE,bg='gray20')
billmenuFrame.grid()

#
cosmeticpriceLabel = Label(billmenuFrame,text='Cosmetic Price',font=('times new roman',14,'bold'),
                  bg='gray20',fg='white')
cosmeticpriceLabel.grid(row=0,column=0,pady=6,padx=10,sticky='w')
cosmeticpriceEntry = Entry(billmenuFrame,font=('times new roman',14,'bold'),
                  width=10,bd=5)
cosmeticpriceEntry.grid(row=0,column=1,pady=6,padx=10)
#
grocerypriceLabel = Label(billmenuFrame,text='Grocery Price',font=('times new roman',14,'bold'),
                  bg='gray20',fg='white')
grocerypriceLabel.grid(row=0,column=0,pady=6,padx=10,sticky='w')
grocerypriceEntry = Entry(billmenuFrame,font=('times new roman',14,'bold'),
                  width=10,bd=5)
grocerypriceEntry.grid(row=1,column=1,pady=6,padx=10)
#
drinkspriceLabel = Label(billmenuFrame,text='Cold Drink Price',font=('times new roman',14,'bold'),
                  bg='gray20',fg='white')
drinkspriceLabel.grid(row=2,column=0,pady=6,padx=10,sticky='w')
drinkspriceEntry = Entry(billmenuFrame,font=('times new roman',14,'bold'),
                  width=10,bd=5)
drinkspriceEntry.grid(row=1,column=1,pady=6,padx=10)

#############################
cosmetictaxLabel = Label(billmenuFrame,text='Cosmetic Tax',font=('times new roman',14,'bold'),
                  bg='gray20',fg='white')
cosmetictaxLabel.grid(row=0,column=2,pady=6,padx=10,sticky='w')

cosmetictaxEntry = Entry(billmenuFrame,font=('times new roman',14,'bold'),
                  width=10,bd=5)
cosmetictaxEntry.grid(row=0,column=3,pady=6,padx=10)
#
grocerytaxLabel = Label(billmenuFrame,text='Grocery Tax',font=('times new roman',14,'bold'),
                  bg='gray20',fg='white')
grocerytaxLabel.grid(row=1,column=2,pady=6,padx=10,sticky='w')
grocerytaxEntry = Entry(billmenuFrame,font=('times new roman',14,'bold'),
                  width=10,bd=5)
grocerytaxEntry.grid(row=1,column=3,pady=6,padx=10)
#
drinkstaxLabel = Label(billmenuFrame,text='Cold Drink Tax',font=('times new roman',14,'bold'),
                  bg='gray20',fg='white')
drinkstaxLabel.grid(row=2,column=2,pady=6,padx=10,sticky='w')
drinkstaxEntry = Entry(billmenuFrame,font=('times new roman',14,'bold'),
                  width=10,bd=5)
drinkstaxEntry.grid(row=2,column=3,pady=6,padx=10)


#Button Frame
buttonFrame = Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)
#Total Button
totalButton = Button(buttonFrame,text='Total',font=('arial',16,'bold'),
                     bg='gray20',fg='white',bd=5,width=8,pady=10,command=total)
totalButton.grid(row=0,column=0,padx=5,pady=20)
#Bill Button
billButton = Button(buttonFrame,text='Bill',font=('arial',16,'bold'),
                     bg='gray20',fg='white',bd=5,width=8,pady=10,command =bill_area)
billButton.grid(row=0,column=1,padx=5,pady=20)
#Email Button
emailButton = Button(buttonFrame,text='E-mail',font=('arial',16,'bold'),
                     bg='gray20',fg='white',bd=5,width=8,pady=10, command = send_email)
emailButton.grid(row=0,column=2,padx=5,pady=20)
#Print Button
printButton = Button(buttonFrame,text='Print',font=('arial',16,'bold'),
                     bg='gray20',fg='white',bd=5,width=8,pady=10, command = print_bill)
printButton.grid(row=0,column=3,padx=5,pady=20)
#Clear Button
clearButton = Button(buttonFrame,text='Clear',font=('arial',16,'bold'),
                     bg='gray20',fg='white',bd=5,width=8,pady=10)
clearButton.grid(row=0,column=4,padx=5,pady=20)










root.mainloop()  #window will be shown 
import tkinter as tk
from tkinter import ttk
from tkinter import*
from PIL import Image, ImageTk
import random
from datetime import date
from datetime import datetime
from tkinter import messagebox


prices = {
    "Chocolate Ice Cream": 3,
    "Vanilla Ice Cream": 3,
    "Swirl Ice Cream": 4,
    "Butterscotch Ice Cream": 4,
    "Cheesecake Ice Cream": 4,
    "Moosetrack Ice Cream": 5,
}


root = Tk()

root.title("TTC-Ice Cream Shop")

#------------FUNCTIONS----------#

messagebox.showinfo("Ice Cream Shop", "Welcome, thank you for shopping!")

# Random Order ID
def ORDER_ID():
    numbers = [0,1,2,3,4,5,6,7,8,9]
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
               'P','Q','R','S','T','U','V','W','X','Y','Z']
    order_id = "ICS_"
    random_letters = ""
    random_digits = ""
    for i in range(0,3):
        random_letters += random.choice(letters)
        random_digits += str(random.choice(numbers))

    order_id += random_letters + random_digits
    return order_id


#Region Add to Order Button
def add():
    #Updating transaction label
    current_order = orderTransaction.cget("text")
    added_dish = displayLabel.cget("text") + "--" + str(prices[displayLabel.cget("text")]) + "$"
    updated_order = current_order + added_dish
    orderTransaction.configure(text=updated_order)

    #Updating Order Total Label
    order_total = orderTotalLabel.cget("text").replace("TOTAL:","")
    order_total = order_total.replace("$","")
    updated_total = int(order_total) + prices[displayLabel.cget("text")]
    orderTotalLabel.configure(text="TOTAL:" + str(updated_total) + "$")

#Region Remove Button Function
def remove():
    dish_to_remove=displayLabel.cget("text")+"--"+str(prices[displayLabel.cget("text")])
    transaction_list=orderTransaction.cget("text").split("$ ")
    transaction_list.pop(len(transaction_list)- 1)

    if dish_to_remove in transaction_list:
        #update transaction label
        transaction_list.remove(dish_to_remove)
        updated_order=""
        for item in transaction_list:
            updated_order+=item+"$ "

        orderTransaction.configure(text=updated_order)

        #update transaction total
        order_total=orderTotalLabel.cget("text").replace("TOTAL : " ,"")
        order_total=order_total.replace("$", "")
        updated_total=int(order_total)-prices[displayLabel.cget("text")]
        orderTotalLabel.configure(text="TOTAL:"+str(updated_total)+"$")

#Display Button Functions
def displayChocolate():
    ChocolateDishFrame.configure(
        relief="sunken",
        style="SelectedDish.TFrame"
    )
    VanillaDishFrame.configure(style="DishFrame.TFrame")
    SwirlDishFrame.configure(style="DishFrame.TFrame")
    CheesecakeDishFrame.configure(style="DishFrame.TFrame")
    MoosetrackDishFrame.configure(style="DishFrame.TFrame")
    displayLabel.configure(
        image=ChocolateImage,
        text="Chocolate Ice Cream",
        font=('Helvetica', 14, "bold"),
        foreground="white",
        compound="bottom",
        padding=(5,5,5,5),
    )

def displayVanilla():
    VanillaDishFrame.configure(
        relief="sunken",
        style="SelectedDish.TFrame"
    )
    ChocolateDishFrame.configure(style="DishFrame.TFrame")
    SwirlDishFrame.configure(style="DishFrame.TFrame")
    CheesecakeDishFrame.configure(style="DishFrame.TFrame")
    MoosetrackDishFrame.configure(style="DishFrame.TFrame")
    displayLabel.configure(
        image=VanillaImage,
        text="Vanilla Ice Cream",
        font=('Helvetica', 14, "bold"),
        foreground="white",
        compound="bottom",
        padding=(5,5,5,5),
    )

def displaySwirl():
    SwirlDishFrame.configure(
        relief="sunken",
        style="SelectedDish.TFrame"
    )
    ChocolateDishFrame.configure(style="DishFrame.TFrame")
    VanillaDishFrame.configure(style="DishFrame.TFrame")
    CheesecakeDishFrame.configure(style="DishFrame.TFrame")
    MoosetrackDishFrame.configure(style="DishFrame.TFrame")
    displayLabel.configure(
        image=SwirlImage,
        text="Swirl Ice Cream",
        font=('Helvetica', 14, "bold"),
        foreground="white",
        compound="bottom",
        padding=(5,5,5,5),
    )

def displayButterscotch():
    ButterscotchDishFrame.configure(
        relief="sunken",
        style="SelectedDish.TFrame"
    )
    ChocolateDishFrame.configure(style="DishFrame.TFrame")
    VanillaDishFrame.configure(style="DishFrame.TFrame")
    SwirlDishFrame.configure(style="DishFrame.TFrame")
    CheesecakeDishFrame.configure(style="DishFrame.TFrame")
    MoosetrackDishFrame.configure(style="DishFrame.TFrame")

    displayLabel.configure(
        image=ButterscotchImage,
        text="Butterscotch Ice Cream",
        font=('Helvetica', 14, "bold"),
        foreground="white",
        compound="bottom",
        padding=(5,5,5,5),
    )

def displayCheesecake():
    CheesecakeDishFrame.configure(
        relief="sunken",
        style="SelectedDish.TFrame"
    )
    ChocolateDishFrame.configure(style="DishFrame.TFrame")
    VanillaDishFrame.configure(style="DishFrame.TFrame")
    SwirlDishFrame.configure(style="DishFrame.TFrame")
    MoosetrackDishFrame.configure(style="DishFrame.TFrame")
    displayLabel.configure(
        image=CheesecakeImage,
        text="Cheesecake Ice Cream",
        font=('Helvetica', 14, "bold"),
        foreground="white",
        compound="bottom",
        padding=(5,5,5,5),
    )

def displayMoosetrack():
    MoosetrackDishFrame.configure(
        relief="sunken",
        style="SelectedDish.TFrame"
    )
    ChocolateDishFrame.configure(style="DishFrame.TFrame")
    VanillaDishFrame.configure(style="DishFrame.TFrame")
    SwirlDishFrame.configure(style="DishFrame.TFrame")
    CheesecakeDishFrame.configure(style="DishFrame.TFrame")
    displayLabel.configure(
        image=MoosetrackImage,
        text="Moosetrack Ice Cream",
        font=('Helvetica', 14, "bold"),
        foreground="white",
        compound="bottom",
        padding=(5,5,5,5),
    )

#Region Generates Reciepts from Order Button
def order():
    new_receipt = orderIDLabel.cget("text")
    new_receipt = new_receipt.replace("ORDER_ID : ","")
    transaction_list = orderTransaction.cget("text").split("$")
    transaction_list.pop(len(transaction_list)-1)

    order_day = data.today()
    order_time = data.now()

    for item in transaction_list:
        item += "$ "

    with open(new_receipt, 'w') as file:
        file.write("Ice Cream Shop")
        file.write("\n")
        file.write("----------------------------")
        file.write("\n")
        file.write(order_day.strftime("%x"))
        file.write("\n")
        file.write(order.time.strftime("%x"))
        file.write("\n\n")
        for item in transaction_list:
            file.write(item + "\n")
        file.write("\n\n")
        file.write(orderTotalLabel.cget("text"))

    orderTotalLabel.configure(text ="TOTAL:$0")
    orderIDLabel.configure(text = "ORDER ID:" + ORDER_ID())
    orderTransaction.configure(text = "")

#endregion


#---------- STYLING AND IMAGES ----------#
#region style configurations

s=ttk.Style()
s.configure('MainFrame.TFrame', background= "#F8F8FF")
s.configure('MenuFrame.TFrame', background= "#F8F8FF")
s.configure('DisplayFrame.TFrame', background="#9AC0CD")
s.configure('OrderFrame.Tfram',background="#B7C4CF")
s.configure('DishFrame.TFrame', background="#F8F8FF", relief="raised")
s.configure('SelectedDish.TFrame', background="#C4DFAA")
s.configure('MenuLabel.TLabel',
           background="#9AC0CD",
           font=("Arial", 13, "italic"),
           foreground="white",
           padding=(5,5,5,5),
           width=21
           )

s.configure('orderTotalLabel.TLabel',
           background="#9AC0CD",
           font=("Arial", 10, "bold"),
           foreground="white",
           padding=(2,2,2,2),
           anchor="W"
           )

s.configure('orderTransaction.TLabel',
           background="#F8F8FF",
           font=("Helvetica", 12),
           foreground="black",
           wraplength=170,
           padding=(3,3,3,3),
           anchor="NW"
           )


#end region

#region Images
#Top Banner Images

LogoImageObject = Image.open("menu/logo.jpg").resize((200, 200))
LogoImage=ImageTk.PhotoImage(LogoImageObject)

TopBannerImageObject=Image.open("menu/banner.jpg").resize((800, 200))
TopBannerImage = ImageTk.PhotoImage(TopBannerImageObject)


#Menu Images
displayDefaultImageObject=Image.open(r'C:\Users\joco1\PycharmProjects\pythonProject11\menu\love.jpg').resize((350, 360))
displayDefaultImageObject=ImageTk.PhotoImage(displayDefaultImageObject)

ChocolateImageObject=Image.open(r'C:\Users\joco1\PycharmProjects\pythonProject11\menu\Chocolate.jpg').resize((350, 334))
ChocolateImage=ImageTk.PhotoImage(ChocolateImageObject)

VanillaImageObject=Image.open(r'C:\Users\joco1\PycharmProjects\pythonProject11\menu\Vanilla.jpg').resize((350, 334))
VanillaImage=ImageTk.PhotoImage(VanillaImageObject)

SwirlImageObject=Image.open(r'C:\Users\joco1\PycharmProjects\pythonProject11\menu\Swirl.png').resize((350, 334))
SwirlImage=ImageTk.PhotoImage(SwirlImageObject)

ButterscotchImageObject=Image.open(r'C:\Users\joco1\PycharmProjects\pythonProject11\menu\Butterscotch.jpg').resize((350, 334))
ButterscotchImage=ImageTk.PhotoImage(ButterscotchImageObject)

CheesecakeImageObject=Image.open(r'C:\Users\joco1\PycharmProjects\pythonProject11\menu\Cheesecake.jpg').resize((350, 334))
CheesecakeImage=ImageTk.PhotoImage(CheesecakeImageObject)

MoosetrackImageObject=Image.open(r'C:\Users\joco1\PycharmProjects\pythonProject11\menu\Moosetrack.jpg').resize((350, 334))
MoosetrackImage=ImageTk.PhotoImage(MoosetrackImageObject)

#endregion

#------------- WIDGETS ---------------#

#region Frames
# Section Frames

mainFrame=ttk.Frame(root, width=800, height=580, style='MainFrame.TFrame')
mainFrame.grid(row=0, column=0, sticky="NSEW")

topBannerFrame= ttk.Frame(mainFrame)
topBannerFrame.grid(row=0, column=0, sticky="NSEW", columnspan=3)

menuFrame=ttk.Frame(mainFrame, style='MenuFrame.TFrame')
menuFrame.grid(row=1, column=0, padx=3, pady=3, sticky="NSEW")

displayFrame = ttk.Frame(mainFrame, style="Displayframe.TFrame")
displayFrame.grid(row=1, column=1, padx=3, pady=3, sticky="NSEW")

orderFrame = ttk.Frame(mainFrame, style ="OrderFrame.TFrame")
orderFrame.grid(row=1, column =2, padx=3, pady=3, sticky="NSEW")

#Dish Frames
ChocolateDishFrame=ttk.Frame(menuFrame, style = "DishFrame.TFrame")
ChocolateDishFrame.grid(row=1, column=0, sticky="NSEW")

VanillaDishFrame=ttk.Frame(menuFrame, style="DishFrame.TFrame")
VanillaDishFrame.grid(row=2, column=0, sticky="NSEW")

SwirlDishFrame=ttk.Frame(menuFrame, style="DishFrame.TFrame")
SwirlDishFrame.grid(row=3, column=0, sticky="NSEW")

ButterscotchDishFrame=ttk.Frame(menuFrame, style="DishFrame.TFrame")
ButterscotchDishFrame.grid(row=4, column=0, sticky="NSEW")

CheesecakeDishFrame=ttk.Frame(menuFrame, style="DishFrame.TFrame")
CheesecakeDishFrame.grid(row=5, column=0, sticky="NSEW")

MoosetrackDishFrame=ttk.Frame(menuFrame, style="DishFrame.TFrame")
MoosetrackDishFrame.grid(row=6, column=0, sticky="NSEW")


#endregion

#Top Banner Images

LogoLabel= tk.Label(topBannerFrame, image=LogoImage, background= "#9AC0CD")
LogoLabel.grid(row=0, column=0, sticky="W")

RestaurantBannerLabel= ttk.Label(topBannerFrame, image=TopBannerImage, background ="#9AC0CD")
RestaurantBannerLabel.grid(row=0, column=1, sticky="NSEW")

#endregion

#region Menu Section
MainMenuLabel=ttk.Label(menuFrame, text="MENU", style="MenuLabel.TLabel")
MainMenuLabel.grid(row=0, column=0, sticky="WE")
MainMenuLabel.configure(
    anchor="center",
    font=("Helvetica", 14, "bold")
)

ChocolateDishLabel=ttk.Label(ChocolateDishFrame, text="Chocolate -- $3", style="MenuLabel.TLabel")
ChocolateDishLabel.grid(row=0, column=0, padx=10, pady=10, sticky="W")

VanillaDishLabel=ttk.Label(VanillaDishFrame, text="Vanilla -- $3", style="MenuLabel.TLabel")
VanillaDishLabel.grid(row=0, column=0, padx=10, pady=10, sticky="W")

SwirlDishLabel=ttk.Label(SwirlDishFrame, text="Swirl Scoop -- $4", style="MenuLabel.TLabel")
SwirlDishLabel.grid(row=0, column=0, padx=10, pady=10, sticky="W")

ButterscotchDishLabel=ttk.Label(ButterscotchDishFrame, text="Butterscotch -- $4", style="MenuLabel.TLabel")
ButterscotchDishLabel.grid(row=0, column=0, padx=10, pady=10, sticky="W")

CheesecakeDishLabel=ttk.Label(CheesecakeDishFrame, text="Cheesecake -- $4", style="MenuLabel.TLabel")
CheesecakeDishLabel.grid(row=0, column=0, padx=10, pady=10, sticky="W")

MoosetrackDishLabel=ttk.Label(MoosetrackDishFrame, text="Moosetrack -- $5", style="MenuLabel.TLabel")
MoosetrackDishLabel.grid(row=0, column=0, padx=10, pady=10, sticky="W")


ChocolateDisplayButton=ttk.Button(ChocolateDishFrame, text="Display", command=displayChocolate)
ChocolateDisplayButton.grid(row=0, column=1, padx=10)

VanillaDisplayButton=ttk.Button(VanillaDishFrame, text="Display", command=displayVanilla)
VanillaDisplayButton.grid(row=0, column=1, padx=10)

SwirlDisplayButton=ttk.Button(SwirlDishFrame, text="Display", command=displaySwirl)
SwirlDisplayButton.grid(row=0, column=1, padx=10)

ButterscotchDisplayButton=ttk.Button(ButterscotchDishFrame, text="Display", command=displayButterscotch)
ButterscotchDisplayButton.grid(row=0, column=1, padx=10)

CheesecakeDisplayButton=ttk.Button(CheesecakeDishFrame, text="Display", command=displayCheesecake)
CheesecakeDisplayButton.grid(row=0, column=1, padx=10)

MoosetrackDisplayButton=ttk.Button(MoosetrackDishFrame, text="Display", command=displayMoosetrack)
MoosetrackDisplayButton.grid(row=0, column=1, padx=10)

#endreigon

#Order Section

orderTitleLabel=ttk.Label(orderFrame, text="ORDER")
orderTitleLabel.configure(
    foreground="white", background="#9AC0CD",
    font=("Helvetica", 14, "bold"), anchor="center",
    padding=(5,5,5,5),
)
orderTitleLabel.grid(row=0, column=0, sticky="EW")

orderIDLabel=ttk.Label(orderFrame, text="ORDER ID:" + ORDER_ID())
orderIDLabel.configure(
    background="#9AC0CD",
    foreground="white",
    font=("Helvetica", 11, "italic"),
    anchor="center",
)
orderIDLabel.grid(row=1, column=0, sticky="EW", pady=1)


#Region Display Section
displayLabel=ttk.Label(displayFrame, image=displayDefaultImageObject)
displayLabel.grid(row=0, column=0, sticky="NSEW", columnspan=2)
displayLabel.configure(background="#9AC0CD")

addOrderButton = ttk.Button(displayFrame, text="ADD TO CART", command = add)
addOrderButton.grid(row=1, column=0, padx=2, sticky="NSEW")

removeOrderButton=ttk.Button(displayFrame, text="REMOVE")
removeOrderButton.grid(row=1, column=1, padx=2, sticky="NSEW")

orderTransaction = ttk.Label(orderFrame, style='orderTransaction.TLabel')
orderTransaction.grid(row=2, column=0, sticky="NSEW")

orderTotalLabel = ttk.Label(orderFrame, text="TOTAL: $0", style="orderTotalLabel.TLabel")
orderTotalLabel.grid(row=3, column=0, sticky="EW")

orderButton=ttk.Button(orderFrame, text="ORDER", command = order)
orderButton.grid(row=4, column=0, sticky="EW")



#endregion


#---------------GRID CONFIGURATIONS ----------------#

mainFrame.columnconfigure(2, weight=1)
mainFrame.rowconfigure(1, weight=1)
menuFrame.columnconfigure(0, weight=1)
menuFrame.rowconfigure(1, weight=1)
menuFrame.rowconfigure(2, weight=1)
menuFrame.rowconfigure(3, weight=1)
menuFrame.rowconfigure(4, weight=1)
menuFrame.rowconfigure(5, weight=1)
menuFrame.rowconfigure(6, weight=1)
orderFrame.columnconfigure(0, weight=1)
orderFrame.rowconfigure(2, weight=1)


root.mainloop()
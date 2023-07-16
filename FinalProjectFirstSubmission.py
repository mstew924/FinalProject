import tkinter as tk
from tkinter import ttk
from tkinter import*
from PIL import Image, ImageTk


root = Tk()
root.title("TTC-Ice Cream Shop")

#------------FUNCTIONS----------#



#---------- STYLING AND IMAGES ----------#
#region style configurations

s=ttk.Style()
s.configure('MainFrame.TFrame', background= "#F8F8FF")
s.configure('MenuFrame.TFrame', background= "#F8F8FF")
s.configure('DisplayFrame.TFrame', background="#9AC0CD")
s.configure('OrderFrame.Tfram',background="#B7C4CF")
s.configure('DishFrame.TFrame', background="#F8F8FF", relief="raised")
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
           foreground="white",
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

ChocolateDishLabel=ttk.Label(ChocolateDishFrame, text="Chocolate Ice Cream -- $3", style="MenuLabel.TLabel")
ChocolateDishLabel.grid(row=0, column=0, padx=10, pady=10, sticky="W")

VanillaDishLabel=ttk.Label(VanillaDishFrame, text="Vanilla Ice Cream -- $3", style="MenuLabel.TLabel")
VanillaDishLabel.grid(row=0, column=0, padx=10, pady=10, sticky="W")

SwirlDishLabel=ttk.Label(SwirlDishFrame, text="Swirl Ice Cream -- $4", style="MenuLabel.TLabel")
SwirlDishLabel.grid(row=0, column=0, padx=10, pady=10, sticky="W")

ButterscotchDishLabel=ttk.Label(ButterscotchDishFrame, text="Butterscotch Icecream -- $4", style="MenuLabel.TLabel")
ButterscotchDishLabel.grid(row=0, column=0, padx=10, pady=10, sticky="W")

CheesecakeDishLabel=ttk.Label(CheesecakeDishFrame, text="Cheesecake Ice Cream -- $4", style="MenuLabel.TLabel")
CheesecakeDishLabel.grid(row=0, column=0, padx=10, pady=10, sticky="W")

MoosetrackDishLabel=ttk.Label(MoosetrackDishFrame, text="Moose Track Ice Cream -- $5", style="MenuLabel.TLabel")
MoosetrackDishLabel.grid(row=0, column=0, padx=10, pady=10, sticky="W")


ChocolateDisplayButton=ttk.Button(ChocolateDishFrame, text="Display")
ChocolateDisplayButton.grid(row=0, column=1, padx=10)

VanillaDisplayButton=ttk.Button(VanillaDishFrame, text="Display")
VanillaDisplayButton.grid(row=0, column=1, padx=10)

SwirlDisplayButton=ttk.Button(SwirlDishFrame, text="Display")
SwirlDisplayButton.grid(row=0, column=1, padx=10)

ButterscotchDisplayButton=ttk.Button(ButterscotchDishFrame, text="Display")
ButterscotchDisplayButton.grid(row=0, column=1, padx=10)

CheesecakeDisplayButton=ttk.Button(CheesecakeDishFrame, text="Display")
CheesecakeDisplayButton.grid(row=0, column=1, padx=10)

MoosetrackDisplayButton=ttk.Button(MoosetrackDishFrame, text="Display")
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

orderIDLabel=ttk.Label(orderFrame, text="ORDER NUMBER")
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

addOrderButton = ttk.Button(displayFrame, text="ADD TO CART")
addOrderButton.grid(row=1, column=0, padx=2, sticky="NSEW")

removeOrderButton=ttk.Button(displayFrame, text="REMOVE")
removeOrderButton.grid(row=1, column=1, padx=2, sticky="NSEW")

orderTransaction=ttk.Label(orderFrame, style='orderTransaction.TLabel')
orderTransaction.grid(row=2, column=0, sticky="NSEW")

orderTotalLabel=ttk.Label(orderFrame, text="TOTAL: $0", style="orderTotalLabel.TLabel")
orderTotalLabel.grid(row=3, column=0, sticky="EW")

orderButton=ttk.Button(orderFrame, text="ORDER")
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
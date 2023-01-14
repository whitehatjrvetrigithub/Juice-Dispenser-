from tkinter import*
from tkinter import ttk
from PIL import ImageTk,Image
root=Tk()
root.config(bg="#808080")
root.title("Encapsulation")
root.geometry("800x500")
label=Label(root,text="Juice centre")
label.place(relx=0.1,rely=0.2,anchor=CENTER)
Fruit_list=["Apple","Orange","Watermelon","Mango"]
Fruit_dropdown=ttk.Combobox(root,value=Fruit_list)
Fruit_dropdown.place(relx=0.9,rely=0.3,anchor=CENTER)
label_quantity=Label(root,text="Quantity is")
label_quantity.place(relx=0.9,rely=0.4,anchor=CENTER)
input_quantity=Entry(root)
input_quantity.place(relx=0.9,rely=0.5,anchor=CENTER)
label_amount=Label(root)
label_amount.place(relx=0.9,rely=0.6,anchor=CENTER)
label_show_quantity=Label(root)
label_show_quantity.place(relx=0.9,rely=0.7,anchor=CENTER)
img=(Image.open("dispenser.jpg"))
img1=img.resize((400,400))
juiceimage=ImageTk.PhotoImage(img1)
label_image=Label(root,image=juiceimage)
label_image.place(relx=0.1,rely=0.5,anchor=W)
class Juice():
    def __init__(self,Fruit_Name,Quantity):
        self.Fruit=Fruit_Name
        self.Quantity=int(Quantity)
        self.__cost=10
    def __calculate(self):
        totalcost=self.Quantity*self.__cost
        label_amount["text"]="You Have To Pay",str(totalcost)
        print("You Have To Pay",totalcost)
        if(self.Fruit=="Apple"):
            calorie=self.Quantity*52
        elif(self.Fruit=="Orange"):
            calorie=self.Quantity*60
        elif(self.Fruit=="Watermelon"):
            calorie=self.Quantity*30
        elif(self.Fruit=="Mango"):
            calorie=self.Quantity*48
        label_show_quantity["text"]="Total Colorie=",str(calorie)
        print("Total Colorie=",calorie)
        
    def getcost(self):
        self.__calculate()
    
        
def orderjuice():
    fruit=Fruit_dropdown.get()
    quantity=input_quantity.get()
    obj1=Juice(fruit, quantity)
    obj1.getcost()
        
        

button1=Button(root,text="total",command=orderjuice)
button1.place(relx=0.9,rely=0.8,anchor=CENTER)
root.mainloop()
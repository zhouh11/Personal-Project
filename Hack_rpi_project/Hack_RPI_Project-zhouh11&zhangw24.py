from tkinter import *
from tkinter import ttk
import csv
import os
from csv import writer

class Recipe_Book:
    from tkinter import messagebox
    def __init__(self, window):
        
        
        self.title = Label(window,text='Recipe Book',font=(20))
        self.title.place(x=350, y=20)
        
        self.recipe_name_label = Label(window,text='Recipe Name')
        self.recipe_name_label.place(x=100, y=100)
        self.recipe_name_entry = Entry(window,width=70)
        self.recipe_name_entry.place(x=200, y=100)
        
        self.ingredients_name_entry = Text(window,width=50,height =10)
        self.ingredients_name_label = Label(window,text='Ingredients')
        self.ingredients_name_label.place(x=100, y=150)
        self.ingredients_name_entry.place(x=200, y=150)
        
        self.recipe_detail_label = Label(window,text='Recipe Detail')
        self.recipe_detail_label.place(x=100, y=350)
        self.recipe_detail_entry = Text(window,width = 50)
        self.recipe_detail_entry.place(x=200,y=350)
        
        
        self.tree_frame = ttk.Frame(window, width=500, height=800)
        self.tree_frame.grid(row=0, column=0)
        self.tree_frame.place(x=700, y=250)
        self.tree = ttk.Treeview(self.tree_frame, show="headings")
        self.tree.pack(fill="both", expand=True)

        self.open_csv_button = Button(window, text='See saved info', command=self.display_csv_data)
        self.open_csv_button.place(x=700, y=200)
        
        self.save_button = Button(window,text='save',command=self.save_data)
        self.save_button.place(x=700,y=100)

    def create_display(self):
        with open("HackRPI_Project_Recipe_Book.csv", 'r', newline='') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
            self.tree["columns"] = header
            for col in header:
                self.tree.heading(col, text=col)
                self.tree.column(col, width=100)
            for row in csv_reader:
                self.tree.insert("", "end", values=row)

    def display_csv_data(self):
        self.create_display()
        
    def save_data(self):
        rows = [self.recipe_name_entry.get(), self.ingredients_name_entry.get("1.0", "end-1c"), self.recipe_detail_entry.get("1.0", "end-1c")]
        recipe_data.append(rows)
        
        exist_file = os.path.isfile("HackRPI_Project_Recipe_Book.csv")

        recipe_file= open("HackRPI_Project_Recipe_Book.csv", "a") 
        csv_recipe_writer = writer(recipe_file)
        if not exist_file:
            csv_recipe_writer.writerow(['Recipe','Ingredient','Detail'])   

        csv_recipe_writer.writerow(rows)

            
        self.messagebox.showinfo("Entry", "Saved")
        
        self.recipe_name_entry.delete(0, "end")
        self.ingredients_name_entry.delete("1.0", "end")
        self.recipe_detail_entry.delete("1.0",  "end")  


window = Tk()
window.title("Recipe Book")
recipe_data = []
window.geometry("1600x800")
window.configure(background="lightblue")
app = Recipe_Book(window)
window.mainloop()

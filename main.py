import os
import tkinter as tk
import tkinter.ttk as ttk
import pygubu

from Data import data
from tkinter import messagebox



PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "BrowserUIApp.ui")


class BrowseruiappApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object('top_level', master)
        builder.connect_callbacks(self)

        self.tree = self.builder.get_object('show_tree')
        self.nameEntry = self.builder.get_object('nameEntry')
        self.gender = self.builder.get_variable('genderSelection')
        self.setupTree()


    def AddRowToTree(self,theRow):
        self.tree.insert('', 'end', values=(theRow[0],theRow[1],theRow[2],theRow[3],theRow[4]))

    def setupTree(self):

        self.tree.configure(columns=(0, 1, 2, 3, 4), displaycolumns=(0,1, 2, 3, 4))
        self.tree.heading(0, text="Name")
        self.tree.heading(1, text="Year")
        self.tree.heading(2, text="Gender")
        self.tree.heading(3, text="Year Count")
        self.tree.heading(4, text="Total Count")

    def getData(self):

        searchName = self.nameEntry.get()
        # get_variable to retrieve the value that was set for each radio button in designer
        selectedGender = self.gender.get()

        if searchName == "":
            messagebox.showerror("Error", "Please enter a name to search")
        else:

            getRows = data.getData(searchName,selectedGender)

            # this statement is to loop through to empty treeview for the next set of data

            for i in self.tree.get_children():
                self.tree.delete(i)

            # this for retrieves the new set of data by also calling the AddRowToTree for assistance
            # to insert data in each row
            for row in getRows:
                self.AddRowToTree(row)

    def closeProgram(self):
        root.destroy()

    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Juian's Database Project")
    app = BrowseruiappApp(root)
    app.run()

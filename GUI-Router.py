from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
import templateengine
from tkinter import ttk
import tkinter.messagebox


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.master = master
        self.master.title("Template Engine")
        self.init_window()

    def clicked():
        messagebox.showerror("Error", "Please note to use only cool things ")


    def init_window(self):
        self.leftFrame = Frame(self.master, width=490, height=190)
        self.leftFrame.grid(row=0, column=0, padx=5, pady=2)

        self.templateLabel = Label(self.leftFrame,text='Template')
        self.templateLabel.grid(row=1, column=0, sticky=E)

        self.csvLabel = Label(self.leftFrame,text='CSV Data')
        self.csvLabel.grid(row=2, column=0,sticky=E)

        self.outputLabel = Label(self.leftFrame,text='Output Directory')
        self.outputLabel.grid(row=3, column=0, sticky=E)

        self.templateFile = StringVar()
        self.templateEntry = Entry(self.leftFrame, width=50, textvariable=self.templateFile)
        self.templateEntry.grid(row=1, column=1,sticky=E+W)

        self.dataFile = StringVar()
        self.dataEntry = Entry(self.leftFrame, width=50, textvariable=self.dataFile)
        self.dataEntry.grid(row=2, column=1, sticky=E+W)

        self.outputDirectory = StringVar()
        self.outputEntry = Entry(self.leftFrame, width=50, textvariable=self.outputDirectory)
        self.outputEntry.grid(row=3,column=1, sticky=E+W)

        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        fileMenu = Menu(menubar, tearoff=False)
        fileMenu.add_command(label='Choose Template...', command=self.open_template)
        fileMenu.add_command(label='Choose CSV Data...', command=self.open_data)

        fileMenu.add_separator()
        fileMenu.add_command(label='Exit', command=self.client_exit)
        menubar.add_cascade(label='File', menu=fileMenu)

        editMenu = Menu(menubar, tearoff=False)
        editMenu.add_command(label='Test', command=self.clicked)
        menubar.add_cascade(label='Edit', menu=editMenu)

        openButton = Button(self.leftFrame, text='Browse..', command=self.open_template)
        openButton.grid(row=1, column=2, pady=5, padx=5)

        openButton1 = Button(self.leftFrame, text='Browse..', command=self.open_data)
        openButton1.grid(row=2, column=2, pady=5, padx=5)
        openButton2 = Button(self.leftFrame, text='Browse..', command=self.output_directory)
        openButton2.grid(row=3, column=2, pady=5, padx=5)

        buildconfigs = Button(self.leftFrame, text='Build Configs', command=self.build_configs,
                                                                             width=10)
        buildconfigs.grid(row=4, column=2, padx=5)
        quitButton = Button(self.leftFrame, text='Quit', command=self.client_exit)
        quitButton.grid(row=4, column=1)

    def open_template(self):
        fileName = askopenfilename(
                            filetypes=(
                                ("code files", "*.template"),
                                ("All Files", "*.*")
                                    )
                                )
        return self.templateFile.set(fileName)

    def open_data(self):
        fileName = askopenfilename(
                            filetypes=(
                                ("CSV files", "*.csv"),
                                ("All Files", "*.*")
                                      )
                                )

        return self.dataFile.set(fileName)

    def output_directory(self):
        directoryName = askdirectory(initialdir="/", title="Select Output")
        print (directoryName)

        return self.outputDirectory.set(directoryName)

    def build_configs(self):
        templateengine.parseandreplace(self.dataFile.get(),self.templateFile.get(),self.outputDirectory.get())
        tkinter.messagebox.showinfo(title="Complete", message='Configuration builds complete')

    def client_exit(self):
        exit()



root = Tk()
#root.resizable(width=FALSE, height=FALSE)
root.geometry('500x170')
#root.iconbitmap('sync.ico')
app = Window(root)

root.mainloop()

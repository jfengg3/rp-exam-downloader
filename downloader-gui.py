from tkinter import *
from tkinter import filedialog
import downloader, webbrowser, _thread

# Declare a GLOBAL Font
FONT = ('Arial', 14, 'bold')

class GUIDownloader(object):
    def __init__(self):

        # Let's make some fun callbacks :D
        def urlCallback(url):
            webbrowser.open_new(r"https://github.com/evelystria")

        self.username = ''
        self.password = ''
        self.module = ''
        self.folder = ''

        root = Tk()
        root.withdraw()
        root.update_idletasks()

        # Get screen size
        x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
        y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2

        root.geometry("+%d+%d" % (x,y))
        root.deiconify()

        root.title('RP Exam Downloader - v1.1')
        root.resizable(0, 0)

        self.top = Frame(root)
        self.top.grid(row=0, column=0, padx=50, pady=20)
        self.top.columnconfigure(0, weight=1)
        self.top.rowconfigure(0, weight=1)

        Label_Title = Label(self.top, text='RP Exam Downloader', font=('Arial', 28, 'bold'))
        Label_Title.grid(row=1, column=0, columnspan=3, padx=50, pady=20)

        Label_Login = Label(self.top, text='Student ID:', font=FONT)
        Label_Login.grid(row=2, column=0)
        self.LoginField = Entry(self.top, bd=2, textvariable=self.username)
        self.LoginField.grid(row=2, column=1)

        Label_Password = Label(self.top, text='Password:', font=FONT)
        Label_Password.grid(row=3, column=0)
        self.PasswordField = Entry(self.top, bd=2, show='*', textvariable=self.password)
        self.PasswordField.grid(row=3, column=1)

        Label_Module = Label(self.top, text='Module:', font=FONT)
        Label_Module.grid(row=4, column=0)
        self.ModuleField = Entry(self.top, bd=2, textvariable=self.module)
        self.ModuleField.grid(row=4, column=1)

        Label_Folder = Label(self.top, text='Save To Location:', font=FONT)
        Label_Folder.grid(row=5, column=0)
        self.FolderField = Entry(self.top, bd=2, textvariable=self.folder, state='disabled')
        self.FolderField.grid(row=5, column=1)
        Button_Folder = Button(self.top, text='Browse', command=self.locateFolder)
        Button_Folder.grid(row=5, column=2)

        self.StatusField = Label(self.top, text='- Developed by Jing Jie, SOI-DIDM')
        self.StatusField.grid(row=6, columnspan=3, pady=(20,0))
        linkLabel = Label(self.top, text='https://github.com/evelystria', fg="blue", cursor="hand2")
        linkLabel.grid(row=7, columnspan=3, padx=20)
        linkLabel.bind("<Button-1>", urlCallback)

        startButton = Button(self.top, text='Get Papers!', command=self.beginDownload)
        startButton.grid(row=8, columnspan=3, padx=20, pady=20)

        # Run the app
        root.mainloop()

    def locateFolder(self):
        self.folder = filedialog.askdirectory(mustexist=False, parent=self.top, title='Choose a folder')
        self.FolderField.configure(state='normal')
        self.FolderField.delete(0, END)
        self.FolderField.insert(0, self.folder)
        self.FolderField.configure(state='disabled')

    def beginDownload(self):
        username = self.LoginField.get()
        password = self.PasswordField.get()
        module = self.ModuleField.get()
        folder = self.FolderField.get()
        DLR = downloader.downloader('GUI')

        _thread.start_new_thread(DLR.beginDLR, (username, password, module, folder, self.updateStatus))

    def updateStatus(self, dispatch, type='normal'):
        self.StatusField['text'] = dispatch
        if type == 'success':
            self.StatusField['fg'] = 'green'
        elif type == 'error':
            self.StatusField['fg'] = 'red'
        else:
            self.StatusField['fg'] = 'blue'

if __name__ == '__main__':
    GUIDownloader()

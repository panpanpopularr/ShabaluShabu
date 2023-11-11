import subprocess, sys, os, glob
import tkinter as tk
from PIL import Image


class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title("PDF Converter")
        self._frame = None

class AnimalPage(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.master = master
        self.controller = controller
        self.config(relief='sunken', borderwidth=2)
        self.pack(fill = "both", expand = False)
        sys.argv.pop(0)
        allfile = []
        for i in sys.argv:
            if os.path.exists(i):
                if os.path.isdir(i):
                    allfile.extend(glob.glob(os.path.join(i, "*")))
                else:
                    allfile.append(i)

        self.filelist = allfile
        self.filepath = tk.StringVar(value=self.filelist)
        self.animalBox = tk.Listbox(self, listvariable=self.filepath,
                                height=25, width=100, borderwidth=2)
        self.animalBox.bind('<Double-1>', self.go)
        self.animalBox.pack()

        moveUpButton = tk.Button(self, text="Move Up", command=lambda: self.moveup())
        moveUpButton.pack()
        moveDownButton = tk.Button(self, text="Move Down", command=lambda: self.movedown())
        moveDownButton.pack()
        createpdf = tk.Button(self, text="Create PDF", command=lambda: self.pdftime())
        createpdf.pack()

    def pdftime(self):
        imglist = []
        for i in reversed(self.animalBox.get(0, tk.END)):
            image = Image.open(i)
            image_changed = image.convert('RGB')
            imglist.append(image_changed)
        imglist.pop()
        image_changed.save("Test.pdf", save_all=True, append_images=reversed(imglist))

    def go(self, event):
        cs = self.animalBox.get(self.animalBox.curselection())
        Image.open(cs).show()


    def moveup(self, *args):
        try:
            self.idxs = self.animalBox.curselection()
            if not self.idxs:
                return
            for pos in self.idxs:
                if pos==0:
                    continue
                text=self.animalBox.get(pos)
                self.animalBox.delete(pos)
                self.animalBox.insert(pos-1, text)
                self.filelist.pop(pos)
                self.filelist.insert(pos-1, text)
                self.animalBox.selection_set(pos-1)
        except:
            pass
    def movedown(self, *args):
        try:
            self.idxs = self.animalBox.curselection()
            if not self.idxs:
                return
            for pos in self.idxs:
                text=self.animalBox.get(pos)
                print(text)
                self.animalBox.delete(pos)
                self.animalBox.insert(pos+1, text)
                self.filelist.pop(pos)
                self.filelist.insert(pos+1, text)
                self.animalBox.selection_set(pos+1)
        except:
            pass

if __name__ == "__main__":
    app = SampleApp()
    newFrame = AnimalPage(app, app)
    app.geometry("1200x700")
    app.mainloop()

import os, sys
import Tkinter
import tkMessageBox

class Dialog:

    def __init__(self, path):
        self.path = path
        self.dst_path = ''
        self.root = root = Tk()

        root.iconify()
        root.after_idle(self.askdirectory)
        root.mainloop()

    def askdirectory(self):
        self.dst_path = filedialog.askdirectory(initialdir=self.path)
        showinfo('Selected Path', self.dst_path)
        self.root.destroy()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        path = sys.argv[1]
        if os.path.isfile(path):
            path = os.path.dirname(path)

        dialog = Dialog(path)

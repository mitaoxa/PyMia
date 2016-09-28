from Tkinter import *
import ttk

items = ["Item %d" % (i+1,) for i in range(9)]
d = dict(zip(items, [i + ' description.' for i in items]))

root = Tk()
frame = ttk.Frame(root, padding=8)

cb_val = StringVar()
cb_val.set('Item 1')
cb = ttk.Combobox(frame, textvariable=cb_val, height=4)
cb['values'] = sorted(d.keys())

statusmsg = StringVar()
status = ttk.Label(frame, textvariable=statusmsg, relief='solid')

frame.grid()
cb.grid()
status.grid(pady=(80, 0), sticky='SWE')

cb.bind('<<ComboboxSelected>>',
        lambda e: statusmsg.set(d[sorted(d.keys())[int(cb.current())]]))

root.mainloop()
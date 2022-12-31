import calendar
c = calendar.TextCalendar()
m = c.formatmonth(2012,2)
print(m)

import tkinter as tk

s = "중요한 것은 꺾이지 않는 마음"
root = tk.Tk()
t = tk.Text(root, height=20, width=20)
t.insert(tk.END, m)
t.pack()
tk.mainloop()
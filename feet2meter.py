from tkinter import *
from tkinter import ttk

print("Convert your steps in meters")
def calf2m():
	try:
		value = float(feet.get())

		meter.set((0.3048 * value * 10000.0 + 0.5) / 10000.0)
	except:
		meter.set(0)	

root = Tk()
root.title("Feet 2 Meters")

mainFrame = ttk.Frame(root, padding="3 3 12 12")
mainFrame.grid(row=0, column=0, sticky=('n','w','s','e'))

feet = StringVar()

lblFeet = ttk.Label(mainFrame, text="Enter your feets")
lblFeet.grid(row=0, column=1, sticky=('w','e'))

entFeet = ttk.Entry(mainFrame, textvariable=feet, width=20)
entFeet.grid(row=0, column=2, sticky=('w','e'))

#lblmeterT = ttk.Label(mainFrame, text="Your total meters are")
#lblmeterT.grid(row=1, column=0, sticky=('w','e'))

meter = StringVar()

lblmeterT = ttk.Label(mainFrame, text="Your total meters are")
lblmeterT.grid(row=1, column=0, sticky=('w','e'))


lblmeter = ttk.Label(mainFrame, textvariable=meter)
lblmeter.grid(row=1, column=1, sticky=('w','e'))

lblmeterTS = ttk.Label(mainFrame, text="meter")
lblmeterTS.grid(row=1, column=2, sticky=('e'))

calculateBtn = ttk.Button(mainFrame, text="Calculate", width=50, command=calf2m)
calculateBtn.grid(row=2, column=3, sticky=('e'))


root.mainloop()

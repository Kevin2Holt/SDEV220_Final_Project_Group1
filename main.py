import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

"""Constants"""
#File Paths
CIRCLE = "./imgs/Circle.png"
DIAMOND = "./imgs/Diamond.png"
OVAL = "./imgs/Oval.png"
RECT = "./imgs/Rect.png"
RISING_RECT = "./imgs/Rising_Rect.png"
TRAPIZOID = "./imgs/Trapizoid.png"
WAVY_RECT = "./imgs/Wavy_Rect.png"
#Easy-Change Settings
TOOLS_ICON_PADDING = (2,5,5,5)#Left,Up,Right,Down
TOOLS_BAR_SCALER = 40
CANVAS_PADDING =(10,5,5,5)#Left,Up,Right,Down
CANVAS_ITEM_PADDING =(5,5,5,5)#Left,Up,Right,Down
CANVAS_SCALER = 50
#Keybinds
KEY_CIRCLE = 'Q'
KEY_DIAMOND = 'W'
KEY_OVAL = 'E'
KEY_RECT = 'R'
KEY_RISING_RECT = 'T'
KEY_TRAPIZOID = 'Y'
KEY_WAVY_RECT = 'U'


#Test Variables
flowchart = ['Q','w']

#Declare root & set basic properties
root = tk.Tk()
root.resizable(True, True)
root.title("Flowcharts!")
root.geometry("500x385")


#Load Images
circleIconImg = 	Image.open(CIRCLE)
diamondIconImg = 	Image.open(DIAMOND)
ovalIconImg = 		Image.open(OVAL)
rectIconImg = 		Image.open(RECT)
risingRectIconImg = Image.open(RISING_RECT)
trapizoidIconImg = 	Image.open(TRAPIZOID)
wavyRectIconImg = 	Image.open(WAVY_RECT)
#Convert Image to PhotoImage (Readable by Label)
#For Tool Bar
circleIconLab = 	ImageTk.PhotoImage(circleIconImg.resize((		1*TOOLS_BAR_SCALER, 1*TOOLS_BAR_SCALER)))
diamondIconLab = 	ImageTk.PhotoImage(diamondIconImg.resize((		2*TOOLS_BAR_SCALER, 1*TOOLS_BAR_SCALER)))
ovalIconLab = 		ImageTk.PhotoImage(ovalIconImg.resize((			2*TOOLS_BAR_SCALER, 1*TOOLS_BAR_SCALER)))
rectIconLab = 		ImageTk.PhotoImage(rectIconImg.resize((			2*TOOLS_BAR_SCALER, 1*TOOLS_BAR_SCALER)))
risingRectIconLab = ImageTk.PhotoImage(risingRectIconImg.resize((	2*TOOLS_BAR_SCALER, 1*TOOLS_BAR_SCALER)))
trapizoidIconLab = 	ImageTk.PhotoImage(trapizoidIconImg.resize((	2*TOOLS_BAR_SCALER, 1*TOOLS_BAR_SCALER)))
wavyRectIconLab = 	ImageTk.PhotoImage(wavyRectIconImg.resize((		2*TOOLS_BAR_SCALER, 1*TOOLS_BAR_SCALER)))
#For Canvas
circleLab = 	ImageTk.PhotoImage(circleIconImg.resize((		1*CANVAS_SCALER, 1*CANVAS_SCALER)))
diamondLab = 	ImageTk.PhotoImage(diamondIconImg.resize((		2*CANVAS_SCALER, 1*CANVAS_SCALER)))
ovalLab = 		ImageTk.PhotoImage(ovalIconImg.resize((			2*CANVAS_SCALER, 1*CANVAS_SCALER)))
rectLab = 		ImageTk.PhotoImage(rectIconImg.resize((			2*CANVAS_SCALER, 1*CANVAS_SCALER)))
risingRectLab = ImageTk.PhotoImage(risingRectIconImg.resize((	2*CANVAS_SCALER, 1*CANVAS_SCALER)))
trapizoidLab = 	ImageTk.PhotoImage(trapizoidIconImg.resize((	2*CANVAS_SCALER, 1*CANVAS_SCALER)))
wavyRectLab = 	ImageTk.PhotoImage(wavyRectIconImg.resize((		2*CANVAS_SCALER, 1*CANVAS_SCALER)))
#For Canvas



"""Main Canvas"""
canvasFrame = ttk.Frame(root,padding=CANVAS_PADDING)

"""Update Flowchart Canvas"""
def update(flowchart=[Read()]):
	for i, item in enumerate(flowchart):
		if(item.upper()==KEY_CIRCLE):
			itemLabel = ttk.Label(canvasFrame, image=circleLab,		padding=CANVAS_ITEM_PADDING)
		elif(item.upper()==KEY_DIAMOND):
			itemLabel = ttk.Label(canvasFrame, image=diamondLab,	padding=CANVAS_ITEM_PADDING)
		elif(item.upper()==KEY_OVAL):
			itemLabel = ttk.Label(canvasFrame, image=ovalLab,		padding=CANVAS_ITEM_PADDING)
		elif(item.upper()==KEY_RECT):
			itemLabel = ttk.Label(canvasFrame, image=rectLab,		padding=CANVAS_ITEM_PADDING)
		elif(item.upper()==KEY_RISING_RECT):
			itemLabel = ttk.Label(canvasFrame, image=risingRectLab,	padding=CANVAS_ITEM_PADDING)
		elif(item.upper()==KEY_TRAPIZOID):
			itemLabel = ttk.Label(canvasFrame, image=trapizoidLab,	padding=CANVAS_ITEM_PADDING)
		elif(item.upper()==KEY_WAVY_RECT):
			itemLabel = ttk.Label(canvasFrame, image=wavyRectLab,	padding=CANVAS_ITEM_PADDING)

		itemLabel.grid(column=0,row=i)


"""Update (Advanced) Flowchart Canvas"""
# ****Experimental****
#This expects the format of:
#        [
#            [
#                Key,
#                Column,
#                Row
#            ],
#            [...],
#        ]
def updateAdv(flowchart=[Read()]):
	for itemSet in flowchart:
		if(item[0]==KEY_CIRCLE):
			itemLabel = ttk.Label(canvasFrame, image=circleIconLab,		padding=CANVAS_ITEM_PADDING)
		elif(item[0]==KEY_DIAMOND):
			itemLabel = ttk.Label(canvasFrame, image=diamondIconLab,	padding=CANVAS_ITEM_PADDING)
		elif(item[0]==KEY_OVAL):
			itemLabel = ttk.Label(canvasFrame, image=ovalIconLab,		padding=CANVAS_ITEM_PADDING)
		elif(item[0]==KEY_RECT):
			itemLabel = ttk.Label(canvasFrame, image=rectIconLab,		padding=CANVAS_ITEM_PADDING)
		elif(item[0]==KEY_RISING_RECT):
			itemLabel = ttk.Label(canvasFrame, image=risingRectIconLab,	padding=CANVAS_ITEM_PADDING)
		elif(item[0]==KEY_TRAPIZOID):
			itemLabel = ttk.Label(canvasFrame, image=trapizoidIconLab,	padding=CANVAS_ITEM_PADDING)
		elif(item[0]==KEY_WAVY_RECT):
			itemLabel = ttk.Label(canvasFrame, image=wavyRectIconLab,	padding=CANVAS_ITEM_PADDING)

		itemLabel.grid(column=itemSet[1],row=itemSet[2])

# Return contents from "Flowchartdata.txt" file into a list.
def Read():
    txtf = open("flowchartdata.txt","r")
    file_content = txtf.read()
    content_list = list(file_content)
    txtf.close()
    return content_list

# Write key stroke to end of file, expects a variable to be passed through.
def Write(key):
    txtf = open("flowchartdata.txt","a")
    z = key
    txtf.write(z)
    txtf.close()

# Deletes last enty and rewrites list to file.
def Delete():
    txtf = open("flowchartdata.txt","r+")
    file_content = txtf.read()
    clst = list(file_content)
    txtf.close()
    del clst[len(clst)-1]
    x = " ".join(clst)
    txtf = open("flowchartdata.txt","w")
    txtf.write(x)
    txtf.close()


"""Tool Bar"""
toolsFrame = ttk.Frame(root,borderwidth=4,relief="solid")

"""Tool Bar - Icons"""
#Place PhotoImage into Label
circleIcon = 		ttk.Label(toolsFrame, image=circleIconLab,		padding=TOOLS_ICON_PADDING)
diamondIcon = 		ttk.Label(toolsFrame, image=diamondIconLab,		padding=TOOLS_ICON_PADDING)
ovalIcon = 			ttk.Label(toolsFrame, image=ovalIconLab,		padding=TOOLS_ICON_PADDING)
rectIcon = 			ttk.Label(toolsFrame, image=rectIconLab,		padding=TOOLS_ICON_PADDING)
risingRectIcon = 	ttk.Label(toolsFrame, image=risingRectIconLab,	padding=TOOLS_ICON_PADDING)
trapizoidIcon =		ttk.Label(toolsFrame, image=trapizoidIconLab,	padding=TOOLS_ICON_PADDING)
wavyRectIcon = 		ttk.Label(toolsFrame, image=wavyRectIconLab,	padding=TOOLS_ICON_PADDING)
#Place Label on grid
circleIcon.grid(	column=0, row=0)
diamondIcon.grid(	column=0, row=1)
ovalIcon.grid(		column=0, row=2)
rectIcon.grid(		column=0, row=3)
risingRectIcon.grid(column=0, row=4)
trapizoidIcon.grid(	column=0, row=5)
wavyRectIcon.grid(	column=0, row=6)

"""Tool Bar - Key Labels"""
#Create Labels
circleLabel = 		ttk.Label(toolsFrame, text="Q")
diamondLabel = 		ttk.Label(toolsFrame, text="W")
ovalLabel = 		ttk.Label(toolsFrame, text="E")
rectLabel = 		ttk.Label(toolsFrame, text="R")
risingRectLabel = 	ttk.Label(toolsFrame, text="T")
trapizoidLabel = 	ttk.Label(toolsFrame, text="Y")
wavyRectLabel = 	ttk.Label(toolsFrame, text="U")
#Place Labels on grid
circleLabel.grid(		column=0,row=0)
diamondLabel.grid(		column=0,row=1)
ovalLabel.grid(			column=0,row=2)
rectLabel.grid(			column=0,row=3)
risingRectLabel.grid(	column=0,row=4)
trapizoidLabel.grid(	column=0,row=5)
wavyRectLabel.grid(		column=0,row=6)




""" Load flowchart **For Testing Purposes** """
update(flowchart)
update(flowchart)


"""Place frames in root"""
toolsFrame.grid(column=0,row=0,sticky="NW")
canvasFrame.grid(column=1,row=0,sticky="N")

root.mainloop()

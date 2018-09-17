# imports the image package and the EasyFrame package
from breezypythongui import EasyFrame
from tkinter import PhotoImage


class ImageViewer(EasyFrame):
	# illustrates command buttons and user events
	def __init__(self):
	# sets up the window, labels, and buttons
		EasyFrame.__init__(self, title = "Image Viewer")
		self.addLabel(text = "Image Viewer 1.0", row = 0, column = 0, columnspan = 3, sticky = "NSEW")
		# creates button and label where the first image will be inserted
		self.label1 = self.addLabel(text = "", row = 1, column = 0, sticky = "NSEW")
		self.button1 = self.addButton(text = "Click", row = 2, column = 0, command = self.change)
		# creates button and label where the second image will be inserted
		self.label2 = self.addLabel(text = "", row = 1, column = 1, sticky = "NSEW")
		self.button2 = self.addButton(text = "Click", row = 2, column = 1, command = self.change2)
		# creates button and label where the third image will be inserted
		self.label3 = self.addLabel(text = "", row = 1, column = 2, sticky = "NSEW")
		self.button3 = self.addButton(text = "Click", row = 2, column = 2, command = self.change3)

	# methods to handle user events for the first button
	def change(self):
		self.image = PhotoImage(file = "image1.gif")
		self.label1["image"] = self.image
		self.button1["command"] = self.changeBack1
	
	# methods to handle user events for the second button	
	def change2(self):
		self.image2 = PhotoImage(file = "image2.gif")
		self.label2["image"] = self.image2
		self.button2["command"] = self.changeBack2

	# methods to handle user events for the third button	
	def change3(self):
		self.image3 = PhotoImage(file = "image3.gif")
		self.label3["image"] = self.image3
		self.button3["command"] = self.changeBack3
	
	# method to restore the label for the first button
	def changeBack1(self):
		self.label1["image"] = ""
		self.button1["command"] = self.change
		
	# method to restore the label for the second button
	def changeBack2(self):
		self.label2["image"] = "" 
		self.button2["command"] = self.change2
		
	# method to restore the label for the third button
	def changeBack3(self):
		self.label3["image"] = ""
		self.button3["command"] = self.change3
		
		
# main method to compile the program	
def main():
	ImageViewer().mainloop()
	

# activates the program	
if __name__ == "__main__":
	main()
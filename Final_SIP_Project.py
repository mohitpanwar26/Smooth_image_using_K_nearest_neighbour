from tkinter import *
from tkinter import filedialog
import numpy as np
import time
import os
import tkinter as tk
from PIL import Image,ImageTk


# to show the input image
def showimage():
    global img, img1, fln
    fln = filedialog.askopenfilename(initialdir=os.getcwd(),title='select image file',filetype=(('JPG File','.jpg'),("PNG file",".png"),("Tif file",".tif"),("All Files",".")))
    img =Image.open(fln)

    img.thumbnail((800,273))
    img1 =ImageTk.PhotoImage(img)
    lbl.configure(image=img1)
    lbl.image=img1
    
    
def processing():
    global img, img1, im

    image = Image.open(fln)
    image_frame = np.asarray(image)
    print('Input image size is {} x {}'.format(image_frame.shape[1], image_frame.shape[0]))
    
    n = int(n_entry.get())
    k = int(k_entry.get())
    
    # Can be used to keep track of computation time
    start_time = time.monotonic()
    
    # KNN computation using convolution3d() and get_knn_average() starts here
    new_image = convolution3d(image_frame, n, k)
    
    # Can be used to keep track of computation time
    end_time = time.monotonic()
    print('Time Taken to compute is - {} secs\n'.format(round(end_time - start_time, 4)))
    
    form = (new_image*255/np.max(new_image)).astype('uint8')
    im = Image.fromarray(form)
    im.thumbnail((800,273))
    
    # to show output image
    img1 =ImageTk.PhotoImage(im)
    lbl2.configure(imag=img1)
    lbl2.imag=img1
    

# Convolution function will perform convolution over original image
# new_image pixels will be knn averaged pixel values    
def convolution3d(image, n, k):
    y, x, z = image.shape
    y = y - (n - 1)
    x = x - (n - 1)
    new_image = np.zeros((y,x,z))
    for a in range(z):
        for i in range(y):
            for j in range(x):
                new_image[i][j][a] = knn_average(image[i:i+n, j:j+n, a], n, k)

    return new_image    
    

# function to find the average of the local matrix
def knn_average(window_matrix, n, k):
    center_pixel_index = int(n/2 - 0.5)
    center_pixel = window_matrix[center_pixel_index, center_pixel_index]

    window_matrix = window_matrix.flatten()

    # Subtracting center pixel value from local matrix
    differ_matrix = abs(window_matrix - center_pixel)
    
    # Sorting local_matrix (which has actual pixel values) according to absolute difference between pixels
    window_matrix = window_matrix[differ_matrix.argsort()]

    return (np.average(window_matrix[0 : k+1 : 1]))/255

    
# to save the output image    
def saveimage():
    global im
    file = filedialog.asksaveasfilename(filetype=(('JPG File','.jpg'),("PNG file",".png"),("Tif file",".tif"),("All Files",".")),defaultextension='.jpg', initialdir='D:/SIP Project/output') 
    im.save(file)
                                        
# to quit the GUIa
def quit():
    root.destroy()



root =Tk()
img = None
img1=None
frm= Frame(root)
frm.pack(side=BOTTOM,padx=15, pady=15)
lbl=Label(root, text="Open an image to smooth", font="comicsansms 13 bold")
lbl2=Label(root)

# creating label
n_v = Label(root, text = "Enter the size of convolution matrix", font="comicsansms 13 bold")
n_v.place(x = 0, y = 570)
k_v = Label(root, text = "Enter the value of K nearest neighbours", font="comicsansms 13 bold")
k_v.place(x = 0, y = 600)
n_value = StringVar()
k_value = StringVar()

# creating entry box
n_entry = Entry(root, textvariable = n_value)
k_entry = Entry(root, textvariable = k_value)
n_entry.place(x=300,y=573)
k_entry.place(x=330,y=603)
lbl.pack()
lbl2.pack()


#for adding menu bar and open, save as, exit options
Menubar = Menu(root)
FileMenu = Menu(Menubar, tearoff=0)
FileMenu.add_command(label="Open", command=showimage)
FileMenu.add_separator()
FileMenu.add_command(label="Save as", command=saveimage)
FileMenu.add_separator()
FileMenu.add_command(label="Exit", command=quit)
Menubar.add_cascade(label="File",menu=FileMenu)
root.config(menu=Menubar)


#for submit button
btn2=Button(frm,text="Submit", font="comicsansms 13 bold", command=processing)
btn2.pack(padx=20)


root.title('Sip_project')
root.geometry('900x700')
root.mainloop()

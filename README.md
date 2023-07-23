# Smooth_image_using_K_nearest_neighbour

# Smoothing
  1- Implied that local differences between pixels are reduced resulting in a smooth appearance of parts of the image.
  2- Filter window covers the entire image, moving left to right and top to bottom.
  3- Smoothing is done to reduce noise and to generate a less pixelated image.
  4-There are several methods for image smoothing. One of the method that is used in our project is K-Nearest Neighbor algorithm.
# K-Nearest Neighbor averaging 
  1- K-nearest neighbor average: compute equally weighted average of k-nearest neighbors – k neighbors whose gray levels are closest to the central pixel in the           neighborhood.
  2- Sort the neighbors on the basis of similarity of gray level to the central pixel.
  3- Compute the average of K neighbors whose gray levels are closest including the central pixel.

# steps to implement

  1.Use the given file (Final_SIP_Project.exe).
  2.GUI pop up will come, through "open" button in file menu choose any image that you want to smooth.
  3.Provide value of convolution matrix size and k nearest neighbours.
  4.Press "submit" button.
  5.In the back end code will run (Depending on size of n,k and image size it will take some time)
  6.Finally the required smoothen image will appear in gui.
  7.you can use "save as" option from "file" menu to save output image in desired directory.
  8.similarily use "exit" option from "file" menu to exit from gui.

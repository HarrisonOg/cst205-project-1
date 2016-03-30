#Harrison Oglesby SP2016 CST205 Group 30
#I created all the variables at the top (leftover from java programming).
#Then I added the images to the pics array.
#Then I defined my median finding function.
#Then I used 3 loops.  These loops worked to go through
#each picture and pick the same pixel by x and y coordinates, put
#their rgb values into three different arrays, and then use
#my predefined function to find the median value, which would be the rgb values
#without having the person in the picture since that is the only thing changing
#throughout all three pictures.
#Then I saved that median rgb value as the pixel in a new picture which is generated
#as the program goes through each pixel in the other 9 pictures.
#then it shows the picture.

imgfolder = "/Users/harrisonoglesby/cst205/project1/"
pics = []
redval = []
greenval = []
blueval = []
outputpic = makeEmptyPicture(495, 557)

#adding all the images
image1 = makePicture(imgfolder + "1.png")
pics.append(image1)
image2 = makePicture(imgfolder + "1.png")
pics.append(image2)
image3 = makePicture(imgfolder + "3.png")
pics.append(image3)
image4 = makePicture(imgfolder + "4.png")
pics.append(image4)
image5 = makePicture(imgfolder + "5.png")
pics.append(image5)
image6 = makePicture(imgfolder + "6.png")
pics.append(image6)
image7 = makePicture(imgfolder + "7.png")
pics.append(image7)
image8 = makePicture(imgfolder + "8.png")
pics.append(image8)
image9 = makePicture(imgfolder + "9.png")
pics.append(image9)

#a function that finds the median value in an array
def medianVal(values):
  listLength = len(values)
  sortedValues = sorted(values)
  mid = (listLength/2)
  return sortedValues[mid]

#x loop
for w in range(0, 495):
  for y in range(0, 557):		#y loop
    for p in range(0, 9):		#getting the rgb values for that pixel for each pic
      imgpixel = getPixel(pics[p], w, y)
      redval.append(getRed(imgpixel))
      blueval.append(getBlue(imgpixel))
      greenval.append(getGreen(imgpixel))
    setRed(getPixel(outputpic, w, y), medianVal(redval))
    setBlue(getPixel(outputpic, w, y), medianVal(blueval))
    setGreen(getPixel(outputpic, w, y), medianVal(greenval))
    redval = []
    blueval = []
    greenval = []

show(outputpic)
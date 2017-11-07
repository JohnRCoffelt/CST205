#Lab 6

def get_pic():
  return makePicture(pickAFile())

#This function asks where you want to
#store media, then writes a picture to a file
#make sure name ends with the file type extension
def write_pic(pict):
  setMediaFolder()
  name = requestString("Please enter what you want the file to be called with .jpg at the end")
  file = getMediaPath(name)
  writePictureTo(pict, file)
  
# function to create a better black and white image
#I have rewritten this function to return a picture
#and take a picture parameter.
#Nothing fancy  
def betterBnW(pic):
  pixels = getPixels(pic)
  for p in pixels:
    lumin = getRed(p)*0.299 + getBlue(p)*0.114 + getGreen(p)*0.587
    setColor(p, makeColor(lumin, lumin, lumin))
  return pic

#skipping warm up

#Problem 1
#This function creates a sepia toned picture from a picture given
#It then prompts the user to choose where they want to save their file
#then asks them to name it, then it finally saves the file
#oh it'll also show the new sepia toned picture.
def sepiaTone(pic):
  bnw = betterBnW(pic)
  width = getWidth(bnw)
  height = getHeight(bnw)
  for x in range(0, width):
    for y in range(0, height):
    #just need the red and blue values
      r = getRed(getPixel(bnw,x,y))
      b = getBlue(getPixel(bnw,x,y))
      #sepia tone multipliers
      if r < 63:
        r = r * 1.1
        b = b * 0.9
      elif r > 62 and r < 192:
        r = r * 1.15
        b = b * 0.85
      else:
        r = r * 1.08
        if r > 255:#check incase red goes over 255
          r = 255
        b = b * 0.93
      setRed(getPixel(bnw,x,y),r)
      setBlue(getPixel(bnw,x,y),b)
  show(bnw)
  write_pic(bnw)
  return bnw

#Problem 2
#This function "artifies" a picture by modifying rgb values
#based on their initial range. It then shows it, asks the user
#to state where they want to save it, then name it, then finally save it
#with that name.  It also shows and returns the new picture.
def Artify():
  pic = get_pic()
  pixels = getPixels(pic)
  for p in pixels:
    #The following statements do the "artifying" by changing the rgb values
    #based on their initial value.
    rgb = list((p.red, p.green, p.blue))
    for i in range(0,3):
      if rgb[i] < 64:
        rgb[i] = 31
      elif rgb[i] > 63 and rgb[i] < 128:
        rgb[i] = 95
      elif rgb[i] > 127 and rgb[i] < 192:
        rgb[i] = 159
      else:
        rgb[i] = 223
    setColor(p,makeColor(rgb[0],rgb[1],rgb[2]))
  show(pic)
  write_pic(pic)
  return pic

#Problem 3 
# Function that replaces all of the green pixels in an image with pixels forma background image
# The user must first select the BACKGROUND image, then the GREEN SCREEN image.
# With this code,the BACKGROUND must be larger than the GREEN SCREEN image.
def chromakey():
  background = get_pic()
  green_pic = get_pic()
  width = getWidth(green_pic)
  height = getHeight(green_pic)
  #start for loop to cycle through all pixels in the GREEN SCREEN image
  for y in range (0,height): 
    for x in range (0, width):
      #get the pixel from the BACKGROUND image
      back_pixel=getPixel(background, x, y) 
      #get the pixel from the GREEN SCREEN image
      green_pixel=getPixel(green_pic, x, y) 
      #grab the color from the BACKGROUND pixel
      color=getColor(back_pixel) 
      #This if statement tests the GREEN SCREEN pixel to see if the RGB values fall within the green range
      if getRed(green_pixel) < (getGreen(green_pixel) - 30) and getBlue(green_pixel) < (getGreen(green_pixel) - 30):
        #If the pixel is green, re-color it
        setColor(green_pixel, color) 

  repaint(green_pic) 
  write_pic(green_pic)
  return green_pic

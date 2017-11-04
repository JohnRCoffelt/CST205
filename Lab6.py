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
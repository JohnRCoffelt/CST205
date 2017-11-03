def get_pic():
  return makePicture(pickAFile())
  
# function to create a better black and white image  
def betterBnW():
  pic = get_pic()
  pixels = getPixels(pic)
  for p in pixels:
    lumin = getRed(p)*0.299 + getBlue(p)*0.114 + getGreen(p)*0.587
    setColor(p, makeColor(lumin))
  repaint(pic)






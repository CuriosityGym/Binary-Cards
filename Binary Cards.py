from PIL import Image
import numpy as np
from PIL import ImageFont
from PIL import ImageDraw
import math

imgWidth=57
imgHeight=88
sizeMultiplier=3
maxNumber=50
maxExponent=math.ceil(math.log(maxNumber,2))
columns=5
fontSize=10
maxNumbersPerCard=math.pow(2,maxExponent-1)
maxRowCount=math.floor(maxNumbersPerCard/columns)
#positionArray=np.ones((maxRowCount,columns))
xPosM=imgWidth*sizeMultiplier/(columns)
yPosM=xPosM*imgHeight/imgWidth


if(maxNumber<30):
    fontSize=20   
elif(maxNumber<51):
    fontSize=17
elif(maxNumber<70):
    fontSize=10

def writeNumber(imgref, xpos, ypos, number):
    
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("arialbd.ttf", fontSize)
    if(number<10):
        number=" "+str(number)
    draw.text((xpos, ypos), str(number),(0,0,0),font=font)


A=np.ones((imgHeight*sizeMultiplier,imgWidth*sizeMultiplier))
A.fill(255)

for cardNumber in range(0,maxExponent):
    im = Image.fromarray(A)
    if im.mode != 'RGB':
        im = im.convert('RGB')
    counter=0
    rownum=0
    colnum=-1
    for number in range(1,maxNumber):
        shiftedNumber=number>>cardNumber
        if shiftedNumber%2==1:
               
               if(counter%columns==0):
                   rownum=0
                   colnum=colnum+1
               else:
                   rownum=rownum+1
                   
               writeNumber(im,(rownum*xPosM)+(xPosM/4),(colnum*yPosM)+xPosM/4,number)
               counter=counter+1  
    im.save(str(cardNumber)+".jpeg")







#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 18:31:38 2019

@author: siddharth
"""


from PIL import Image
import numpy as np
import cv2
from pytesseract import image_to_string
import pandas as pd


#importing image 

Vidhan_Sabha = []
Part_Number = []
Main_Town = []
PS_Name = []
Male = []
Female = []
Total = []
File_Name = []

for n in range(31,62):
    
    
    img = Image.open('AC04200' +str(n) +'_Page_01.jpg')
    #img.show()

    #using cv2 to actually increse the contrast and using adaptive contrast
    im = cv2.adaptiveThreshold(np.array(img,dtype=np.uint8), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 50)
    im = Image.fromarray(im)
    im
    
    imm = cv2.adaptiveThreshold(np.array(img,dtype=np.uint8), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 100)
    imm = Image.fromarray(imm)
    imm
    
    im2 = cv2.adaptiveThreshold(np.array(img,dtype=np.uint8), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 50)
    im2 = Image.fromarray(im2)
    im2
    
    #cropping image .
    crop_vs = (360, 40, 493, 102)             
    #vs : vidyan sabha
    cropped_vs = im.crop(crop_vs)
    #cropped_vs.show()
    
    crop_pn = (730,60,780,100)                 
    #pn : part number
    cropped_pn = im.crop(crop_pn)
    #cropped_pn.show()                            
    
    crop_mt = (640,560,780,595)                 
    #mt : main town
    cropped_mt = im.crop(crop_mt)
    #cropped_mt.show()
    
    crop_ps = (80,770,590,820)              
    #ps : polling station
    cropped_ps = im.crop(crop_ps)
    #cropped_ps.show()
    
    
    crop_male = (420,980,480,1025)                 
    cropped_male = imm.crop(crop_male)
    
    
    crop_female = (520,980,580,1025)                 
    cropped_female = im.crop(crop_female)
    #cropped_female.show()
    
    crop_total = (690,980,780,1025)                 
    cropped_total = im2.crop(crop_total)
    #cropped_total.show()
    
    
    vidhan_sabha = image_to_string(cropped_vs , config = '--psm 6')
    Vidhan_Sabha.append(vidhan_sabha)
    
    part_number = image_to_string(cropped_pn, config = '--psm 6')
    Part_Number.append(part_number)
    
    main_town = image_to_string(cropped_mt, config = '--psm 6')
    Main_Town.append(main_town)
    
    polling_station = image_to_string(cropped_ps, config = '--psm 6')
    PS_Name.append(polling_station)
    
    male = image_to_string(cropped_male , config = '-c tessedit_char_whitelist=0123456789 --psm 6')
    Male.append(male)
   
    female = image_to_string(cropped_female , config = '-c tessedit_char_whitelist=0123456789 --psm 6')
    Female.append(female)
    
    total = image_to_string(cropped_total , config = '-c tessedit_char_whitelist=0123456789 --psm 6')
    Total.append(total)
    
    filename = 'AC04200' + str(n)
    File_Name.append(filename)
        
        
dataset = pd.DataFrame(np.column_stack([Vidhan_Sabha,Part_Number,Main_Town,PS_Name,Male,Female,Total,File_Name]),columns=['Vidhan Sabha','Part Number','Main Town','PS_Name0','Male','Female','Total','File Name'] )        
dataset.head(10)
       
                    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 17:21:16 2023

@author: saurav
"""

import cv2
import requests
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
from time import perf_counter
 
def breaking_frames():
    capture = cv2.VideoCapture('video.mp4')
     
    frameNr = 0
    frames_list = []
     
    while (True):
     
        success, frame = capture.read()
     
        if success:
            cv2.imwrite(f'output/frame_{frameNr}.jpg', frame)
            frames_list.append(f'frame_{frameNr}')
     
        else:
            break
     
        frameNr = frameNr+1
     
    capture.release()
    return frames_list

def image_captioning(img_lst,processor,model):
    
    
    text = "a photography of"
    label_dict = {}
    
    for img in img_lst:
        raw_image = Image.open(f'output/{img}.jpg').convert('RGB')
        # inputs = processor(raw_image, text, return_tensors="pt").to("cuda")
        # out = model.generate(**inputs)
        inputs = processor(raw_image, return_tensors="pt").to("cuda")
        out = model.generate(**inputs)
        label_dict[img] = processor.decode(out[0], skip_special_tokens=True)
        # inputs = processor(raw_image, return_tensors="pt").to("cuda")
    return label_dict

if __name__ == '__main__':
    
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large").to("cuda")
    
    start = perf_counter()
    frames = breaking_frames()
    label_dict = image_captioning(frames,processor,model)
    end = perf_counter()
    
    print(end - start)
import cv2
import time
import numpy as np
import os
import random
PATH = 'mydata/test_set'



def get_all_gestures():
    gestures = []
    for (dirpath,dirnames,filenames) in os.walk(PATH):
        dirnames.sort()
        for label in dirnames:
            #print(label)
            if not (label == '.DS_Store'):
                for (subdirpath,subdirnames,images) in os.walk(PATH+'/'+label+'/'):
                    random.shuffle(images)
                    #print(label)
                    imagePath = PATH+'/'+label+'/'+images[0]
                    #print(imagePath)
                    img = cv2.imread(imagePath)
                    img = cv2.resize(img, (int(64 * 3/4),int(64* 3/4)))
                    img = cv2.putText(img, label, (5,15), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,255,255), 1, cv2.LINE_AA)
                    gestures.append(img)
    
    print('length of gestures {}'.format(len(gestures)))
    im_tile = concat_tile(gestures, (13, 2))
    return im_tile

def concat_tile(im_list_2d, size):
    count = 0
    all_imgs = []
    for row in range(size[1]):
        imgs = []
        for col in range(size[0]):
            imgs.append(im_list_2d[count])
            count += 1
        all_imgs.append(imgs)    
    return cv2.vconcat([cv2.hconcat(im_list_h) for im_list_h in all_imgs])


gestures = get_all_gestures()
cv2.imwrite("all_gestures.jpg", gestures)

import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import string

def func():
        r = sr.Recognizer()
       
        with sr.Microphone() as source:

                r.adjust_for_ambient_noise(source) 
                i=0
                while True:
                        print('Say something')
                        audio = r.listen(source)

                        try:
                                a=r.recognize_google(audio)
                                print( a.lower())
                                
                                for p in string.punctuation:
                                    a= a.replace(p,"")
                                    
                                if(a.lower()=='close'):
                                        return 'closing window'
                                        break
                         
                                else:
                                    return a
                                       

                        except:
                               return ("Not Audible")
  # result = {
  #       "output": combine
  #   }
  #   result = {str(key): value for key, value in result.items()}
  #   return jsonify(result=result)                       


def ges(a):
       
        arr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
        's','t','u','v','w','x','y','z']
        for p in string.punctuation:
            a= a.replace(p,"")
                                    
        for i in range(len(a)):
            if(a[i] in arr):
                                            
                loc = 'letters/'+a[i]+'.jpg'
                img = mpimg.imread(loc)
                plt.imshow(img)
                plt.draw()
                plt.pause(0.8) 
                                       

        plt.close()
        return 'okay now return to home'                        
                                
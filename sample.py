import winsound
import pygame
import librosa
import time
import threading

class Sample:
    def __init__(self, path):
        self.path = path
        self.length = librosa.get_duration(filename=path)

        self.start_time = None
        

    def start_loop(self):
        self.start_time = time.time()
      

    def wait_loop(self):

        int_time = int((time.time() - self.start_time)/self.length)
        while True:
          
            #check whether loop has been fully played before killing it
            if int((time.time() - self.start_time)/(self.length)) - int_time >= 1:
                break

        

      
           
           
            


    
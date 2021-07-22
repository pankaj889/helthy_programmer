from pygame import mixer
from datetime import datetime
from time import time
def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a== stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")
if __name__ == "__main__":
   # musiconloop("water.mp3","stop")
   init_water = time()
   init_eyes = time()
   init_exercise = time()
   watersecs = 900
   eyessec =  1800
   exercisesec = 2400

   while True:
        if time() -init_water > watersecs:
           print("water Drinking time. enter 'drank' to stop the alarm.")
           musiconloop("water.mp3","drank")
           init_water = time()
           log_now("Drank water at")
        
        if time() -init_eyes > eyessec:
           print("eyes exercise time time. enter 'doneeyes' to stop the alarm.")
           musiconloop("eyes.mp3","doneeyes")
           init_water = time()
           log_now("Eyes Relaxed at")

        if time() -init_exercise > exercisesec:
           print("Exercise  time. enter 'donept' to stop the alarm.")
           musiconloop("exercise.mp3","donept")
           init_water = time()
           log_now("Done exercise at")
      
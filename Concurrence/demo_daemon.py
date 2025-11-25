from threading import Thread
import time 

def draw_caractere(car):
    for i in range(0, 10):
        time.sleep(0.5)
        print(car, end="", flush=True)

t1 = Thread(target=draw_caractere, args="*", daemon=True)
t2 = Thread(target=draw_caractere, args="+", daemon=True)

t1.start()
time.sleep(3)
t2.start()
print(" $ ",end="", flush=True)  #***** $ 
import gpiozero
from time import sleep
import pygame

StepCount = 8
Seq = list(range(0, StepCount))
Seq[0] = [1,0,0,0]
Seq[1] = [1,1,0,0]
Seq[2] = [0,1,0,0]
Seq[3] = [0,1,1,0]
Seq[4] = [0,0,1,0]
Seq[5] = [0,0,1,1]
Seq[6] = [0,0,0,1]
Seq[7] = [1,0,0,1]

class motor:
    def __init__(self,a,b,c,d):
        self.coil_A_1 = gpiozero.DigitalOutputDevice(a)
        self.coil_A_2 = gpiozero.DigitalOutputDevice(b)
        self.coil_B_1 = gpiozero.DigitalOutputDevice(c)
        self.coil_B_2 = gpiozero.DigitalOutputDevice(d)
    
    def setStep(self,w1, w2, w3, w4):
        if w1:
            self.coil_A_1.on()
        else:
            self.coil_A_1.off()
        
        if w2:
            self.coil_A_2.on()
        else:
            self.coil_A_2.off()
        
        if w3:
            self.coil_B_1.on()
        else:
            self.coil_B_1.off()
        
        if w4:
            self.coil_B_2.on()
        else:
            self.coil_B_2.off()
    
    def forward(self,steps):
        for i in range(steps):
            for j in range(StepCount):
                self.setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
                sleep(0.002)
     
    def backward(self,steps):
        for i in range(steps):
            for j in reversed(range(StepCount)):
                self.setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
                sleep(0.002)



if __name__ == '__main__':
    m1 = motor(2,3,4,14)
    '''while True:
        step = input("steps")
        m1.backward(int(step))'''
    m2 = motor(15,18,17,27)
    pygame.init()
    if pygame.joystick.get_count() == 0:
        print("No controller attached")
        exit()
    j = pygame.joystick.Joystick(0)
    j.init()
    
    try:
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.JOYBUTTONDOWN and event.button == 0:
                    j.quit()
                    break
                if event.axis == 1 and event.value != 0 and event.value > 0.1:
                    m1.forward(1)
                elif event.axis == 1 and event.value != 0 and event.value < 0.1:
                    m1.backward(1)
                if event.axis == 4 and event.value != 0 and event.value > 0.1:
                    m2.forward(1)
                elif event.axis == 4 and event.value != 0 and event.value < 0.1:
                    m2.backward(1)
    except KeyboardInterrupt:
        print("EXITING NOW")
        j.quit()

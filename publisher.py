#!/usr/bin/env python
import pygame, sys, time
from pygame.locals import *
import  paho.mqtt.client as mqtt

pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
screen= pygame.display.set_mode((400,300))
pygame.display.set_caption('Blue collar')

interval = 0.01

loopQuit  = False
while loopQuit ==False:
        axis_1 = joystick.get_axis(1) #.get_axis(1)
        axis_1 = axis_1 * 100 
        str_axis_1 = str(int(axis_1)) 
 
        axis_3 = joystick.get_axis(0) #.get_axis(3)
        axis_3 = axis_3 * 100 
        str_axis_3 = str(int(axis_3))
 
        button_5 = str(joystick.get_button(5)*100) 
 
        
        str_js = str_axis_3 + "," + str_axis_1 + "," + button_5
 
        #MQTT?Publish
        broker = "m14.cloudmqtt.com"
        port=14641
        username="zsbxbstt"
        password="O7N1CSgyZAwr"
        client = mqtt.Client()
        client.username_pw_set(username, password)
        client.connect(broker,port)
        client.publish("topic/motor-BCA/dt", str_js);
        client.disconnect();
        
        print (str_js) #Publish
 

        for event in pygame.event.get():
            if event.type == QUIT:
                loopQuit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: 
                    loopQuit = True
        
        time.sleep(interval)
 
pygame.quit()
sys.exit()
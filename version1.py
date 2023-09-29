#only ineficient
# Import the libraries
from sense_hat import SenseHat
from time import sleep

# Set up the Sense HAT
sense = SenseHat()
sense.set_rotation(270, False)

# Set up the colour sensor
sense.color.gain = 60 # Set the sensitivity of the sensor
sense.color.integration_cycles = 64 # The interval at which the reading will be taken

# Add colour variables and image
B = (0, 20, 130) #blue
DB = (0, 20, 102) #dark blue
EDB = (2, 18, 82) #Even darker blue

L = (167, 184, 250) #lua

M = (194, 191, 190) #metal
V = (152, 226, 245) #vidro

frame1 = [
    EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
    EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
    EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
    EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
    DB, DB, DB, DB, DB, DB, DB, DB,  
    DB, DB, DB, DB, DB, DB, DB, DB,
    DB, DB, DB, DB, DB, DB, DB, DB,
    B, B, B, B, B, B, B, B]

frame2= [
    EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
    EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
    EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
    L, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
    L, DB, DB, DB, DB, DB, DB, DB,
    DB, DB, DB, DB, DB, DB, DB, DB,
    DB, DB, DB, DB, DB, DB, DB, DB,
    B, B, B, B, B, B, B, B]

frame3= [
    EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
    L, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
    L, L, EDB, EDB, EDB, EDB, EDB, EDB,
    L, L, EDB, EDB, EDB, EDB, EDB, EDB,
    L, DB, DB, DB, DB, DB, DB, DB,
    DB, DB, DB, DB, DB, DB, DB, DB,
    DB, DB, DB, DB, DB, DB, DB, DB,
    B, B, B, B, B, B, B, B]

frame4= [
    L, L, EDB, EDB, EDB, EDB, EDB, EDB,
    L, L, L, EDB, EDB, EDB, EDB, EDB,
    L, L, L, EDB, EDB, EDB, EDB, EDB,
    L, L, EDB, EDB, EDB, EDB, EDB, EDB,
    DB, DB, DB, DB, DB, DB, DB, DB,  
    DB, DB, DB, DB, DB, DB, DB, DB,
    DB, DB, DB, DB, DB, DB, DB, DB,
    B, B, B, B, B, B, B, B]

frame5= [
    EDB, EDB, L, L, EDB, EDB, EDB, EDB,
    EDB, L, L, L, L, EDB, EDB, EDB,
    EDB, L, L, L, L, EDB, EDB, EDB,
    EDB, EDB, L, L, EDB, EDB, EDB, EDB,
    DB, DB, DB, DB, DB, DB, DB, DB,  
    DB, DB, DB, DB, DB, DB, DB, DB,
    DB, DB, DB, DB, DB, DB, DB, DB,
    B, B, B, B, B, B, B, B]

frame6= [
    EDB, EDB, EDB, L, L, EDB, EDB, EDB,
    EDB, EDB, L, L, L, L, EDB, EDB,
    EDB, EDB, L, L, L, L, EDB, EDB,
    EDB, EDB, EDB, L, L, EDB, EDB, EDB,
    DB, DB, DB, DB, DB, DB, DB, DB,  
    DB, DB, DB, DB, DB, DB, DB, DB,
    DB, DB, DB, DB, DB, DB, DB, DB,
    B, B, B, B, B, B, B, B]

frame7 = [
    EDB, EDB, EDB, EDB, EDB, EDB, L, L,
    EDB, EDB, EDB, EDB, EDB, L, L, L,
    EDB, EDB, EDB, EDB, EDB, L, L, L,
    EDB, EDB, EDB, EDB, EDB, EDB, L, L,
    DB, DB, DB, DB, DB, DB, DB, DB,  
    DB, DB, DB, DB, DB, DB, DB, DB,
    DB, DB, DB, DB, DB, DB, DB, DB,
    B, B, B, B, B, B, B, B]

frame8 = [
    EDB, EDB, EDB, EDB, EDB, EDB, EDB, L,
    EDB, EDB, EDB, EDB, EDB, EDB, L, L,
    EDB, EDB, EDB, EDB, EDB, EDB, L, L,
    EDB, EDB, EDB, EDB, EDB, EDB, EDB, L,
    DB, DB, DB, DB, DB, DB, DB, DB,  
    DB, DB, DB, DB, DB, DB, DB, DB,
    DB, DB, DB, DB, DB, DB, DB, DB,
    B, B, B, B, B, B, B, B]

frame9 = [
    EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
    EDB, EDB, EDB, EDB, EDB, EDB, EDB, L,
    EDB, EDB, EDB, EDB, EDB, EDB, L, L,
    EDB, EDB, EDB, EDB, EDB, EDB, L, L,
    DB, DB, DB, DB, DB, DB, DB, L,
    DB, DB, DB, DB, DB, DB, DB, DB,
    DB, DB, DB, DB, DB, DB, DB, DB,
    B, B, B, B, B, B, B, B]

frame10 = [
    EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
    EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
    EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
    EDB, EDB, EDB, EDB, EDB, EDB, EDB, L,
    DB, DB, DB, DB, DB, DB, DB, L,
    DB, DB, DB, DB, DB, DB, DB, DB,
    DB, DB, DB, DB, DB, DB, DB, DB,
    B, B, B, B, B, B, B, B]

frame12 = [
    EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
    EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
    EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
    EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
    DB, DB, DB, DB, DB, DB, DB, M,
    DB, DB, DB, DB, DB, DB, DB, M,
    DB, DB, DB, DB, DB, DB, DB, DB,
    B, B, B, B, B, B, B, B]

frame13 = [
    EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
    EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
    EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
    EDB, EDB, EDB, EDB, EDB, EDB, EDB, V,
    DB, DB, DB, DB, DB, DB, M, M,
    DB, DB, DB, DB, DB, DB, M, M,
    DB, DB, DB, DB, DB, DB, DB, DB,
    B, B, B, B, B, B, B, B]

frame14 = [
    EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
    EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
    EDB, EDB, EDB, EDB, EDB, EDB, EDB, V,
    EDB, EDB, EDB, EDB, EDB, EDB, V, V,
    DB, DB, DB, DB, DB, M, M, M, 
    DB, DB, DB, DB, DB, M, M, M,
    DB, DB, DB, DB, DB, DB, DB, DB,
    B, B, B, B, B, B, B, B]

frame15 = [
    EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
    EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
    EDB, EDB, EDB, EDB, EDB, EDB, V, M,
    EDB, EDB, EDB, EDB, EDB, V, V, M,
    DB, DB, DB, DB, M, M, M, M,
    DB, DB, DB, DB, M, M, M, M,
    DB, DB, DB, DB, DB, DB, DB, DB,
    B, B, B, B, B, B, B, B]

frame16 = [
    EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
    EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
    EDB, EDB, EDB, EDB, EDB, V, M, M,
    EDB, EDB, EDB, EDB, V, V, M, M, 
    DB, DB, DB, M, M, M, M, M,
    DB, DB, DB, M, M, M, M, M,
    DB, DB, DB, DB, DB, DB, DB, DB,
    B, B, B, B, B, B, B, B]

frame17 = [
    EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
    EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
    EDB, EDB, EDB, EDB, V, M, M, M,
    EDB, EDB, EDB, V, V, M, M, M,
    DB, DB, M, M, M, M, M, M,
    DB, DB, M, M, M, M, M, M,
    DB, DB, DB, DB, DB, DB, DB, DB,
    B, B, B, B, B, B, B, B]

frame18 = [
    EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
    EDB, EDB, EDB, EDB, EDB, EDB, EDB, M,
    EDB, EDB, EDB, V, M, M, M, M,
    EDB, EDB, V, V, M, M, M, M,
    DB, M, M, M, M, M, M, M,
    DB, M, M, M, M, M, M, M,
    DB, DB, DB, DB, DB, DB, DB, DB,
    B, B, B, B, B, B, B, B]

frame19 = [
    EDB, EDB, EDB, EDB, EDB, EDB, EDB, M,
    EDB, EDB, EDB, EDB, EDB, EDB, M, M,
    EDB, EDB, V, M, M, M, M, M,
    EDB, V, V, M, M, M, M, M,
    M, M, M, M, M, M, M, M,
    M, M, M, M, M, M, M, M,
    DB, DB, DB, DB, DB, DB, DB, DB,
    B, B, B, B, B, B, B, B]

frame20 = [
    EDB, EDB, EDB, EDB, EDB, EDB, M, M,
    EDB, EDB, EDB, EDB, EDB, M, M, M,
    EDB, V, M, M, M, M, M, M,
    V, V, M, M, M, M, M, M,
    M, M, M, M, M, M, M, M,
    M, M, M, M, M, M, M, M,
    DB, DB, DB, DB, DB, DB, DB, M,
    B, B, B, B, B, B, B, B]

frame21 = [
    EDB, EDB, EDB, EDB, EDB, M, M, EDB,
    EDB, EDB, EDB, EDB, M, M, M, EDB,
    V, M, M, M, M, M, M, EDB,
    V, M, M, M, M, M, M, EDB,
    M, M, M, M, M, M, M, DB,
    M, M, M, M, M, M, M, DB,
    DB, DB, DB, DB, DB, DB, M, DB,
    B, B, B, B, B, B, B, B]

frame22 = [
    EDB, EDB, EDB, EDB, M, M, EDB, EDB,
    EDB, EDB, EDB, M, M, M, EDB, EDB,
    M, M, M, M, M, M, EDB, EDB,
    M, M, M, M, M, M, EDB, EDB,
    M, M, M, M, M, M, DB, DB,
    M, M, M, M, M, M, DB, DB,
    DB, DB, DB, DB, DB, M, DB, DB,
    B, B, B, B, B, B, B, B]

frame23 = [
    EDB, EDB, EDB, M, M, EDB, EDB, EDB,
    EDB, EDB, M, M, M, EDB, EDB, EDB,
    M, M, M, M, M, EDB, EDB, EDB,
    M, M, M, M, M, EDB, EDB, EDB,
    M, M, M, M, M, DB, DB, DB,
    M, M, M, M, M, DB, DB, DB,
    DB, DB, DB, DB, M, DB, DB, DB,
    B, B, B, B, B, B, B, B]

frame24 = [
    EDB, EDB, M, M, EDB, EDB, EDB, EDB,
    EDB, M, M, M, EDB, EDB, EDB, EDB,
    M, M, M, M, EDB, EDB, EDB, EDB,
    M, M, M, M, EDB, EDB, EDB, EDB,
    M, M, M, M, DB, DB, DB, DB,
    M, M, M, M, DB, DB, DB, DB,
    DB, DB, DB, M, DB, DB, DB, DB,
    B, B, B, B, B, B, B, B]

frame25 = [
    EDB, M, M, EDB, EDB, EDB, EDB, EDB,
    M, M, M, EDB, EDB, EDB, EDB, EDB,
    M, M, M, EDB, EDB, EDB, EDB, EDB,
    M, M, M, EDB, EDB, EDB, EDB, EDB,
    M, M, M, DB, DB, DB, DB, DB,
    M, M, M, DB, DB, DB, DB, DB,
    DB, DB, M, DB, DB, DB, DB, DB,
    B, B, B, B, B, B, B, B]

frame26 = [
    M, M, EDB, EDB, EDB, EDB, EDB, EDB,
    M, M, EDB, EDB, EDB, EDB, EDB, EDB,
    M, M, EDB, EDB, EDB, EDB, EDB, EDB,
    M, M, EDB, EDB, EDB, EDB, EDB, EDB,
    M, M, DB, DB, DB, DB, DB, DB,
    M, M, DB, DB, DB, DB, DB, DB,
    DB, M, DB, DB, DB, DB, DB, DB,
    B, B, B, B, B, B, B, B]

frame27 = [
    M, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
    M, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
    M, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
    M, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
    M, DB, DB, DB, DB, DB, DB, DB,
    M, DB, DB, DB, DB, DB, DB, DB,
    M, DB, DB, DB, DB, DB, DB, DB,
    B, B, B, B, B, B, B, B]
for i in range(28):
    if i ==1:
        sense.set_pixels(frame1)
    if i ==2:
        sense.set_pixels(frame2)
    if i ==3:
        sense.set_pixels(frame3)
    if i ==4:
        sense.set_pixels(frame4)
    if i ==5:
        sense.set_pixels(frame5)
    if i ==6:
        sense.set_pixels(frame6)
    if i ==7:
        sense.set_pixels(frame7)
    if i ==8:
        sense.set_pixels(frame8)
    if i ==9:
        sense.set_pixels(frame9)
    if i ==10:
        sense.set_pixels(frame10)
    if i ==11:
        sense.set_pixels(frame1)
    if i ==12:
        sense.set_pixels(frame12)
    if i ==13:
        sense.set_pixels(frame13)
    if i ==14:
        sense.set_pixels(frame14)
    if i ==15:
        sense.set_pixels(frame15)
    if i ==16:
        sense.set_pixels(frame16)
    if i ==17:
        sense.set_pixels(frame17)
    if i ==18:
        sense.set_pixels(frame18)
    if i ==19:
        sense.set_pixels(frame19)
    if i ==20:
        sense.set_pixels(frame20)
    if i ==21:
        sense.set_pixels(frame21)
    if i ==22:
        sense.set_pixels(frame22)
    if i ==23:
        sense.set_pixels(frame23)
    if i ==24:
        sense.set_pixels(frame24)
    if i ==25:
        sense.set_pixels(frame25)
    if i ==26:
        sense.set_pixels(frame26)
    if i ==27:
        sense.set_pixels(frame27)
    if i ==28:
        sense.set_pixels(frame1)
    if i ==29:
        print("i´ve reached the end")

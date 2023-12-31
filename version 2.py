# Import the libraries
from sense_hat import SenseHat
from time import sleep

# Set up the Sense HAT
sense = SenseHat()
sense.set_rotation(270, False)

# Set up the colour sensor
sense.color.gain = 60 # Set the sensitivity of the sensor
sense.color.integration_cycles = 64 # The interval at which the reading will be taken

class Lc: #check for moon colour sensor reactive
    def __init__(self, Red, Green, Blue):
        if Red==0 and Green==0 and Blue==0:
            self.Red = 167
            self.Green= 184
            self.Blue= 250
        else:
            self.Red = Red
            self.Green = Green
            self.Blue = Blue

# Add colour variables and image
B = (0, 20, 130) #blue
DB = (0, 20, 102) #dark blue
EDB = (2, 18, 82) #Even darker blue

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

# Display the image  
for i in range(len(frames)):
   rgb = sense.color#ayo check the colour trough the sensor    
    #see if rgb sensor is black
   L = Lc(rbg.red, rgb.grenn, rbg.blue)
   sense.set_pixels(frames[i])

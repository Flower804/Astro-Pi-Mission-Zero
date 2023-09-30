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

M = (194, 191, 190) #metal
V = (152, 226, 245) #vidro

Bl= (0, 0, 0)#black
Sb= (0, 191, 255)#blue water
G= (0, 255, 127)#green

for i in range(46): #i don't know why i put this here but if i take it out, EVERYTHING BREAKS, sooooo
    rgb = sense.color    
    L = (rgb.red, rgb.green, rgb.blue)
    frames = [[
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        DB, DB, DB, DB, DB, DB, DB, DB,  
        DB, DB, DB, DB, DB, DB, DB, DB,
        DB, DB, DB, DB, DB, DB, DB, DB,
        B, B, B, B, B, B, B, B]

    , [
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        L, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        L, DB, DB, DB, DB, DB, DB, DB,
        DB, DB, DB, DB, DB, DB, DB, DB,
        DB, DB, DB, DB, DB, DB, DB, DB,
        B, B, B, B, B, B, B, B]

    , [
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        L, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        L, L, EDB, EDB, EDB, EDB, EDB, EDB,
        L, L, EDB, EDB, EDB, EDB, EDB, EDB,
        L, DB, DB, DB, DB, DB, DB, DB,
        DB, DB, DB, DB, DB, DB, DB, DB,
        DB, DB, DB, DB, DB, DB, DB, DB,
        B, B, B, B, B, B, B, B]

    , [
        L, L, EDB, EDB, EDB, EDB, EDB, EDB,
        L, L, L, EDB, EDB, EDB, EDB, EDB,
        L, L, L, EDB, EDB, EDB, EDB, EDB,
        L, L, EDB, EDB, EDB, EDB, EDB, EDB,
        DB, DB, DB, DB, DB, DB, DB, DB,  
        DB, DB, DB, DB, DB, DB, DB, DB,
        DB, DB, DB, DB, DB, DB, DB, DB,
        B, B, B, B, B, B, B, B]

    , [
        EDB, EDB, L, L, EDB, EDB, EDB, EDB,
        EDB, L, L, L, L, EDB, EDB, EDB,
        EDB, L, L, L, L, EDB, EDB, EDB,
        EDB, EDB, L, L, EDB, EDB, EDB, EDB,
        DB, DB, DB, DB, DB, DB, DB, DB,  
        DB, DB, DB, DB, DB, DB, DB, DB,
        DB, DB, DB, DB, DB, DB, DB, DB,
        B, B, B, B, B, B, B, B]

    , [
        EDB, EDB, EDB, L, L, EDB, EDB, EDB,
        EDB, EDB, L, L, L, L, EDB, EDB,
        EDB, EDB, L, L, L, L, EDB, EDB,
        EDB, EDB, EDB, L, L, EDB, EDB, EDB,
        DB, DB, DB, DB, DB, DB, DB, DB,  
        DB, DB, DB, DB, DB, DB, DB, DB,
        DB, DB, DB, DB, DB, DB, DB, DB,
        B, B, B, B, B, B, B, B]

    ,[
        EDB, EDB, EDB, EDB, EDB, EDB, L, L,
        EDB, EDB, EDB, EDB, EDB, L, L, L,
        EDB, EDB, EDB, EDB, EDB, L, L, L,
        EDB, EDB, EDB, EDB, EDB, EDB, L, L,
        DB, DB, DB, DB, DB, DB, DB, DB,  
        DB, DB, DB, DB, DB, DB, DB, DB,
        DB, DB, DB, DB, DB, DB, DB, DB,
        B, B, B, B, B, B, B, B]

    ,[
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, L,
        EDB, EDB, EDB, EDB, EDB, EDB, L, L,
        EDB, EDB, EDB, EDB, EDB, EDB, L, L,
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, L,
        DB, DB, DB, DB, DB, DB, DB, DB,  
        DB, DB, DB, DB, DB, DB, DB, DB,
        DB, DB, DB, DB, DB, DB, DB, DB,
        B, B, B, B, B, B, B, B]

    ,[
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, L,
        EDB, EDB, EDB, EDB, EDB, EDB, L, L,
        EDB, EDB, EDB, EDB, EDB, EDB, L, L,
        DB, DB, DB, DB, DB, DB, DB, L,
        DB, DB, DB, DB, DB, DB, DB, DB,
        DB, DB, DB, DB, DB, DB, DB, DB,
        B, B, B, B, B, B, B, B]

    ,[
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, L,
        DB, DB, DB, DB, DB, DB, DB, L,
        DB, DB, DB, DB, DB, DB, DB, DB,
        DB, DB, DB, DB, DB, DB, DB, DB,
        B, B, B, B, B, B, B, B]

    ,[
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        DB, DB, DB, DB, DB, DB, DB, M,
        DB, DB, DB, DB, DB, DB, DB, M,
        DB, DB, DB, DB, DB, DB, DB, DB,
        B, B, B, B, B, B, B, B]

    ,[
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, V,
        DB, DB, DB, DB, DB, DB, M, M,
        DB, DB, DB, DB, DB, DB, M, M,
        DB, DB, DB, DB, DB, DB, DB, DB,
        B, B, B, B, B, B, B, B]

    ,[
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, V,
        EDB, EDB, EDB, EDB, EDB, EDB, V, V,
        DB, DB, DB, DB, DB, M, M, M, 
        DB, DB, DB, DB, DB, M, M, M,
        DB, DB, DB, DB, DB, DB, DB, DB,
        B, B, B, B, B, B, B, B]
    ,[
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, EDB, EDB, V, M,
        EDB, EDB, EDB, EDB, EDB, V, V, M,
        DB, DB, DB, DB, M, M, M, M,
        DB, DB, DB, DB, M, M, M, M,
        DB, DB, DB, DB, DB, DB, DB, DB,
        B, B, B, B, B, B, B, B]
    ,[
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, EDB, V, M, M,
        EDB, EDB, EDB, EDB, V, V, M, M, 
        DB, DB, DB, M, M, M, M, M,
        DB, DB, DB, M, M, M, M, M,
        DB, DB, DB, DB, DB, DB, DB, DB,
        B, B, B, B, B, B, B, B]
    ,[
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, V, M, M, M,
        EDB, EDB, EDB, V, V, M, M, M,
        DB, DB, M, M, M, M, M, M,
        DB, DB, M, M, M, M, M, M,
        DB, DB, DB, DB, DB, DB, DB, DB,
        B, B, B, B, B, B, B, B]
    ,[
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, M,
        EDB, EDB, EDB, V, M, M, M, M,
        EDB, EDB, V, V, M, M, M, M,
        DB, M, M, M, M, M, M, M,
        DB, M, M, M, M, M, M, M,
        DB, DB, DB, DB, DB, DB, DB, DB,
        B, B, B, B, B, B, B, B]
    ,[
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, M,
        EDB, EDB, EDB, EDB, EDB, EDB, M, M,
        EDB, EDB, V, M, M, M, M, M,
        EDB, V, V, M, M, M, M, M,
        M, M, M, M, M, M, M, M,
        M, M, M, M, M, M, M, M,
        DB, DB, DB, DB, DB, DB, DB, DB,
        B, B, B, B, B, B, B, B]
    ,[
        EDB, EDB, EDB, EDB, EDB, EDB, M, M,
        EDB, EDB, EDB, EDB, EDB, M, M, M,
        EDB, V, M, M, M, M, M, M,
        V, V, M, M, M, M, M, M,
        M, M, M, M, M, M, M, M,
        M, M, M, M, M, M, M, M,
        DB, DB, DB, DB, DB, DB, DB, M,
        B, B, B, B, B, B, B, B]
    ,[
        EDB, EDB, EDB, EDB, EDB, M, M, EDB,
        EDB, EDB, EDB, EDB, M, M, M, EDB,
        V, M, M, M, M, M, M, EDB,
        V, M, M, M, M, M, M, EDB,
        M, M, M, M, M, M, M, DB,
        M, M, M, M, M, M, M, DB,
        DB, DB, DB, DB, DB, DB, M, DB,
        B, B, B, B, B, B, B, B]
    ,[
        EDB, EDB, EDB, EDB, M, M, EDB, EDB,
        EDB, EDB, EDB, M, M, M, EDB, EDB,
        M, M, M, M, M, M, EDB, EDB,
        M, M, M, M, M, M, EDB, EDB,
        M, M, M, M, M, M, DB, DB,
        M, M, M, M, M, M, DB, DB,
        DB, DB, DB, DB, DB, M, DB, DB,
        B, B, B, B, B, B, B, B]
    ,[
        EDB, EDB, EDB, M, M, EDB, EDB, EDB,
        EDB, EDB, M, M, M, EDB, EDB, EDB,
        M, M, M, M, M, EDB, EDB, EDB,
        M, M, M, M, M, EDB, EDB, EDB,
        M, M, M, M, M, DB, DB, DB,
        M, M, M, M, M, DB, DB, DB,
        DB, DB, DB, DB, M, DB, DB, DB,
        B, B, B, B, B, B, B, B]
    ,[
        EDB, EDB, M, M, EDB, EDB, EDB, EDB,
        EDB, M, M, M, EDB, EDB, EDB, EDB,
        M, M, M, M, EDB, EDB, EDB, EDB,
        M, M, M, M, EDB, EDB, EDB, EDB,
        M, M, M, M, DB, DB, DB, DB,
        M, M, M, M, DB, DB, DB, DB,
        DB, DB, DB, M, DB, DB, DB, DB,
        B, B, B, B, B, B, B, B]
    ,[
        EDB, M, M, EDB, EDB, EDB, EDB, EDB,
        M, M, M, EDB, EDB, EDB, EDB, EDB,
        M, M, M, EDB, EDB, EDB, EDB, EDB,
        M, M, M, EDB, EDB, EDB, EDB, EDB,
        M, M, M, DB, DB, DB, DB, DB,
        M, M, M, DB, DB, DB, DB, DB,
        DB, DB, M, DB, DB, DB, DB, DB,
        B, B, B, B, B, B, B, B]
    ,[
        M, M, EDB, EDB, EDB, EDB, EDB, EDB,
        M, M, EDB, EDB, EDB, EDB, EDB, EDB,
        M, M, EDB, EDB, EDB, EDB, EDB, EDB,
        M, M, EDB, EDB, EDB, EDB, EDB, EDB,
        M, M, DB, DB, DB, DB, DB, DB,
        M, M, DB, DB, DB, DB, DB, DB,
        DB, M, DB, DB, DB, DB, DB, DB,
        B, B, B, B, B, B, B, B]
    ,[
        M, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        M, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        M, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        M, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        M, DB, DB, DB, DB, DB, DB, DB,
        M, DB, DB, DB, DB, DB, DB, DB,
        M, DB, DB, DB, DB, DB, DB, DB,
        B, B, B, B, B, B, B, B]
    ,[
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        DB, DB, DB, DB, DB, DB, DB, DB,
        DB, DB, DB, DB, DB, DB, DB, DB,
        DB, DB, DB, DB, DB, DB, DB, DB,
        B, B, B, B, B, B, B, B]
    ,[
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        DB, DB, DB, DB, DB, DB, DB, DB,
        DB, DB, DB, DB, DB, DB, DB, DB,
        DB, DB, DB, DB, DB, DB, DB, DB,
        L, L, L, L, L, L, L, L]
    ,[
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        DB, DB, DB, DB, DB, DB, DB, DB,
        DB, DB, DB, DB, DB, DB, DB, DB, 
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L]
    ,[
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        DB, DB, DB, DB, DB, DB, DB, DB,
        L, L, L, L, L, L, L, L, 
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L]
    ,[
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L, 
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L]
    ,[
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L, 
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L]
    ,[
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB, 
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L, 
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L]
    ,[
        EDB, EDB, EDB, EDB, EDB, EDB, EDB, EDB,
        L, L, L, L, L, L, L, L, 
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L, 
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L]
    ,[ #35
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L, 
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L, 
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L]
    ,[
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L, 
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L, 
        L, L, L, L, L, L, L, L,
        L, L, B, B, B, B, L, L]
    ,[
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L, 
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L, 
        L, L, Bl, Bl, Bl, Bl, L, L,
        L, Bl, Sb, Sb, Sb, G, Bl, L]
    ,[
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L, 
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L,
        L, L, Bl, Bl, Bl, Bl, L, L, 
        L, Bl, Sb, Sb, Sb, G, Bl, L,
        Bl, Sb, Sb, Sb, Sb, G, G, Bl]
    ,[
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L, 
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L,
        L, L, Bl, Bl, Bl, Bl, L, L,
        L, Bl, Sb, Sb, Sb, G, Bl, L, 
        Bl, Sb, Sb, Sb, Sb, G, G, Bl,
        Bl, Sb, Sb, Sb, G, G, G, Bl]
    ,[
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L, 
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L,
        L, L, Bl, Bl, Bl, Bl, L, L,
        L, Bl, Sb, Sb, Sb, G, Bl, L, 
        Bl, Sb, Sb, Sb, Sb, G, G, Bl,
        Bl, Sb, Sb, Sb, G, G, G, Bl]
    ,[
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L, 
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L,
        L, L, Bl, Bl, Bl, Bl, L, L,
        L, Bl, Sb, Sb, Sb, G, Bl, L, 
        Bl, Sb, Sb, Sb, Sb, G, G, Bl,
        Bl, Sb, Sb, Sb, G, G, G, Bl]
    ,[
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L, 
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L,
        L, L, Bl, Bl, Bl, Bl, L, L,
        L, Bl, Sb, Sb, Sb, G, Bl, L, 
        Bl, Sb, Sb, Sb, Sb, G, G, Bl,
        Bl, Sb, Sb, Sb, G, G, G, Bl]
    ,[
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L, 
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L,
        L, L, Bl, Bl, Bl, Bl, L, L,
        L, Bl, Sb, Sb, Sb, G, Bl, L, 
        Bl, Sb, Sb, Sb, Sb, G, G, Bl,
        Bl, Sb, Sb, Sb, G, G, G, Bl]
    ,[
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L, 
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L,
        L, L, Bl, Bl, Bl, Bl, L, L,
        L, Bl, Sb, Sb, Sb, G, Bl, L, 
        Bl, Sb, Sb, Sb, Sb, G, G, Bl,
        Bl, Sb, Sb, Sb, G, G, G, Bl]
    ,[
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L, 
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L,
        L, L, Bl, Bl, Bl, Bl, L, L,
        L, Bl, Sb, Sb, Sb, G, Bl, L, 
        Bl, Sb, Sb, Sb, Sb, G, G, Bl,
        Bl, Sb, Sb, Sb, G, G, G, Bl]
    ,[
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L, 
        L, L, L, L, L, L, L, L,
        L, L, L, L, L, L, L, L,
        L, L, Bl, Bl, Bl, Bl, L, L,
        L, Bl, Sb, Sb, Sb, G, Bl, L, 
        Bl, Sb, Sb, Sb, Sb, G, G, Bl,
        Bl, Sb, Sb, Sb, G, G, G, Bl]
    ]
             
    #see if rgb sensor is black
    sense.set_pixels(frames[i])
    sleep(0.5)

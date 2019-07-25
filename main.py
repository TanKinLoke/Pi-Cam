import sys, os
from picamera import PiCamera, Color
from datetime import datetime
from time import sleep
from termcolor import colored

#Setup
camera = PiCamera()

#Functions
def preview():
    camera.start_preview()
    sleep(5)
    camera.stop_preview()
    Start()
    
def capture():
    #Clear Terminal
    ClearTerminal()
    #Image name
    typew("Image Name:\n1)Date and Time\n2)Custom\n3)Back\n\nSelect:")
    option = input()
    path = ""
    if option.isdigit():
        if option == "1":
            path = "{programpath}/Gallery/Images/{filename}.jpg".format(filename=datetime.now(),programpath=sys.path[0])
        elif option == "2":
            typew("Enter the name you want: ")
            name = input()
            path = "{programpath}/Gallery/Images/{filename}.jpg".format(filename=name,programpath=sys.path[0])
        elif option == "3":
            Start()
        else:
            typew("Please enter a valid selection.")
            Start()
    else:
        typew("\nPlease enter a number!\n")
    #Start capture
    typew("\nStarting in 3......")
    sleep(1)
    typew("2.....")
    sleep(1)
    typew("1")
    sleep(1)
    camera.start_preview()
    sleep(2)
    camera.capture(path)
    camera.stop_preview()
    typew("......Image captured\n")
    sleep(0.5)
    os.system("sudo feh \"{}\"".format(path))
    Start()

def captureOption():
        #Clear Terminal
        ClearTerminal()
        #Capture Option
        typew("\nOptions: \t\tValue\n1)Add text\t\t{}\n2)Brightness\t\t{}\n3)Contrast\t\t{}\n4)Text size\t\t{}\n5)Text Color\n6)Text Background Color\n7)Image Effect\t\t{}\n8)Exposure Mode\t\t{}\n9)Reset\n10)Back\n\nSelect: ".format(camera.annotate_text,camera.brightness,camera.contrast,camera.annotate_text_size,camera.image_effect,camera.exposure_mode))
        choose = input()
        #Text
        if choose == "1":
            typew("Text: ")
            text = input()
            camera.annotate_text = text
            captureOption()
        #Brightness
        elif choose == "2":
            typew("\nBrightness({}): ".format(camera.brightness))
            brightness = int(input())
            if brightness >= 0 and brightness <= 100:
                camera.brightness = brightness
            else:
                typew("\nPlease input within 0-100\n")
            captureOption()
        #Contrast
        elif choose == "3":
            typew("\nContrast({}): ".format(camera.contrast))
            contrast = int(input())
            if contrast >= 0 and contrast <= 100:
                camera.contrast = contrast
            else:
                typew("\nPlease input within 0-100\n")
            captureOption()
        #Text size
        elif choose == "4":
            typew("\nText size({}): ".format(camera.annotate_text_size))
            size = int(input())
            if size >= 6 and size <= 160:
                camera.annotate_text_size = size
            else:
                typew("\nPlease input within 6-160\n")
            captureOption()
        #Text color
        elif choose == "5":
            typew("\nText color: ")
            colortype = input()
            colorselection = ["red","green","blue","black","white","yellow","purple","pink","orange","brown","magenta","cyan","grey"]
            if colortype.lower() in colorselection:
                camera.annotate_foreground = Color(colortype.lower())
            else:
                typew("\nPlease type a valid color.\n")
            captureOption()
        #Text background color
        elif choose == "6":
            typew("\nText background color: ")
            colortype = input()
            colorselection = ["red","green","blue","black","white","yellow","purple","pink","orange","brown","magenta","cyan","grey"]
            if colortype.lower() in colorselection:
                camera.annotate_background = Color(colortype.lower())
            else:
                typew("\nPlease type a valid color.\n")
            captureOption()
        #Image Effect
        elif choose == "7":
            typew("\nEffect: none, negative, solarize, sketch, denoise, emboss, oilpaint, hatch, gpen, pastel, watercolor, film, blur, saturation, colorswap, washedout, posterise, colorpoint, colorbalance, cartoon, deinterlace1, and deinterlace2\n")
            typew("\nImage Effect({}): ".format(camera.image_effect))
            effect = input()
            EffectType = ["none", "negative","solarize","sketch","denoise","emboss","oilpaint","hatch","gpen","pastel","watercolor", "film", "blur", "saturation", "colorswap", "washedout", "posterise", "colorpoint","colorbalance", "cartoon", "deinterlace1", "deinterlace2"]
            if effect.lower() in EffectType: 
                camera.image_effect = effect.lower()
            else:
                typew("\nPlease type a valid effect.\n")
            captureOption()
        #Exposure Mode
        elif choose == "8":
            typew("\nExposure Type: off, auto, night, nightpreview, backlight, spotlight, sports, snow, beach, verylong, fixedfps, antishake, and fireworks\n")
            typew("Exposure Mode({}): ".format(camera.exposure_mode))
            mode = input()
            modeType = ["off", "auto", "night", "nightpreview", "backlight", "spotlight", "sports", "snow", "beach", "verylong", "fixedfps", "antishake","fireworks"]
            if mode.lower() in modeType:
                camera.exposure_mode = mode.lower()
            else:
                typew("\nPlease type a valid exposure mode.\n")
            captureOption()
        #Reset
        elif choose == "9":
            camera.annotate_text = ""
            camera.contrast = 0
            camera.brightness = 50
            camera.annotate_text_size = 32
            camera.annotate_foreground = Color("white")
            camera.annotate_background = None
            camera.image_effect = "none"
            camera.exposure_mode = "auto"
            typew("Done reset!!")
            captureOption()
        #Back
        elif choose == "10":
            Start()
        #Invalid option
        else:
            typew("Please type a valid selection")
            captureOption()

def record(seconds):
    #Clear Terminal
    ClearTerminal()
    #Image name
    typew("Image Name:\n1)Date and Time\n2)Custom\n3)Back\n")
    option = input()
    path = ""
    name = ""
    if option == "1":
        name = datetime.now()
        path = "{programpath}/Gallery/Videos/{filename}.h264".format(programpath=sys.path[0],filename=name)
    elif option == "2":
        typew("Enter the name you want: ")
        name = input()
        path = "{programpath}/Gallery/Videos/{filename}.h264".format(programpath=sys.path[0],filename=name)
    elif option == "3":
        Start()
    else:
        typew("Please enter a valid selection.")
        Start()
    #Start record
    camera.start_preview()
    camera.start_recording(path)
    sleep(int(seconds))
    camera.stop_recording()
    camera.stop_preview()
    print("path")
    if option == "1":
        os.system("avconv -r 30 -i \"{original}\" -vcodec copy \"{programpath}/Gallery/Videos/{filename}.mp4\"".format(original=path,programpath=sys.path[0],filename=name))
    elif option == "2":
        os.system("avconv -r 30 -i \"{original}\" -vcodec copy \"{programpath}/Gallery/Videos/{filename}.mp4\"".format(original=path,programpath=sys.path[0],filename=name))
    os.system("sudo rm \"{}\"".format(path))
    os.system("omxplayer \"{programpath}/Gallery/Videos/{filename}.mp4\"".format(programpath=sys.path[0],filename=name))
    Start()

#def typew(words):
#    for char in words:
#        #Typing speed
#        sleep(0.024)
#        sys.stdout.write(char)
#        sys.stdout.flush()
#        
#def typew(words,seconds):
#    for char in words:
#        #Typing speed
#        sleep(seconds)
#        sys.stdout.write(char)
#        sys.stdout.flush()
#

def typew(words,seconds=None,color=None,highlights=None,attr=None):
    if seconds == None:
        seconds = 0.1
    if color == None:
        color = "green"
    for char in words:
        if highlights == None and attr == None:
            sleep(seconds)
            sys.stdout.write(colored(char,color))
            sys.stdout.flush()
        elif highlights == None:
            sleep(seconds)
            sys.stdout.write(colored(char,color,attrs=attr))
            sys.stdout.flush()
        elif attr == None:
            sleep(seconds)
            sys.stdout.write(colored(char,color,highlights))
            sys.stdout.flush()
        else:
            sleep(seconds)
            sys.stdout.write(colored(char,color,highlights,attrs=attr))
            sys.stdout.flush() 

def Filecreate():
    newpath = "{}/Gallery".format(sys.path[0])
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    newpath = "{}/Gallery/Images".format(sys.path[0])
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    newpath = "{}/Gallery/Videos".format(sys.path[0])
    if not os.path.exists(newpath):
        os.makedirs(newpath)

def Start():
    #Create gallery
    Filecreate()
    #Clear Terminal
    ClearTerminal()
    #Main menu
    typew("\nWelcome to PiCam!!!\n")
    typew("\nPlease choose a function below: \n1)Preview\n2)Capture\n3)Record\n4)Options\n5)Exit\n\nSelect: ")
    option = input()
    #Preview
    if option.isdigit():
        if option == "1":
            typew("Preview will last for 5 seconds!!")
            sleep(2)
            preview()
        #Capture
        elif option == "2":
            capture()
        #Record
        elif option == "3":
            ClearTerminal()
            typew("\n\nHow long you want to record? (Seconds): ")
            time = input()
            record(time)
        #Options
        elif option == "4":
            captureOption()
        #Back
        elif option == "5":
            typew("\n\nThanks for choosing PiCam\n")
            ClearTerminal()
            exit()
        else:
            typew("\nPlease choose a valid option\n\n")
            Start()
    else:
        typew("Please enter a digit!")


def ClearTerminal():
    os.system("clear")

#Main Program
try:
    Start()
except KeyboardInterrupt:
    ClearTerminal()
    typew("\nThanks for choosing PiCam\n")
    ClearTerminal()

import cv2
import numpy as np
# import listening
import connect
import pyttsx3
from playsound import playsound

channel = connect.join()

def heardfunction():
    print ('you said no')

while(1):

    engine = pyttsx3.init()
    #engine.say("Indepedence, April first, eighteen hundred eighty four. The weather is cool and a breeze sweeps down the busy street full of settlers. Throughout the game you will always have 6 menu pins in the pin row closest to you with different textures on top that can be used to access different actions. Actions might not be available always, and if unavailable the height of the pin will be in a lowered state. You can always briefly press a pin to get the action read aloud, the action is selected by pressing the pin for a longer period. From left to right the pins provide access to: 1, Continue on trail. 2, Feel the map. 3, buy supplies. 4, Hunt for food. 5, Talk to people in the area")
    #engine.runAndWait()
    # recognition takes a function that is called when keyword is head, the keyword, and if it should keep listening for the keyword
    inputNum = input('1: Feel the map, 2: Continue on the trail, 3: Buy Supplies, 4: Hunt for food, 5: Talk to people nearby, 6: Check your inventory').lower()

    if inputNum == '1':
        # load image
        engine.say("A map will be physicalized in front of you shortly. The height of the pins refer to topology of the environment, high pins represent mountain ranges and noticeably lowered pins equals a river with no bridges. Your current location is indicated by the slowly pulsating pin, and your target of Oregon city with the fast pulsing pin. Traveling through rivers and across mountain tops will result in a shorter route but will present other risks that might endanger your travel. The route is entirely up to you to decide, after having traveled a distance equal to one pin you will select in what direction the caravan should head next. Each pin equals a distance of 30 miles and will take several days to travel dependent on weather conditions, the health of your oxen, state of your wagon and the geography in the area. Press down on a pin next to your starting position to select an initial direction. Once selected it will slowly pulsate along with your previously traveled route. Once ready to start your travel, press the Continue travel pin positioned left most, to start your journey or use some of the other options to buy additional supplies, interact with people or start hunting.")
        engine.runAndWait()
        for n in range(4): #play animation 3 times (moving pins)
            cap = cv2.VideoCapture('vid/JespersMap.avi', 0)
            while(cap.isOpened()):
                # read

                    ret, img = cap.read()
                    if ret:
                        # resize img for transform
                        img = cv2.resize(img, (16,24), interpolation = cv2.INTER_NEAREST)

                        # uncomment this to see image
                        #'''
                        cv2.imshow('image', img)
                        #'''
                        # flatten array
                        img = img.flatten()

                        # set the frame rate
                        cv2.waitKey(200)

                        # stringify for server
                        transformSend = ""
                        for i,ele in enumerate(img):
                            if i % 3 == 0:
                                transformSend+=(" "+str(ele))

                        # if you want to look at the numbers :)
                        print (transformSend)

                        # uncomment this to send to server
                        channel.push("input",{"body": transformSend})
                    else:
                        break
            cap.release()
            cv2.destroyAllWindows()

            #go back to menu screen
            img = cv2.imread('img/menu.jpg', 0)
            # resize img for transform
            #cv2.imshow('image', img)
            img = cv2.resize(img, (16,24), interpolation = cv2.INTER_NEAREST)
            img = img.flatten()
            transformSend = ""
            for ele in img:
                transformSend+=(" "+str(ele))
            # uncomment this to send to server
            channel.push("input",{"body": transformSend})
    elif inputNum == '2':
                # load image
        playsound('sound/Wagon.wav',False)
        cap = cv2.VideoCapture('vid/wagon.avi', 0)
        while(cap.isOpened()):
            # read
            ret, img = cap.read()

            if ret:
                # resize img for transform
                img = cv2.resize(img, (16,24), interpolation = cv2.INTER_NEAREST)

                # uncomment this to see image
                #'''
                cv2.imshow('image', img)
                #'''
                # flatten array
                img = img.flatten()

                # set the frame rate
                cv2.waitKey(1000)

                # stringify for server
                transformSend = ""
                for i,ele in enumerate(img):
                    if i % 3 == 0:
                        transformSend+=(" "+str(ele))

                # if you want to look at the numbers :)
                print (transformSend)

                # uncomment this to send to server
                channel.push("input",{"body": transformSend})
            else:
                break

        cap.release()
        cv2.destroyAllWindows()

        engine.say("April third, the rain is pouring down, but your party is at good health and making steady progress. You have now traveled 30 miles. You have camped on the flat prairie along with a few other travelers. Use the menu pins to select an action.")
        engine.runAndWait()
        #go back to menu screen
        img = cv2.imread('img/menu.jpg', 0)
        # resize img for transform
        #cv2.imshow('image', img)
        img = cv2.resize(img, (16,24), interpolation = cv2.INTER_NEAREST)
        img = img.flatten()
        transformSend = ""
        for ele in img:
            transformSend+=(" "+str(ele))
        # uncomment this to send to server
        channel.push("input",{"body": transformSend})
    elif inputNum == '3':
                # load image
        engine.say("Hello, I am Daniel. So your going to Oregon! I can fix you up with what you need: Oxen to pull your wagon, Cloth to keep you warm, Food for the trip and Ammunition to hunt with your rifle")
        engine.runAndWait()
        engine.say("In the mid of the table in front of you the total available space in your wagon will been marked with an empty square that has fourteen times 5 available spaces. Each of the five types of items will be physicalized in front of it in unique shapes from left to right in the following order: Oxen, Cloth [2 pins], Food [4 pins], Ammunition [1 pin], Spare parts [6 pins]. The number of pins in each icon directly translate to the amount of space (pins) the item takes up in your caravan, and via their height you can identify each type of object in your inventory. Press each object briefly to get information about the item and hold one or several of the pins of a given icon in order to purchase it.")
        engine.runAndWait()

        cap = cv2.VideoCapture('vid/Merchant.avi', 0)
        while(cap.isOpened()):
            # read
            ret, img = cap.read()

            if ret:
                # resize img for transform
                img = cv2.resize(img, (16,24), interpolation = cv2.INTER_NEAREST)

                # uncomment this to see image
                #'''
                cv2.imshow('image', img)
                #'''
                # flatten array
                img = img.flatten()

                # set the frame rate
                cv2.waitKey(1000)

                # stringify for server
                transformSend = ""
                for i,ele in enumerate(img):
                    if i % 3 == 0:
                        transformSend+=(" "+str(ele))

                # if you want to look at the numbers :)
                print (transformSend)

                # uncomment this to send to server
                channel.push("input",{"body": transformSend})
            else:
                break

        cap.release()
        cv2.destroyAllWindows()

        #go back to menu screen
        img = cv2.imread('img/menu.jpg', 0)
        # resize img for transform
        #cv2.imshow('image', img)
        img = cv2.resize(img, (16,24), interpolation = cv2.INTER_NEAREST)
        img = img.flatten()
        transformSend = ""
        for ele in img:
            transformSend+=(" "+str(ele))
        # uncomment this to send to server
        channel.push("input",{"body": transformSend})
    elif inputNum == '4':
                # load image
        engine.say("Hunting food require patience and high alertness. As you look across the prairie, the landscape of bushes and trees will be mapped out in front of you. Every high point indicate terrain features such as bushes, rocks and trees from which animals typically emerge. From time to time, an animal will slowly emerge on the prairie breaking the static landscape: as a hunter it’s your job to identify the animal and press it to shoot before it disappears behind another debris.")
        engine.runAndWait()
        engine.say("Let us get started!")
        engine.runAndWait()
        playsound('sound/Winchester.wav',False)
        cap = cv2.VideoCapture('vid/hunting.avi', 0)
        playsound('sound/Wind.wav',False)
        while(cap.isOpened()):
            # read
            ret, img = cap.read()

            if ret:
                # resize img for transform
                img = cv2.resize(img, (16,24), interpolation = cv2.INTER_NEAREST)

                # uncomment this to see image
                #'''
                cv2.imshow('image', img)
                #'''
                # flatten array
                img = img.flatten()

                # set the frame rate
                cv2.waitKey(1000)

                # stringify for server
                transformSend = ""
                for i,ele in enumerate(img):
                    if i % 3 == 0:
                        transformSend+=(" "+str(ele))

                # if you want to look at the numbers :)
                print (transformSend)

                # uncomment this to send to server
                channel.push("input",{"body": transformSend})
            else:
                break

        cap.release()
        cv2.destroyAllWindows()

        #go back to menu screen
        img = cv2.imread('img/menu.jpg', 0)
        # resize img for transform
        #cv2.imshow('image', img)
        img = cv2.resize(img, (16,24), interpolation = cv2.INTER_NEAREST)
        img = img.flatten()
        transformSend = ""
        for ele in img:
            transformSend+=(" "+str(ele))
        # uncomment this to send to server
        channel.push("input",{"body": transformSend})
    elif inputNum == '5':
                # load image
        playsound('sound/TraderJim.wav',False)
        for n in range(5): #play animation 3 times (moving pins)
            cap = cv2.VideoCapture('vid/Talking.avi', 0)
            while(cap.isOpened()):
                # read
                ret, img = cap.read()

                if ret:
                    # resize img for transform
                    img = cv2.resize(img, (16,24), interpolation = cv2.INTER_NEAREST)

                    # uncomment this to see image
                    #'''
                    cv2.imshow('image', img)
                    #'''
                    # flatten array
                    img = img.flatten()

                    # set the frame rate
                    cv2.waitKey(500)

                    # stringify for server
                    transformSend = ""
                    for i,ele in enumerate(img):
                        if i % 3 == 0:
                            transformSend+=(" "+str(ele))

                    # if you want to look at the numbers :)
                    print (transformSend)

                    # uncomment this to send to server
                    channel.push("input",{"body": transformSend})
                else:
                    break

        cap.release()
        cv2.destroyAllWindows()

        #go back to menu screen
        img = cv2.imread('img/menu.jpg', 0)
        # resize img for transform
        #cv2.imshow('image', img)
        img = cv2.resize(img, (16,24), interpolation = cv2.INTER_NEAREST)
        img = img.flatten()
        transformSend = ""
        for ele in img:
            transformSend+=(" "+str(ele))
        # uncomment this to send to server
        channel.push("input",{"body": transformSend})
    else:
        cv2.destroyAllWindows()
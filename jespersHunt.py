import cv2
import numpy as np
# import listening
import connect
from playsound import playsound

#np.set_printoptions(threshold=np.inf)

#channel = connect.join()

while(1):

    # recognition takes a function that is called when keyword is head, the keyword, and if it should keep listening for the keyword
    moreGoods = input('Do you want to go hunting?: ').lower()

    if moreGoods == 'yes':
        print ("SHOOT SHOOOT!")
        playsound('sound/winchester.wav')
        playsound('sound/cow.wav')

        # load image
        cap = cv2.VideoCapture('vid/hunting.avi', 0)
        init_flag = False
        while(cap.isOpened()):
            # read
            ret, img = cap.read()

            if ret:
                # resize img for transform
                img = cv2.resize(img, (16,24), interpolation = cv2.INTER_NEAREST)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                # add img together x3 for total transform
                #img = np.concatenate((img, img, img), axis=1)

                if init_flag == False:
                    init_state = np.copy(img)
                    cv2.imshow('init', init_state)
                    init_flag = True
                
                # uncomment this to see image
                #'''
                cv2.imshow('image', img)
                #cv2.waitKey()
                #'''

                #Finds differences from initial (static) frame and the following frames with animals moving
                dif = np.subtract(img, init_state)
                #cv2.imshow('dif', dif)
                correct = []

                #Threshold to identify pixels that are animals and not just noise
                for row,val in enumerate(dif):
                    for col,val2 in enumerate(val):
                        if 80 > val2 > 10:
                            correct.append((row,col))
                print(correct)

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
                #channel.push("input",{"body": transformSend})
            else:
                break

        cap.release()
        cv2.destroyAllWindows()

    else:
        print ("Too bad! You have to say yes for this demo to work :)")

cv2.destroyAllWindows()
import cv2
import numpy as np
# import listening
import connect


channel = connect.join()

def heardfunction():
    print ('you said no')

while(1):

    # recognition takes a function that is called when keyword is head, the keyword, and if it should keep listening for the keyword
    moreGoods = input('Do you want to purchase more of my goods?: ').lower()

    if moreGoods == 'no':

        # load image
        cap = cv2.VideoCapture('vid/hunting.avi', 0)
        while(cap.isOpened()):
            # read
            ret, img = cap.read()

            if ret:
                # resize img for transform
                img = cv2.resize(img, (16,24), interpolation = cv2.INTER_NEAREST)

                # add img together x3 for total transform
                img = np.concatenate((img, img, img), axis=1)

                # uncomment this to see image
                #'''
                cv2.imshow('image', img)
                #cv2.waitKey()
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
        print ("Well then, you're ready to start. Good luck! You have a long and difficult journey ahead of you.")

    else:
        print ("Too bad! You have to say no for this demo to work :)")

cv2.destroyAllWindows()
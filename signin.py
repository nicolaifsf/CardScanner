import sys
import time
import usb.core
import usb.util


VENDOR_ID = 0x0801
PRODUCT_ID = 0x0001
DATA_SIZE = 337


device = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)
if device is None:
        sys.exit("Could not find MagTek USB HID Swipe Reader.")

start = time.time()


#signin =[]
signin = set()

while(True):
    studentID = raw_input('user: ')
    if(studentID == "exit" or studentID == "quit"):
        break
    if(studentID[-5:] != "1227?" ):
        print "NOT AN NYU STUDENT"
 
    idd = 'N' + studentID[2:-6]
    if(idd in signin):
            print ("STUDENT SIGNED IN ALREADY")
    else:
        signin.add(idd)
        #signin.append(idd)

    print (idd)

    if(time.time() - start > 5):
        f = open('StudentList.txt','w')
        for item in signin:
            print >> f,item
        start = time.time()
        f.close()





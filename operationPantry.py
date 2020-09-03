from firebase import firebase
import serial

firebase = firebase.FirebaseApplication('https://operation-pantry.firebaseio.com/')

try:
    arduino_serial = serial.Serial("/dev/ttyACM1", 9600)
    print("Port ACM1")
except:
    try:
        arduino_serial = serial.Serial("/dev/ttyACM0", 9600)
        print("Port ACM0")
    except:
        arduino_serial = None
        print("Arduino port not detected")

def main():
    global arduino_serial
    try:
        if(arduino_serial is None):
            return 'error'.encode()
        while True:
           item = arduino_serial.readline().decode()
           result = firebase.post('operation-pantry', {'items':str(item)})
           print(item                     )
    except Exception as e:
        print(e)
        return 'error'.encode()
if __name__=="__main__":
    main()

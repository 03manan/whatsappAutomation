import pywhatkit as kit
import time


numbers = new_numbers = [
    "+919999999999",
    "+919999999999",
    "+919999999999",
    "+919999999999",
    "+919999999999",
    "+919999999999",
    "+919999999999",
    "+919999999999",
    "+919999999999"
]

message = ("Put message here")

def send_messages():
    for number in numbers:
        kit.sendwhatmsg_instantly(number, message)
       
        time.sleep(5) 

send_messages()
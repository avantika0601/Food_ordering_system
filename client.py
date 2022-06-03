import socket
import sys

def main():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "192.168.43.248"
    port = 8884

    try:
       
        soc.connect((host, port))
    except:
        
        print("Connection error")
        sys.exit()

    print("*****\n")
    print("\tWelcome to SNACKS JUNCTION\n")
    print("\tToday's Menu\n")
    print("\tFRIES - \t\tRs 60\n")
    print("\tPIZZA - \t\tRs 90\n")
    print("\tNACHOS - \t\tRs 50\n")
    print("\tBURGER - Rs 70\n")
    print("\tPASTA - \tRs 50\n")
    print("\tSANDWICH - \tRs 45\n")
    print("*****\n")

    dishes = {
            "fries":60,
            "pizza":90,
            "nachos":50,
            "burger":70,
            "pasta":50,
            "sandwich":45
            }

    print("Enter your name or 'quit' to exit")
    message = input()
    
    
    while message != 'quit':
        total=0
        print("Enter your order from the menu separated by a ,")
        message_order = input(" -> ")
        print(message_order)
        message_order = message_order.lower()
        for m in message_order.split(","):
              item,quantity = m.split(" ")
              if(item in dishes):
                 total = total + (dishes.get(item)*int(quantity))
    
     
        soc.sendall(message.encode("utf8"))
        message_order = " " + message_order
        soc.sendall(message_order.encode("utf8"))
        if soc.recv(5120).decode("utf8") == "-":
             pass        # null operation
        print("Order Successfully placed")
        print("Grand Total")
        print(total)
        print("Enter your name or 'quit' to exit")
        message = input(" -> ")

    soc.send(b'--quit--')


main()
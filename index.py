from list_3_2 import Pinger
import list_3_4
import list_3_5

def init():
    while True:
        print()
        print("MENU PILIHAN:")
        print("1. Mengetahui delay ke suatu alamat")
        print("2. Mengetahui list interface")
        print("3. Mengetahui alamat IP")
        print("4. Exit")
        print()
        pilihan=int(input("Masukkan pilihan: "))
        print()
        if (pilihan==1):
            nama_web=str(input("Masukkan alamat web: "))
            pinger = Pinger(target_host=nama_web)
            pinger.ping()
        elif (pilihan==2):
            interfaces = list_3_4.list_interfaces()
            print ("This machine has %s network interfaces: %s." %(len(interfaces),interfaces))
        elif (pilihan==3):
            ifname = str(input("Masukkan interface: "))
            print ("Interface [%s] --> IP: %s" %(ifname, list_3_5.get_ip_address(ifname)))
        elif (pilihan==4):
            print("Bye.")
            break
        else:
            print("Pilihan %s tidak ada"%pilihan)

if __name__ == '__main__':
    init()
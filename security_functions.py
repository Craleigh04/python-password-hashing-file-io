# imports hashlib and defines and creates my functions to be used in the main
import hashlib
# take password string input using utf convet to byte to allow hash 
def hash_password(password):
    try:
        password = password.encode("utf-8") 
        my_hash = hashlib.md5(password)
        hash_value = my_hash.hexdigest()
        with open("hashed_password.txt", "w") as file:
            file.write(hash_value + "\n")
        return hash_value
    except:
        print("An error occurred.")
        return None
# function writes dictionary to provide both key and value 
def write_mac_info():
    about_my_mac = {"Model": "Macbook Pro", "Processor": "2.4 GHz 9-core", "Memory": "16 GB"}
    try:
        with open("aboutmymac.txt", "w") as file:
            for key, value in about_my_mac.items():
                file.write(key + " : " + value + "\n")
    except:
        print("An error occurred while writing the file.")
# function opens file in read mode and splits into parts using replace remove \n chracter
def read_mac_info():
    try:
        mac_info = {}
        with open("aboutmymac.txt", "r") as file:
            for line in file:
                parts = line.split(" : ")
                key = parts[0]
                value = parts[1].replace("\n", "")  # Had help with co.pilot for the replace method
                mac_info[key] = value  #key and cleaned valu stored 
        return mac_info
    except:
        print("An error occurred while reading the file.")
        return None
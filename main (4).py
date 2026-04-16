# main program that gets the input and then calls the functions 
import functions1

# Prompt for password and hash it
password = input("Please enter your password: ")
hashed = functions1.hash_password(password)
if hashed:
    print("Hashed password saved.")

# Write Mac info to file
functions1.write_mac_info()
print("Mac info written to file.")

# Read Mac info from file
mac_info = functions1.read_mac_info()
if mac_info:
    print("Read from file:", mac_info) 
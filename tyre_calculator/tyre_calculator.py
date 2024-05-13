import os

def tyre_width():
    while True:
        try:
            tirewidth = int(input("Tire width: (215, 235, etc)\n"))
        except ValueError:
            print("Please enter a valid number")
            continue
        break
    return tirewidth
        
def tyre_profile():
    while True:
        try:
            tireprofile = int(input("Tire profile: (40, 45, etc)\n"))
        except ValueError:
            print("Please enter a valid number")
            continue
        break
    return tireprofile

def rim_size():
    while True:
        try:
            rim = int(input("Wheel size: (17, 18, etc)\n"))
        except ValueError:
            print("Please enter a valid number")
            continue
        break
    return rim

def conversion(width, profile, wheel_size):
    width_meters = width * 0.001
    tyre_meters = profile * 0.01
    wheel_meters = (wheel_size / 2) * 0.0254
    converted_wheel = ((wheel_size + 1) / 2) * 0.0254
    converted_profile = wheel_meters + width_meters * tyre_meters
    print(f"\nWIDTH={width_meters}\nRADIUS={converted_profile:.4f}\nRIM_RADIUS={converted_wheel}")
    print()
    print("Creating tyres text file")
    print()
    tyres = open("tyres.txt", "w")
    tyres.write("WIDTH=" + str(width_meters) + "\nRADIUS=" + str("%.4f" % converted_profile) + "\nRIM_RADIUS=" + str(converted_wheel))
    tyres.close
    

def main():
    
    width = tyre_width()
    profile = tyre_profile()
    wheel_size = rim_size()
    
    conversion(width, profile, wheel_size)

    os.system("pause")

main()

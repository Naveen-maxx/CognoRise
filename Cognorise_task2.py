import qrcode
import cv2
import numpy as np

def generate(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)
    print(f"QR Code was sucessfully generated and saved as {filename}")

def decode(filename):
    img = cv2.imread(filename)
    detector = cv2.QRCodeDetector()
    
    data, vertices_array, binary_qrcode = detector.detectAndDecode(img)
    
    if vertices_array is not None:
        print(f"QR Code was sucessfully detected, data: {data}")
    else:
        print("No QR Code detected")

def main():
    while True:
        choice = input("Enter 'e' to encode data into QR code\nEnter 'd' to decode a QR code\nEnter 'q' to quit: ").lower()
        
        if choice == 'e':
            data = input("Enter the data to encode into the QR code: ")
            filename = input("Enter the filename to save the QR code: ")
            generate(data, filename)
        
        elif choice == 'd':
            filename = input("Enter the filename of the QR code to decode: ")
            decode(filename)
        
        elif choice == 'q':
            print("Exiting...Good Bye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

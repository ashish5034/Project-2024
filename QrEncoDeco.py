import qrcode
import cv2

# *********************************************************************************************************
# import qrcode: This line imports the qrcode module, which provides functionality to generate QR codes.
# import cv2: This line imports the OpenCV library, which is used for image processing tasks, including reading and decoding images.
# *********************************************************************************************************

def encode_text(text, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=50,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

    print(f"QR code generated and saved as {filename}")

# *********************************************************************************************************
# def encode_text(text, filename):: This line defines a function named encode_text that takes two parameters: text (the text to encode into a QR code) and filename (the name of the file to save the QR code image).

# qr = qrcode.QRCode(...): This block initializes a QRCode object with specific parameters such as version, error correction level, box size, and border.

# qr.add_data(text): This line adds the text to the QR code object.

# qr.make(fit=True): This line generates the QR code image.

# img = qr.make_image(fill_color="black", back_color="white"): This line creates an image representation of the QR code with specified fill color (black) and background color (white).

# img.save(filename): This line saves the generated QR code image with the specified filename.

# print(f"QR code generated and saved as {filename}"): This line prints a message indicating that the QR code has been generated and saved.
# *********************************************************************************************************

def decode_image(filename):
    image = cv2.imread(filename)
    detector = cv2.QRCodeDetector()

    data, bbox, _ = detector.detectAndDecode(image)

    if bbox is not None:
        print(f"QR code detected with data: {data}")
    else:
        print("No QR code detected")

# *********************************************************************************************************
# def decode_image(filename):: This line defines a function named decode_image that takes a filename as a parameter.

# image = cv2.imread(filename): This line reads the image file specified by the filename using OpenCV's imread() function.

# detector = cv2.QRCodeDetector(): This line creates a QRCodeDetector object from OpenCV, which will be used to detect and decode QR codes in images.

# data, bbox, _ = detector.detectAndDecode(image): This line attempts to detect and decode a QR code in the provided image. It returns the decoded data, bounding box coordinates, and a tuple indicating the status of the detection.

# if bbox is not None:: This line checks if a QR code is detected in the image by verifying if the bounding box coordinates are not None.

# print(f"QR code detected with data: {data}"): This line prints the decoded data if a QR code is detected.

# else:: This line handles the case where no QR code is detected in the image.

# print("No QR code detected"): This line prints a message indicating that no QR code was found in the image.
# *********************************************************************************************************

def main():
    while True:
        print("1. Encode text to QR code")
        print("2. Decode QR code from image")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            text = input("Enter the text to encode: ")
            filename = input("Enter the filename to save the QR code image: ")
            encode_text(text, filename)
        elif choice == "2":
            filename = input("Enter the filename of the QR code image: ")
            decode_image(filename)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")
            
if __name__ == "__main__":
    main()

# *********************************************************************************************************
# def main():: This line defines the main function of the program where the user interface and interaction with the user are implemented.

# while True:: This line starts an infinite loop to repeatedly prompt the user for options until the user chooses to quit.

# print("1. Encode text to QR code"): This line prints the first menu option for encoding text into a QR code.

# print("2. Decode QR code from image"): This line prints the second menu option for decoding a QR code from an image.

# print("3. Quit"): This line prints the third menu option for quitting the program.

# choice = input("Enter your choice: "): This line prompts the user to enter their choice from the menu options.

# if choice == "1":, elif choice == "2":, elif choice == "3":: These lines check the user's input and call the corresponding functions based on the selected option.

# print("Invalid choice"): This line handles the case where the user enters an invalid choice.

# if __name__ == "__main__":: This line checks if the script is being run directly by the Python interpreter (not imported as a module into another script).

# main(): This line calls the main() function if the script is being run directly, initiating the execution of the program.
# *********************************************************************************************************
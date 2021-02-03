#read QR Code from image

import cv2

def qrreader(image):
    img = cv2.imread(image)
    detector = cv2.QRCodeDetector()
    data , bbox , _ = detector.detectAndDecode(img)
    return data

print(qrreader('QR Code.png'))

import pyqrcode

def qrcode(data):
    q = pyqrcode.create(data)
    q.png('QR Code.png' , scale = 1)
    print('QR Code Generated!!')
    
data = "https://youtube.com/playlist?list=PLVG0Zju2HPJfW2rqtu330DD-MaPk-bvMZ"
qrcode(data)



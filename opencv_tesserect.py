import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('DSC_7213.JPG')
img = cv2.medianBlur(img,3)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img_red = img[:,:,2]
# img_green = img[:,:,1]
# img_blue = img[:,:,0]

equ = cv2.equalizeHist(img_gray)
# ret, img_thre = cv2.threshold(equ, 50, 200, cv2.THRESH_BINARY)
img_thre = cv2.adaptiveThreshold(equ,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,35, 35)
text = pytesseract.image_to_string(img_thre)
print(text)

img_show = cv2.resize(img_thre, (0,0), fx=0.2, fy=0.2)

cv2.imshow("test",img_show)
cv2.waitKey(0)
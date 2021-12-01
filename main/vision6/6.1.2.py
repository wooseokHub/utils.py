import numpy as np, cv2, time
def pixel_access1(image):
    image1 = np.zeros(image.shape[:2], image.dtype)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            pixel = image[i, j]
            image1[i, j] = 255 - pixel
    return image1
def pixel_access2(image):
    image1 = np.zeros(image.shape[:2], image.dtype)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            pixel = image.item(i,j)
            image1.itemset((i,j),255-pixel)
    return image1
def pixel_access3(image):
    lut =[255-i for i in range(256)]
    lut = np.array(lut,np.uint8)
    image1=lut[image]
    return image1
def pixel_access4(image):
    image1 = cv2.subtract(255,image)
    return image1
def pixel_access5(image):
    image1= 255-image
    return image1
image = cv2.imread("../images/ch6/bright.jpg",cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")
def time_check(func, msg):
    start_time= time.perf_counter()
    ret_img = func(image)
    elapsed = (time.perf_counter()-start_time)*1000
    print(msg,"수행시간 : %0.2f ms" % elapsed)
    return ret_img

image1 = time_check(pixel_access1,"[방법1] 직접 접근 방식")
image2 = time_check(pixel_access2,"[방법2] item() 함수 접근")
image3 = time_check(pixel_access3,"[방법3] 룩업테이블 방식")
image4 = time_check(pixel_access4,"[방법4] OpenCV 함수 방식")
image5 = time_check(pixel_access5,"[방법5] ndarray 연산 방식")


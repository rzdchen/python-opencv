import cv2

value = 20

def Beauty(path, filename):
    img = cv2.imread(path)
    img_res = cv2.bilateralFilter(img, value, value * 2, value / 2)
    filename = './static/out/{}'.format(filename)
    cv2.imwrite(filename, img_res)
    # cv2.imshow('img', img_res)
    # cv2.waitKey(0)
    return filename

if __name__ == '__main__':
    Beauty("./static/origin1.jpg", '1')

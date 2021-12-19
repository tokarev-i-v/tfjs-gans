import cv2
import os
import glob
import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)

#finds all .png images in folder, and resize them using cv2
def resize_images_in_folder(in_dir, out_dir, im_size):
    filenames = glob.glob(os.path.join(in_dir, "*.png"))
    for fname in filenames:
        print(fname)
        file_name = os.path.basename(fname)
        img = cv2.imread(fname)
        resized = cv2.resize(img, (im_size, im_size),  interpolation = cv2.INTER_AREA )
        cv2.imwrite(os.path.join(out_dir, file_name), resized)

#finds all .png images in folder, and grayscale them using cv2
def grayscale_images_in_folder(in_dir, out_dir):
    filenames = glob.glob(os.path.join(in_dir, "*.png"))
    for fname in filenames:
        print(fname)
        file_name = os.path.basename(fname)
        img = cv2.imread(fname)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(os.path.join(out_dir, file_name), gray)

#
def create_one_big_image_from_dataset(in_dir, out_dir, img_name, low_bound = None, high_bound = None):
    filenames = glob.glob(os.path.join(in_dir, "*.png"))
    out_img = np.array([])
    img_shape = 1
    if(filenames[0]):
        img_shape = cv2.imread(filenames[0]).shape[0]
    
    counter = 1
    for fname in filenames:
        if low_bound and counter <= low_bound:
            counter += 1
            continue
        file_name = os.path.basename(fname)
        img = cv2.imread(fname)
        img = img.flatten()
        img = img[::3]
        out_img = np.append(out_img, img)
        print(f"{counter} {fname}")
        if high_bound:
             if counter == high_bound:
                break
        counter += 1
           
            
    out_img = out_img.reshape((-1, img_shape**2))
    #print("ответ:", out_img, out_img.shape)
    print("Done")
    #cv2.imshow("Результат", out_img)
    #cv2.waitKey(0)
    #cv2.displayAllWindows()
    cv2.imwrite(os.path.join(out_dir, img_name), out_img)

def show_big_image(im_path):
    img = cv2.imread(im_path)
    print(img.shape)

def merge_images (pathes, img_save_path):
    big_img = None
    if pathes[0]:
        big_img = cv2.imread(pathes[0])
        for path in pathes[1:]:
            img = cv2.imread(path)
            big_img = np.vstack((big_img, img))
    cv2.imwrite(img_save_path, big_img)
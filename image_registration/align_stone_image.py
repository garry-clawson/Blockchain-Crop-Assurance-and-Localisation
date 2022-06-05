# =========== Credit to pyimagesearch ============

# https://pyimagesearch.com/2020/08/31/image-alignment-and-registration-with-opencv/

# =====================================================

# USAGE
# python3 align_stone_image.py --template images/template_ground_stone_plan_view.jpeg --image images/template_ground_stone_90_degree_rotated_45_degree_incline_side_view.jpeg

# import the necessary packages
from alignment import align_images
import numpy as np
import argparse
import imutils
import cv2
import time
import base64


start = time.time()

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image that we'll align to template")
ap.add_argument("-t", "--template", required=True,
	help="path to input template image")
args = vars(ap.parse_args())

# load the input image and template from disk
print("[INFO] loading images...")
image = cv2.imread(args['image'])
template = cv2.imread(args['template'])

# align the images
print("[INFO] aligning images...")
aligned = align_images(image, template, debug=True)

# resize both the aligned and template images so we can easily
# visualize them on our screen
aligned = imutils.resize(aligned, width=700)
template = imutils.resize(template, width=700)

# our first output visualization of the image alignment will be a
# side-by-side comparison of the output aligned image and the
# template
stacked = np.hstack([aligned, template])

# our second image alignment visualization will be *overlaying* the
# aligned image on the template, that way we can obtain an idea of
# how good our image alignment is
overlay = template.copy()
output = aligned.copy()
cv2.addWeighted(overlay, 0.5, output, 0.5, 0, output)

# show the two output image alignment visualizations
# cv2.imshow("Image Alignment Stacked", stacked) 
cv2.imshow("Image Alignment Overlay", output)

print("Success ...")

# Convert image ot base64 which will be kept in IPFS
#with open("ipfs_test_image.jpeg", "rb") as img_file:
b64_string = base64.b64encode(image.read())
#print(b64_string)

end = time.time()
print("Time to align Image: ", end - start)


cv2.waitKey(0)


# ------------------------------- Things to tie up --------------------------
# Once match success push stacked image to the IPFS and get the hash (UploadIPFS.py)
# Pass the hash ImageCall.py to add to the smart contract in the blockchain (ImageCall.py)
# To show it is in the IPFS use GetListItem function from ImageCall.py to call the last list item in the smart contact list (IPFS hash of image)
# 
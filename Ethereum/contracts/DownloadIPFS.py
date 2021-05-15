import requests
import json
import base64



# -------------------Convertn image to base64 then upload to IPFS ---------------------

# Convert image ot base64 which will be kept in IPFS
with open("STONE_TEMPLATE.jpeg", "rb") as img_file:
    b64_string = base64.b64encode(img_file.read())
#print(b64_string)




# -------------------Adds base64 of image to IPFS then prints hash ---------------------

files = {
	'file': (b64_string)
}


#files = {
#	'file': ('STONE_TEMPLATE.jpeg')
#}


# Add further meta dat to the file project where required
#files = {
#    'fileOne': ('Item 1 of metadata'),
#    'fileTwo': ('''Congrats! This is the first sentence),
#}


# Free service to post items to IPFS
response = requests.post('https://ipfs.infura.io:5001/api/v0/add', files=files)

p = response.json()

hash = p['Hash']

print(hash)





# -------------------Get base64 data form IPFS and convert to image ---------------------


# Use the IPFS hash to find the base64 data in IPFS
params = ('arg', hash),

response = requests.post('https://ipfs.infura.io:5001/api/v0/get', params=params)

#print(response.text)


# -------------------Convertn  form base64 to image and put in directory ---------------------

# Convert image fomr base64 to jpeg which will be used 
with open("imageToUse.jpeg", "wb") as fh:
    fh.write(base64.decodebytes(b64_string))



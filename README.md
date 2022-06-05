# Blockchain Crop Assurance and Localisation

This project is a proof-of-concept infield localisation pipeline using smart contracts deployed on the Ethereum network to notarise, store and retrieve images from the Interplanetary File System (IPFS) that have been successfully aligned to show a localisation match within an infield environment. Localisation is achieved by using images of ground stones taken adjacent to planted seeds to enable sub GNSS accuracy without expensive hardware requirements such as RTK-GNSS. This offers a novel way for low ground coverage crops such as onion or asparagus to be re-identified to provide potential for improved supply chain assurance.  

## Table of Contents
* [Demonstration Video](#demonstration)
* [How to Install and Run the Project](#how-to-install-and-run-the-project)
* [How to Use the Project](#how-to-use-the-project)
* [Suggested Improvements](#suggested-improvements)
* [Acknowledgements](#acknowledgements)
* [Licence](#licence)


## Demonstration Video

https://user-images.githubusercontent.com/44243266/172064632-ac9f9f0a-d460-4c8c-9944-084043ed0105.mp4

## How to Install and Run the Project
This installation guide is a quick start to get you onto the right path to build you own smart contracts. This will take you through each of the steps required to replicate the vision localisation pipeline. Web3 libraries and several decencies will be required as well as supporting tool chains. These should be widely available for your chosen operating system. 

With the guide below you should be able to get the pipeline working, experience smart contracts for yourself as well as run your own blockchain (and see it operate in real time), even with limited experience. If you see any errors they are my own. Please feel free to make a pull request to improve this document. 

### 1. Install Node.js
To install Node.js, visit [nodejs.org](https://nodejs.org/en/) and follow the instructions for your operating system.

### 2. Install Truffle and Gananche
After you have installed Node.js, type the following command into your terminal to install Truffle:

```
npm install truffle -g
```

Check that you have correctly installed it by reviewing the version:

```
truffle version
```

You should hopefully see something similar to the below in your terminal:

```
Truffle v5.5.17 (core: 5.5.17)
Ganache v^7.1.0
Solidity - 0.8.14 (solc-js)
Node v16.15.1
Web3.js v1.5.3
```

Truffle comes with a client version of Ganache but you should ideally get the GUI. You should install this from the [trufflesuite.com/ganache/](https://trufflesuite.com/ganache/) website. Then follow the instructions for your own operating system. 

### 3. Start your own project

To start your own project, change directory into a project folder (create a new empty folder on your desktop if you have not got one). The open a terminal in that folder and type:

```
truffle init
```
This will create a new project which will will now have 3 x new folders and a js config file. These will be called, 'contracts', 'migrations', 'test' and 'truffle-config.js'. 

The contracts folder will contain the contracts, the migrations folder will contain the deployment files. The tests is a place write to test the logic of the contracts before they go into production.

Before we start the next step is tho amend the truffle-config.js file. Here, we need to un-comment the part of the configuration file (truffle-config.js) where we define the network to be used. Make sure that the below line (around line 45) is un-commented:

```
host: "127.0.0.1", // Localhost (default: none)
```

### 4. Compile the smart contract

This is the exciting bit! The best place to begin is by cloning this repo and taking the files provided as the project you created in step 3 (assuming it was on a folder on your desktop) will require several of the files in this repo. 

You can do this by either the GitHub desktop tool or by installing Git on your system and typing:

```
git clone https://github.com/garry-clawson/Blockchain-Crop-Assurance-and-Localisation.git
```

You will then have all the files needed when copying and pasting across into your project folder. 

First, take the ```ImageStore.sol``` and place into your ```contracts``` folder. 

Second, take the ```2_deploy_contract.js``` and paste place into your ```migrations``` folder. The '2' at the start of the file name indicates that this is the 2nd file to be compiled (this is how Truffle knows the ordering of compilation). 

The ```ImageStore.sol``` file is a Solidity program ([Solidity](https://docs.soliditylang.org/en/v0.8.14/) is one programming language you can use to develop smart contracts on the Ethereum blockchain), and has three simple functions: ```addItem()```, ```getListItem()``` and ```getListSize```. 

* ```addItem()``` appends a string to a list that was created at the very top of the contract. This is used to keep on adding new images content identifiers (CID) to the contract. 

* ```getListItem()``` returns the CID string of an indexed element in the List data structure. The CID is a the returned value we get when we have uploaded our image to the [Interplanetary File System (IPFS)](https://ipfs.io). This is our decentralized storage that we call on to host our data. 

* ```getListSize``` returns the size of the List. This is mainly used to see how many CIDs we have stored in our contract. 

To compile the project type the following in your terminal:

```
truffle compile
```

If it has compiled successfully you should have something like the below in your terminal:

```
Compiling your contracts...
===========================
> Compiling ./contracts/ImageStore.sol
> Compiling ./contracts/Migrations.sol
> Artifacts written to /Users/garryclawson/Desktop/Project/build/contracts
> Compiled successfully using:
   - solc: 0.5.16+commit.9c3226ce.Emscripten.clang
```

If you do have any trouble there is plenty of support on the web. An item that may cause an issue is stating the default compiler. To remove this issue, comment out line 87 in the ```truffle-config.js``` file so that the default compiler for truffle was being used. 

Now that you have compiled your project you will see one new folder ```build/contracts``` that contains two new files ```ImageStore.json``` and also ```Migrations.json```. 

These are for the contract artifacts, which hold all the necessary information for deploying and interacting with the contracts.

### 5. Deploy the contract to Ganache

[Ganache](https://trufflesuite.com/ganache/) is a locally hosted blockchain used for development of smart contracts as well as other testing requirements. Here we are safe to deploy and try out all of our contract requirements safe in the knowledge that we will not be spending any 'actual' funds. Ganache also allows us to connect our projects so that we can see what is happening under the hood in the smart contract, as well as estimate the Gas costs required for each stage of deployment and interaction with the smart contract (i.e. writing to it to append the list). 

To deploy the contract to Ganache, type the following:

```
truffle migrate
```
If everything to plan, we should see that in Ganache that the contract has been sent to the blockchain and current block height has incremented. To see the actual contract state you will need to add a workspace to the Ganache GUI. The 'Contracts' tab on the GUI will take you through how to do this (2 very simple steps that takes less than 10 seconds). 

The contract has now been deployed and is ready for us to use as we wish. The next steps will be interacting with the contract by adding an image Base64 string, but first, we need to get our images and complete a sample alignment (using OpenCV), which acts as a key part of the localisation pipeline. 

### 6. Interacting with the smart contract

The smart contract can be interacted with via the terminal using Truffle commands, however we want to interact with the contract in a more automated way. This allows us to build broader pipelines and extend the project. To interact with smart contracts we will use ```web3``` tooling, specifically ```web3.py``` To install tyep the following into your terminal:

```
pip install web3
```

Note: You will need to have ```pip``` installed to use pip. For more information about web3 go to [web3.readthedocs](https://web3py.readthedocs.io/en/stable/quickstart.html). 

Now that web3 is installed. We can copy then ```retrieve_image_cid.py``` and ```add_image_cid.py``` and paste these files into your ```project > smart_contract``` project folder. 

The ```retrieve_image_cid.py`` script asks for you smart contract address (this can be found on the 'Contracts' tab next to the ImageStore contract and and also a CID (such as ```QmWmXVKwg3PypTWNt9GSWvZHftDTEbJSyBkXH4rGaUFnh9```) to append the list within the smart contract. This content identified (CID) and is specific to the image uploaded to IPFS. The act of appending this value to the blockchain is effectively notorising it.

#### Add an image CID to the smart contract

To run ```add_image_cid.py``` open a terminal and change directory to the project folder and type:

```
python add_image_cid.py
```

You will then be asked to enter you Ethereum ImageStore contract address and CID. Once entered this information you should get something simular to the below:

```
Enter your Ethereum ImageStore contract address: 0xA40e776DDAB373960dA5F6FC170743A9DAe51204
List size:  2
CID added:  QmcBRbromnTm4dGRzrH2mFJCCwFBxBwhyegRoDGefdbC62
tx_hash: 0x9585e039227b6cb19e1492fe61a6dbe601a033e1cb2d36f014aa091526623392
```

We can see from the above that there are 2 items in the list (the list starts at 1 and not 0), and the last list item is ```QmcBRb...``` and it has an associated transaction hash of ```0x9585e0...```. This last value is the associated transaction in the blockchain and can be seen when inspecting transactions on the Ganache GUI. 

If there is an error, it is most likely due to the contract having an empty list and the ListSize() function returning an exception. To avoid this make sure you first add a CID to the smart contract first by following the pipeline process outlined in 'Putting it all together'. 

#### Retrieve an image CID from the smart contract

To run ```retrieve_image_cid.py``` open a terminal and change directory to the project folder and type:

```
python retrieve_image_cid.py
```

You will then be asked to enter you Ethereum ImageStore contract address and the position of the CID in the list. Once entered this information you should get something similar to the below:

```
Enter your Ethereum ImageStore contract address: 0xA40e776DDAB373960dA5F6FC170743A9DAe51204
List size:  2
CID:  QmcBRbromnTm4dGRzrH2mFJCCwFBxBwhyegRoDGefdbC62
```

For this proof-of-concept no optimization has been completed. We are currently using a very simple list structure. In Solidity there is no simple way to search a list for as each step will incur a Gas cost. Other data structures will offer a better way to do this. 


### 7. Aligning an image

The image alignment process was inspired by the pyimagesearch [tutorial](https://pyimagesearch.com/2020/08/31/image-alignment-and-registration-with-opencv/) for document image alignment and registration. The concept of aligning infield ground stones and using the same type of registration is compelling as low cost method to localize using only a vision system. 

To align an image the ``` align_stone_image.py``` script is called. To call this script the following usage is required:

```
python3 align_stone_image.py --template images/template_ground_stone_plan_view.jpeg --image images/template_ground_stone_90_degree_rotated_45_degree_incline_side_view.jpeg
```

Here, we are taking a template image ```template_ground_stone_plan_view.jpeg``` (this is an image that has been taken by the robot when planting the seed and is a direct plan view adjacent to the planting site), and comparing it to a newly current taken image ```template_ground_stone_90_degree_rotated_45_degree_incline_side_view.jpeg```. 

If the image is successfully able to be aligned then a ```Success...``` message will be shown. The newly current taken image is heavily rotated and banked to show the full alignment process. In practice, as the robot moves up and down a row it a newly taken image will be very similar (i.e. directly overhead) to the template image taken during seeding. 

Since this image (given as an example) is successful, we shall now upload it to IPFS. Further images to test alignment are available in the ```image_registration > images > additional_images``` folder. 

### 8. Upload image to IPFS

The IPFS is accessible via an Infura API endpoint. When ever a user uploads text, files, images etc to IPFS a content identifier (CID) is returned. This looks similar to ```QmcBRbromnTm4dGRzrH2mFJCCwFBxBwhyegRoDGefdbC62```. This CID is what is uploaded to the smart contract described in Step 6. 

The ```ipfs_upload.py``` file is used to upload an image to IPFS. This takes an image (currently the ```template_ground_stone_plan_view.jpeg``` image used as an example, but this should be your successfully aligned image). To run the script using the example image open a terminal and change directory to the ```Project > ipfs``` folder. Then type:

```
python3 ipfs_upload.py
```

You should then get returned a CID as described above. 

### 9. Download an image from IPFS

Downloading an image from IPFS is almost exactly the same as uploading, except that we are getting rather than adding. We use the same Infura API for access and take a content identifier (CID) as seen in step 8 to find the requested file. Since we are using an example image and will be writing this to the same folder as the ```template_ground_stone_plan_view.jpeg```, we will call this returned image ```returned_template_ground_stone_plan_view.jpeg```. Line 27 declares in the get_image() function states where this image should be written to. To download an image type the following into your terminal:

```
python3 ipfs_download.py
```

## How to Use the Project

The installation section above describes how to get all the pieces of the pipeline. However, they are in a natural order for understanding the system and getting it working but not for operating the pipeline. This section will describe what part to run in what order to see a successful pipeline flow. This order is as follows:

#### Prepare the pipeline
1. Create your smart contract (steps 1-5)
2. Upload a template image to IPFS get returned CID (step 8)
3. Add the CID of template image to the list in the smart contract (step 6)

#### Execute the pipeline
4. Take a current image and save to images directory (this will be compared - aligned - to the template image)
5. Recall the CID of the template image from the smart contract (step 6)
6. Download the template image from IPFS (step 9)
7. Align the current image with the template image (step 7)
8. If all goes well and alignment is successful, upload the current image to IPFS (step 8)
9. Repeat the process from stage 4-8 (Note: to do this you will need a collection of template images)

## Suggested Improvements

Multiple improvements can be made to this pipeline in the underlying scripts and the smart contracts to make the system automated. A few ideas are below:

* Improve the alignment process on ground stones - this is currently very simple and enhanced feature detection and segmentation would improve the accuracy (note, we are not looking to see if the images are the same, just if they can be aligned to a high accuracy)
* Build in an accuracy model to provide a Yes/No result for image alignment
* Identify a better way to take images to achieve an improved alignment accuracy (currently, this is a static camera on the front of the open hardware robot). 
* Use GNSS to identify what template image is required and call it from IPFS (this will need an interaction with the smart contract to get the relevant CID)
* Create a better way to get a relevant CID from the list in the smart contract
* Automate the pipeline so that once a current image is taken it will automatically feed through the alignment, storage and smart contract process


## Acknowledgements

The following medium posts [[1]](https://medium.com/coinmonks/creating-and-deploying-smart-contracts-using-truffle-and-ganache-ffe927fa70ae), [[2]](https://medium.com/thecryptoelement/developing-a-todo-list-dapp-in-ethereum-e4daf8a9ea5c), [[3]](https://medium.com/swlh/develop-test-and-deploy-your-first-ethereum-smart-contract-with-truffle-14e8956d69fc) and documents [[4]](https://trufflesuite.com/docs/truffle/quickstart/) were extremely useful when writing up this overview. Additionally, online resources [[5]](https://trufflesuite.com/docs/truffle/quickstart/), [[6]](https://nodejs.org/en/), [[7]](https://trufflesuite.com/ganache/), [[8]](https://www.dappuniversity.com/articles/web3-py-intro), [[9]](https://opencv.org)  and [[10]](https://pyimagesearch.com/2020/08/31/image-alignment-and-registration-with-opencv/) were extremely useful for putting the project together.

## Licence

This project is licensed under the [GNU General Public License v3.0](LICENCE)

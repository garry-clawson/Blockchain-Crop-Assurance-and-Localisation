# Towards Blockchain Enabled Infield Localisation

This project is a proof-of-concept infield localisation pipeline using smart contracts deployed on the Ethereum network to notarise, store and retrieve images from the Interplanetary File System (IPFS) that have been correctly aligned to show a localisation match within an infield environment. Localisation is achieved by using ground stones adjacent to planted seeds to enable sub GNSS accuracy without expensive hardware requirements such as RTK-GNSS. This offers a novel way for low ground coverage crops such as onion or asparagus to  be re-identified to provide potential for improved supply chain assurance.  

## Demonstration

https://user-images.githubusercontent.com/44243266/171829202-f1e23f67-8ac4-48d1-96fa-6f770f302868.mp4

## Installation
This installation guide is a quick start to get you onto the right path to build you own smart contracts. This will take you through each of the steps required to replicate the vision localisation pipeline. Web3 libraries and several depencies will be required as well as supporting tool chains. These should be widely avaiable for your chosen operating system. 

### 1. Install Node.js
To install Node.js, visit [nodejs.org](https://nodejs.org/en/) and follow the instructions for your operating system.

### 2. Install Truffle and Gananche
After you have installed Nodejs, type the following command into your terminal:

```
npm install truffle -g
```

Check that you have correctly installed it by reveiwing the version:

```
truffle version
```

You should hopefully see something simular to the below in your terminal:

```
Truffle v5.5.17 (core: 5.5.17)
Ganache v^7.1.0
Solidity - 0.8.14 (solc-js)
Node v16.15.1
Web3.js v1.5.3
```

Truffle comes with a client version of Ganache but get the GUI you should install from the [trufflesuite.com/ganache/](https://trufflesuite.com/ganache/) website. Then follow the instructions for your own operating system. 

### 3. Start your own project

To start your own project, change directory into a project folder (create a new empty folder on your desktop if you have not got one). The open a terminal in that folder and type:

```
Truffle init
```
This will create a new project whihc will will now have 3 x new folders and a js config file. These will be called, 'contracts', 'migrations', 'test' and 'truffle-config.js'. 

The contracts folder will contain the contracts, the migrations folder will contain the deployment files. The tests is a place write to test the logic of the contracts before they go into production.

Before we start the next step is tho amend the truffle-config.js file. Here, we need to uncomment the part of the configuration file (truffle-config.js) where we define the network to be used. Make sure that the below line (around line 45) is uncommented:

```
host: "127.0.0.1", // Localhost (default: none)
```

### 4. Compile our smart contract

This is the excting bit! The best place to begin is by cloing this repo and taking the files provided as the project you created in step 3 (assuming it was on a folder on your desktop) will require several of the files in this repo. 

You can do this by either the GitHub desktop tool or by installing Git on your system and typing:

```
git clone https://github.com/garry-clawson/Towards-Blockchain-Enabled-Infield-Localisation.git
```

You will then have all the files needed when copying and pasting across into your project folder. 

First, take the ```ImageStore.sol``` and place into your ```contracts``` folder. 

Second, take the ```2_deploy_contract.js``` and paste place into your ```migrations``` folder. The '2' at the start of the file name indicates that this is the 2nd file to be compiled (this is how Truffle knows the ordering of compilation). 

The ```ImageStore.sol``` file is a Solidity program (Solidity is one programming language you can use to develop smart contracts on the Ethereum blockchain), and has three simple functions: ```addItem()```, ```getListItem()``` and ```getListSize```. 

* ```addItem()``` appends a string to a list that was created at the very top of the contract. This is used to keep on adding new images (in Base64 format) to the contract. 

* ```getListItem()``` returns the CID string of an indexed element in the List data structure. The CID is a the retunred value we get when we have uploaded our image to the [Interplantery File System (IPFS)](https://ipfs.io). This is our decentrilised storage that we call on to host our data. 

* ```getListSize``` returns the size of the List. This is used for various items but mainly so we can quickly select the last item in the list for our proof of concept. 

To compile the project type the following in your terminal:

```
truffle compile
```

If it has comiled successfully you should have somethign like the below in your terminal:

```
Compiling your contracts...
===========================
> Compiling ./contracts/ImageStore.sol
> Compiling ./contracts/Migrations.sol
> Artifacts written to /Users/garryclawson/Desktop/Project/build/contracts
> Compiled successfully using:
   - solc: 0.5.16+commit.9c3226ce.Emscripten.clang
```

If you do have any tourble there is plenty of support on the web. An item that may cause an isue is stating the defauilt compiler. To remove this issue, comment out line 87 in the ```truffle-config.js``` file so that the default compiler for truffle was being used. 

Now that you have compiled your project you will see one new folder ```build/contracts``` that contains two new files ```ImageStore.json``` and ``` Migrations.json```. 

These are the contract artifacts, which hold all the necessary information for deploying and interacting with the contracts.

### 5. Deploy the contract to Ganache

Ganache is a locally hosted blockchain used for development of smart contracts as well as other testing requirements. Here we are safe to deploy and try out all of our contarct requirements safe in the knowledge that we will not be spending any 'actual' funds. Ganache also allows us to connect our projects so that we can see what is happening under the hood in the smart contract, as well as estomate the Gas costs required for ecah stage of deployment and interaction with the smart contract (i.e. writing to it to append the list). 

To deploy the contract to Ganache, type the following:

```
truffle migrate
```
If everything to plan, we should see that in Ganache that the contract has been sent to the blockchain and current blockheight has incremented. To see the actual ocntract state you will need to add a workspace to the Ganache GUI. The 'Contracts' tab on the GUI will take you through how to do this (2 very simple steps that takes less than 10 seconds). 

The contrcat has now been deployed and is ready for us to use as we wish. The next steps will be interacting with the contract by adding an image Base64 string, but first, we need to get our images and complete a sample alignment (using OpenCV), which acts as a key part of the localisation pipeline. 

### 6. Interacting with the smart contract

The smart contract can be interacted with via the terminal using Truffle commands, however we want to interct with the contract in a more automated way. This allows us to build brauder pipelines and extend the project. To intercat with smart contracts we will use ```web3``` tooling, specifically ```web3.py``` To install tyep the following into your terminal:

```
pip install web3
```

Note: You will need to have ```pip``` installed to use pip. For more information about web3 go to [web3.readthedocs](https://web3py.readthedocs.io/en/stable/quickstart.html). 

Now that web3 is installed. We can copy the ```ImageCall.py``` file and paste it into your main project folder. This program asks for you smart contract address (this can be found on the 'Contrctas' tab next to the ImageStore contract and will add a hard coded value ```QmWmXVKwg3PypTWNt9GSWvZHftDTEbJSyBkXH4rGaUFnh9``` to the list within the smart contract. This is a content identified (CID) and is individual to the image uploaded to IPFS. The act of appending this value to the blockchain is effectivily notorising it. This

To run ```ImageCall.py``` open a terminal and chnage directoy to the project folder and type:

```
python ImageCall.py
```

You will then be asked to enter you Ethereum ImageStore contract address. Once entered you should get something simular to the below:

```
Enter your Etheruem ImageStore contract address: 0xA40e776DDAB373960dA5F6FC170743A9DAe51204
List size:  2
List Item:  QmWmXVKwg3PypTWNt9GSWvZHftDTEbJSyBkXH4rGaUFnh9
tx_hash: 0x2540e565039b051d5f43ea0cc57cf30ece2d327dab746caf66fb514ef5494a70
```

We can see form the above that there are 2 items in the list (the list starts at 1 and not 0), and the last list item is ```qmWmXV...``` and it has an asscoiated transaction hash of ```0x2540e...```. This last value is the associated trasanction in the blockchain and can be seen when inspecting transactions on the Ganacahe GUI. 

If there is an error, it is most likely due to the contract having an empty list and the ListSize() function returning an exception. To avoid this run the ImageStore.py program once with lines 39-41 commented out (so it won't call the listsize function). Once run, you can then uncomment back and re-run. Remember, this is just a proof of concept, there are a billion ways to improve this! 

### Aligning an image

The image allignment process was inspired by the pyimagesearch [tutorial](https://pyimagesearch.com/2020/08/31/image-alignment-and-registration-with-opencv/) for document image alignment and registration. The concept of aligning infield ground stones and using the same type of registration is compelling as low cost method to localise using only a vision system. 





## Citation

If you use this project for research, please cite [the paper](https://mycittaion):

```
@inproceedings{clawson2022towards,
      title={Towards Blockchain Enabled Infield Localisation}, 
      author={Garry Clawson and Charles Fox},
      month={July},
      year={2022},
      booktitle={TBD}
}
```

## Acknowledgements

The following medium posts [[1]](https://medium.com/coinmonks/creating-and-deploying-smart-contracts-using-truffle-and-ganache-ffe927fa70ae), [[2]](https://medium.com/thecryptoelement/developing-a-todo-list-dapp-in-ethereum-e4daf8a9ea5c), [[3]](https://medium.com/swlh/develop-test-and-deploy-your-first-ethereum-smart-contract-with-truffle-14e8956d69fc) and documents [[4]](https://trufflesuite.com/docs/truffle/quickstart/) were extremely useful when writing up this overview. 

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

Second, take the ```2_deploy_contract.js``` and paste place into your ```migrations``` folder.



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


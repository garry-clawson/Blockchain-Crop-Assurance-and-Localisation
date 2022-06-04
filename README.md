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

Truffle comes with a client version of Ganache but get the GUI you should install from the [trufflesuite.com/ganache/] (https://trufflesuite.com/ganache/) website. Then follow the instructions for your own operating system. 

### Starting your own project





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


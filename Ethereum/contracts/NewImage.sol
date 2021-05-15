
pragma solidity ^0.6.2;

// contracts/NewImagesol

contract NewImage {
    
    //Gets the size of the list
    function getListSize() public view returns (uint256 size) {
        return list.length;
    }
}


// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract GasCompare {
    address public owner;
    
    constructor() {
        owner = msg.sender;
    }

    // Using modifier
    modifier onlyOwner() {
        require(msg.sender == owner, "Not owner!");
        _;
    }

    // Test function with modifier
    function testModifier() view external onlyOwner returns (uint256) {
        return 1;
    }

    // Test function with direct validation
    function testDirect() view external returns (uint256) {
        require(msg.sender == owner, "Not owner!");
        return 1;
    }
}
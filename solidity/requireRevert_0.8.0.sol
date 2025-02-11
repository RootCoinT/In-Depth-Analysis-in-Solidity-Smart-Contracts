// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract GasCompare {
    address public owner;
    
    constructor() {
        owner = msg.sender;
    }

    // Modifier using require
    modifier onlyRequire() {
        require(msg.sender == owner, "Not owner!");
        _;
    }

    // Modifier using assert
    modifier onlyAssert() {
        assert(msg.sender == owner);
        _;
    }
    
    // Modifier using revert
    modifier onlyRevert() {
        if (msg.sender != owner) {
            revert("Not owner!");
        }
        _;
    }

    // Test function for require (returns 1 on success)
    function testRequire() view external onlyRequire returns (uint256) {
        return 1;
    }

    // Test function for assert (returns 1 on success)
    function testAssert() view external onlyAssert returns (uint256) {
        return 1;
    }

    // Test function for revert (returns 1 on success)
    function testRevert() view external onlyRevert returns (uint256) {
        return 1;
    }
}
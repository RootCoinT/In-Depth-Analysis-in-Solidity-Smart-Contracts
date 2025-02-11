// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract ArithmeticCompare {
    using SafeMath for uint256;
    
    // SafeMath
    function testSafeMath(uint256 a, uint256 b) public pure returns (uint256) {
        return a.add(b);
    }
    
    // nature check(0.8.0+)
    function testNative(uint256 a, uint256 b) public pure returns (uint256) {
        return a + b;
    }
    
    // unchecked
    function testUnchecked(uint256 a, uint256 b) public pure returns (uint256) {
        unchecked {
            return a + b;
        }
    }
}
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract TransferCompare {
    // 记录接收到的ETH
    event Received(address sender, uint amount);
    
    // 用于接收ETH
    receive() external payable {
        emit Received(msg.sender, msg.value);
    }
    
    // 使用transfer
    function testTransfer(address payable recipient) public payable {
        recipient.transfer(msg.value);
    }
    
    // 使用send
    function testSend(address payable recipient) public payable returns (bool) {
        bool success = recipient.send(msg.value);
        require(success, "Send failed");
        return success;
    }
    
    // 使用call
    function testCall(address payable recipient) public payable returns (bool) {
        (bool success,) = recipient.call{value: msg.value}("");
        require(success, "Call failed");
        return success;
    }
}
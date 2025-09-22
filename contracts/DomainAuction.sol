// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DomainAuction {
    string public domainName;
    address public owner;
    uint public highestBid;
    address public highestBidder;
    bool public ended;

    event NewBid(address bidder, uint amount);
    event AuctionEnded(address winner, uint amount);

    constructor(string memory _domainName) {
        domainName = _domainName;
        owner = msg.sender;
    }

    function bid() external payable {
        require(!ended, "Auction ended");
        require(msg.value > highestBid, "Bid too low");
        if (highestBidder != address(0)) {
            payable(highestBidder).transfer(highestBid);
        }
        highestBid = msg.value;
        highestBidder = msg.sender;
        emit NewBid(msg.sender, msg.value);
    }

    function endAuction() external {
        require(msg.sender == owner, "Only owner can end auction");
        require(!ended, "Already ended");
        ended = true;
        payable(owner).transfer(highestBid);
        emit AuctionEnded(highestBidder, highestBid);
    }
}

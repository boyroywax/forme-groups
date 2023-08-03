# forme-groups

## What is this?
A Python library for creating and manipulating groups of decentralized assets, Id's, and VC's, and IPFS data.

## What is the Point?
* Zapier for Decentralized Assets
    * Build decentralized systems and applications
    * No need to write smart contracts
    * No need to learn Solidity

* Manage Decentralized Assets
    * Store data on the blockchain
    * Personal Blockchain

* Take Complete Control of your Web3 Data
    * Id's
    * VC's
    * Non-Fungible & Fungible Tokens
    * IPFS Data

* Decentralized Access Control
* No need to write smart contracts

## How does it work?
1. Create a Group
2. Add Members to the Group
3. Add Items to the Group
4. Anchor the Group to a Blockchain

## Functionality
1. Build using Decentralized Units.
2. Operate Across Multiple Blockchains
3. Create Groups of Id's, VC's, and IPFS Data
4. Anchor Groups to Blockchains
5. Manage Group Access and Permissions
6. Allow Group Members to Submit Items to the Group


## Example Use Casees

### Create a blog on the blockchain - proof of existence
* Publish a blog on the blockchain - proof of existence
* Become a merchant on the blockchain - proof of ownership
* Organize an event on the blockchain - proof of service
* Manage of group of members - proof of membership


## Universal Group Unit
A Universal Group Unit is a unit of data that can be used to create a group. A Universal Group Unit contains the following data:
1. Nonce
2. Ownership
3. Credentials
4. Data

### Nonce
A Nonce is a unique identifier for a group unit. Nonce is short for number used once. Generally, a Group Unit nonce will be in sequential order. However, a Group Unit nonce can be any string.

### Ownership
The Decentralized Id/s of the owner/s of the Group Unit.

### Credentials
Who has access to the Group Unit. Credentials are a list of Verified Credentials.

### Data
The data of the Group Unit. The data can be any type of data. The data can be a string, a list, a dictionary, or a file.


## Groups

### NonceChain
* A NonceChain is a list of Nonces.
* Can be any list of Nonces.
* A NonceChain can be a list of Nonces from different groups.
* Default Seperator - ```.```




### Group Hierarchy System Nonces
| Nonce | Description | Example |
| --- | --- | --- |
| 0 | Anchor |  Decentralized Asset ID |
| --- | --- | --- |
| 0.0 | Roles |  [Admin, Reader] |
| 0.1 | Posts |  [Post1, Post2] |
| --- | --- | --- |
| 0.1.0 | Comments |  [Comment1, Comment2] |


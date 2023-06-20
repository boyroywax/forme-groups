# forme-groups

## Groups for Web3

### Installation

```bash
git clone https://github.com/boyroywax/forme-groups.git
cd forme-groups
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 setup.py install
```

### CLI Usage

```bash
python3 groups --help
```

### Python Usage

```python
from groups import Groups
```

## Overview
> Manage groups of decentralized objects/assets

## Features
- [x] Create groups anchored on the blockchain to a digital asset
- [x] Verify the group on the blockchain
- [x] Add members to groups using Verified Credentials
- [x] Manage groups using Decentralized Identities
- [x] Add data schemas to groups to define the data structure of the group
- [x] Add data to groups using the data schemas
- [x] Verify the data on the blockchain
- [x] Public schemas allow for groups members to add data to the group (ratings, comments, etc.)

## Architecture
> The architecture of the project is based on the [DIDComm](
https://identity.foundation/didcomm-messaging/spec/#introduction) specification.

### IPv4 and IPv6
> IPv4 and IPv6 are used to identify the group on the blockchain.  The IPv4 and IPv6 addresses are used to create a decentralized identifier for the group.  Currently only IPv4 is supported with no bytesize limit nor maximum number of items in the dotted-decimal notation.

```text
# Example Group IPv4 Address
group://0.0.0.0.0
```

### Decentralized Identifiers & Identites
> Decentralized Identifiers are used to identify the group on the blockchain.  The decentralized identifiers are used to create a decentralized identifier for the group.  Currently only the `did:ipid` method is supported.
> Decentralized Identities are used to identify the owner of the group.  The decentralized identities are used to create a decentralized identity for the owner of the group.  Currently only the `did:ipid` method is supported.

```text
# Example Group Decentralized Identifier or Owner Decentralized Identity
did:ipid:Q
```

### Verified Credentials
> Verified Credentials are used to identify the members of the group.  The verified credentials are used to create a verified credential for the members of the group.  Currently only the `did:ipid` method is supported.

```text
# Example Group Member Verified Credential
did:ipid:Q
```

### IPFS
> IPFS is used to store the data of the group.  The IPFS hash is used to create a decentralized identifier for the data of the group.  Currently only the `ipfs` method is supported.

### 




## Classes
### Groups
> The Groups class is the main class of the project. It is used to create groups, add members to groups, add data schemas to groups, and add data to groups.

### Universal Object
> The Universal Object class is used to create a universal object. A universal object is an object that can be used in any group. It is used to create data schemas and data.

The Universal Object holds the following attributes:
- `nonce`: The nonce of the universal object
- `name`: The name of the universal object
- `description`: The description of the universal object
- `owner`: The owner of the universal object
- `credentials`: The credentials used to access the the universal object
- `data`: The data of the universal object, can include a schema

### Default Schema
>The default schema is used to create the data schema for the universal object. Data is made up of key value pairs stored in a Dictionary. 

The default schema is a dictionary with the following keys:
- `title`: [String] The title of the data schema.
- `entries`: [Dictionary] The entries of the data schema.

The default entries to describe a group with a schema are:
- `link`: [List] The link to the decentralized asset.
- `schema`: [Dictionary] The schema of the data.

### Nonce
> A nonce is used to organize items in a group. It is a unique identifier for each item in a group.  Nonces are strung together to create a chain of nonces. The chain of nonces is used to verify the group on the blockchain.

Example of a simple chain of string nonces:
```text
nonce1.nonce2
```
In the above example, `nonce1` is the parent nonce of `nonce2`.

### Nonce Types
> Nonce values can be input as a `str` or `int`. The default nonce type is `int`.

In additiion to the two input types, there are many more nonce types that can be used. The nonce types are:
- `int`: An integer
- `str`: A string
- `hexadecimal`: A string representing a hexadecimal value.  Starts with `0x`.
- `decimal`: A string representing a decimal value.  Starts with `0d`.
- `binary`: A string representing a binary value.  Starts with `0b`.
- `boolean`: A boolean value
- `float`: A float value
- `list`: A list of values in string format e.g. `'["value1", "value2", "value3"]'`
- `tuple`: A tuple of values in string format e.g. `'("value1", "value2", "value3")'`
- `dictionary`: A dictionary of values in string format e.g. `'{"key1": "value1", "key2": "value2", "key3": "value3"}'`
- `unknown`: A value of unknown type, rejected by the NonceType class

### Nonce Units
> The NonceUnit class is used to create a nonce unit. A nonce unit is a single nonce in a chain of nonces.

The NonceUnit class checks that the nonce is of a valid type.  It also checks that nonce_unit_value and nonce_unit_type match.

The default nonce unit type is `int`, with a default nonce unit value of `0`.

### Nonce Chain
> The Nonce class is used to create a nonce chain. A nonce chain is a chain of nonce units.

Nonce chains can hold multiple nonce units of varying types.  The Nonce class checks that the nonce units are valid and that the nonce units are in the correct order.

An active nonce unit is the last nonce unit in the chain.  The active nonce unit is used to create the next nonce unit in the chain.

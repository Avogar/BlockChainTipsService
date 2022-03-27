# BlockChainTipsService

## Overview

This is a Blockhain based tips service. It is based on smart contracts. It can be used via a Docker container.

### Features

- Adding organizations and employees to smart contract
- Generating QR-codes for customers to send their tips/reviews
- Sending tips to organizations or employees using QR-codes
- Reviewing organizations or an employees usins QR-codes
- Ability to get the list of all reviews for specific employee or organization

## Installation

The installation of our project is simple, because it uses docker container. Do the following steps:

```
git clone https://github.com/Avogar/BlockChainTipsService.git

cd BlockChainTipsService

sudo docker build . -t tips:latest

sudo docker run -it tips:latest
```

## Using service

Our app is an interactive python script that interacts with our smart contract by calling its functions with the required arguments. The app can be run in three modes, each with its own set of available actions:

### Customer mode
The following actions are available:
- Get the list of all organizations.
- Get the list of employees in the organization.
- Get the list of all reviews of one employee/organization.
- Send a review/tip to an employee/organization. The user will need a QR-code to do so.

### Organization mode
Every modification to your organization in the contract can be made only if it is made from the same address that created the organization. The following actions are available:
- Add your organization to the contract. The user will be able to enter the initial list of employees either interactively or via a json file.
- Remove your organization from the contract.
- Add/remove an employee from your organization.
- Generate your new organization QR-code for tips and/or reviews. Remember that you need a new one for each customer.

### Employee mode:
Here you can only generate your new personal QR-code.  Remember that you need a new one for each customer.

## Example run
Here is an example run where we leave a review for several employees:
```   
Select one number. Who are you?
1) Customer
2) Organization
3) Employee
0) Exit
3
 
Please enter your organization name: MacRonalds
Please enter your name: Alice
Select one number. What do you want to do?
1) Change my organization name
2) Change my name
3) Generate new QR-code
0) Exit
3
 
Enter desired filename for QR-code (leave empty for default):
 
Select one number. What do you want to do?
1) Change my organization name
2) Change my name
3) Generate new QR-code
0) Exit
0
 
 
Select one number. Who are you?
1) Customer
2) Organization
3) Employee
0) Exit
1
 
Select one number. What do you want to do?
1) Get the list of all organizations
2) Get the list of employees in organization
3) Get the list of organization reviews
4) Get the list of employee reviews
5) Send an organization review
6) Send an employee review
7) Send a tip to an organization
8) Send a tip to an employee
9) Change my address
10) Change my private key
0) Exit
2
 
Please enter organization name: MacRonalds
List of employees in the organization MacRonalds: ['Alice', 'Bob']
 
Select one number. What do you want to do?
1) Get the list of all organizations
2) Get the list of employees in organization
3) Get the list of organization reviews
4) Get the list of employee reviews
5) Send an organization review
6) Send an employee review
7) Send a tip to an organization
8) Send a tip to an employee
9) Change my address
10) Change my private key
0) Exit
8
 
Please enter path to QR code from employee (empty to exit): qr.png
Please enter the amount of tip: 0.0001
Please enter employee review: "Very nice girl! Hope to see her some more!"
Please enter your address: 0x8e7050b2E4269590298a1C81c21387C200Ea41ac
Please enter your private_key: ea308eca45ee084aae3ec38cf23ddfc3664fc6f0d133f2863f4e82148ae55b84
Transaction id:  0x2ca570f5e65ba10ecf788fe3a220184ea92dba1fcf8de5492e42c45248b6626c
 
Select one number. What do you want to do?
1) Get the list of all organizations
2) Get the list of employees in organization
3) Get the list of organization reviews
4) Get the list of employee reviews
5) Send an organization review
6) Send an employee review
7) Send a tip to an organization
8) Send a tip to an employee
9) Change my address
10) Change my private key
0) Exit
6
 
Please enter path to QR code from employee (empty to exit): eve.png
Please enter employee review: "Didn't like her. Please fire. 0/5"
Transaction id:  0x37e16ed57539f15d8918ba4ffecd298d6cfa8e159796539498c58ef193311152
```

**Ethereum - Full Node Setup**
====================================================


Introduction
------------

This tutorial is a step by step guide to setting up a Ethereum Node on the operating system of your choice(Windows or Linux). Once a full node is setup, you will have the ability to create/manage accounts, transfer Ethereum and mine Ethereum. This tutorial will leverage Geth, which is a command line interface used to run a full ethereum node, which was developed in Go.

Documentation
-------------
	Documentation at [https://ethereum.gitbooks.io/frontier-guide/content/](https://ethereum.gitbooks.io/frontier-guide/content/ "Frontier Guide")


Requirements
------------

	Windows or Linux environment with atleast 65 GB of storage available.

Installation
------------

	Windows - 
		Download executable - https://geth.ethereum.org/downloads/
		Run downloaded executable
		Open command prompt as administrator and browse to the installation path(cd C:\Program Files\Geth)
		Enter command geth to begin downloading the Ethereum Blockchain

	Linux -
		Clone repository - git clone https://github.com/ethereum/go-ethereum
		Install prereqs - sudo apt-get install -y build-essential libgmp3-dev golang
		Browse to clone path(cd go-ethereum)
		Make geth
		Run build/bin/geth to begin downloading the Ethereum Blockchain

Checking Connectivity
-------------
	
	To check that your node is currently connected to the network you first need to run geth Console to open the interactive console. Once the console is open, you can use the net module to explore the current connectivity status of your node. The two most common commands to use are net.listening and net.peerCount. The listening command returns true or false symbolizing if you are a listening node and the peerCount command will return the number of peers your node is currently connected to. For more detailed information about the peers you are connected to, the admin.peers() module will return detailed information such as names, IP Addresses, Ports used and support versions. 


Account Management
---------------
		


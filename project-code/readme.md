## Final Project
Blockchain API to demonstrate a distrubuted ledger system.
 
 ### Setup:
  
  - Step 1: Make requirements(only needed on first run thru)
  - Step 2: Open a console and run Make run-node1
      - Console should output the following message:
        * Running on http://0.0.0.0:9999/ (Press CTRL+C to quit)
  - Step 2a:Open a second conole and run Make run-node2
      - Console should output the following message:
        * Running on http://0.0.0.0:8888/ (Press CTRL+C to quit)
      
  - Step 4: Make test
    - Console should output test script


 ### CURL Examples:
  - register
    *	curl -H "Content-Type: application/json"  \
		-X POST \
		-d '{"nodes": ["http://127.0.0.1:8888"]}' \
		http\://localhost\:9999/register

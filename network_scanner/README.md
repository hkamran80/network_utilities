# Network Scanner
* Platform: macOS
* Language: Python 3, JSON
* Time to run: 8m 30s

# Files
* `known.json`: Known MAC addresses
  * Format: `"mac_address": "device_name"`
* `macs.json`: MAC vendors (not a complete list)
  * Format: `"mac_address (first 6 chars)": "vendor"`
* `networks.json`: Known networks
  * Format: `"mac_address_of_gateway": "network_name"`
* `netscan.py`: Network scanning program
  * Usage: `python3 netscan.py`
  * Dependencies: None

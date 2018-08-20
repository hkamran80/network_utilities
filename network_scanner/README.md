# Network Scanner
* [Changelog](https://github.com/hkamran80/network_utilities/wiki/Network-Scanner:-Changelog)
* Version: 1.1
* Platforms tested: macOS
* Language(s): Python 3, JSON
* Time to run: ~8 minutes

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

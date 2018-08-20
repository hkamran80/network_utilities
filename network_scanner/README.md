# Network Scanner
* [Changelog](https://github.com/hkamran80/network_utilities/wiki/Network-Scanner:-Changelog)
* Version: ![1.1](https://badgen.net/badge/version/1.1/blue)
* Platforms tested: ![macOS](https://badgen.net/badge/platform/macOS/green)
* Language(s): ![python3](https://badgen.net/badge/language/python3/green) ![JSON](https://badgen.net/badge/language/json/green)
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

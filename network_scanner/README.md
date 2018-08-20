# Network Scanner
* [Changelog](https://github.com/hkamran80/network_utilities/wiki/Network-Scanner:-Changelog)
* Version: [![1.1](https://badgen.net/badge/version/1.1/blue)](https://github.com/hkamran80/network_utilities/blob/master/network_scanner/netscan.py)
* Platforms tested: [![macOS](https://badgen.net/badge/platform/macOS/green)](https://github.com/hkamran80/network_utilities/blob/master/network_scanner/netscan.py)
* Language(s): [![python3](https://badgen.net/badge/language/python3/green) ![JSON](https://badgen.net/badge/language/json/green)](https://github.com/hkamran80/network_utilities/blob/master/network_scanner/netscan.py)
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

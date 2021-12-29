#!/usr/bin/env python

import subprocess
import optparse
import re


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_options():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface",
                      help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error(
            "[-] No interface was provided, use --help for more info.")
    if not options.new_mac:
        parser.error(
            "[-] No mac address was provided, use --help for more info.")
    return options


def get_current_mac(interface):
    # 1. Execute and read ifconfig
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    ifconfig_result_string = ifconfig_result.decode("utf-8")

    # 2. Read the MAC Address from output.
    mac_address_search_result = re.search(
        r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result_string)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC Address.")


options = get_options()
mac_before_update = get_current_mac(options.interface)
print("Current MAC = " + str(mac_before_update))

change_mac(options.interface, options.new_mac)

mac_after_update = get_current_mac(options.interface)

if mac_after_update == options.new_mac:
    print("[+] MAC address was successfully changed to " + mac_after_update)
else:
    print("[-] MAC address did not get changed.")
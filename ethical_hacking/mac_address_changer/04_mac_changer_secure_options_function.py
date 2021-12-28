#!/usr/bin/env python

import subprocess
import optparse

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    subprocess.call(["ifconfig", interface])

def get_options():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface",
                    help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error("[-] No interface was provided, use --help for more info.")
    if not options.new_mac:
        parser.error("[-] No mac address was provided, use --help for more info.")
    return options

options = get_options()
change_mac(options.interface, options.new_mac)
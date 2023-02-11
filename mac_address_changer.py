#!/usr/bin/env python

import subprocess
import argparse
import re


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Interface whose MAC address to be changed")
    parser.add_argument("-m", "--mac", dest="new_mac", help="New MAC address")
    args = parser.parse_args()
    if not args.interface:
        parser.error("[-] Please specify an interface. Use --help for more info.")
    elif not args.new_mac:
        parser.error("[-] Please specify a new MAC address. Use --help for more info.")
    return args


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.run(["ifconfig", interface, "up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_search_result:
        return mac_search_result.group(0)
    else:
        print("[-] Could not read MAC address.")


options = get_arguments()

current_mac = get_current_mac(options.interface)
print("Current MAC address = " + str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address was successfully changed to " + current_mac)
else:
    print("[-] MAC address was not changed.")


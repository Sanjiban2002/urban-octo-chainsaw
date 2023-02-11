#!/usr/bin/env python

import scapy.all as scapy
import argparse


def get_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--range", dest="range", help="Target IP range")
    arg = parser.parse_args()
    if not arg.range:
        parser.error("[-] Please specify an IP range. Use --help for more info.")
    return arg


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list


def print_result(result_list):
    print("IP\t\t\tMAC Address\n-----------------------------------------")
    for client in result_list:
        print(client["ip"] + "\t\t" + client["mac"])


option = get_argument()

scan_result = scan(option.range)

print_result(scan_result)


import subprocess
import optparse
import re


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest='interface', help='Interface to change MAC address of.')
    parser.add_option('-m', '--mac', dest='new_mac', help='New MAC address.')
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error('[-] Please specify an interface, use --help for more info.')
    elif not options.new_mac:
        parser.error('[-] Please specify an interface, use --help for more info.')
    return options


def change_mac(interface, new_mac):
    print(f'[+] Changing MAC address for {interface} to {new_mac}')
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.call(['ifconfig', interface, 'up'])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(['ifconfig', interface])
    print(ifconfig_result)
    print(type(ifconfig_result))
    mac_regex = re.compile(r"([0-9a-f][0-9a-f]:){5}[0-9a-f][0-9a-f]")
    mac_regex = re.compile(r"\w:\w:\w:\w:\w:\w:\w:\w:\w:\w:\w:\w:")
    print(mac_regex)
    mac_address_search_result = re.search(mac_regex, ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print('[-] Could not read MAC address')
    # print(mac_address_search_result.group(0))


options = get_arguments()
current_mac = get_current_mac(options.interface)
print(current_mac)
# change_mac(options.interface, options.new_mac)

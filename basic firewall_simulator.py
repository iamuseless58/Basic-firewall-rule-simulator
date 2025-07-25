# firewall_simulator.py

firewall_rules = []

def add_rule(ip, protocol, port, action):
    rule = {'ip': ip, 'protocol': protocol.upper(), 'port': int(port), 'action': action.upper()}
    firewall_rules.append(rule)

def check_packet(ip, protocol, port):
    for rule in firewall_rules:
        if rule['ip'] == ip and rule['protocol'] == protocol.upper() and rule['port'] == int(port):
            return rule['action']
    return "ALLOW (Default Policy)"

def show_rules():
    print("\n--- Firewall Rules ---")
    for i, rule in enumerate(firewall_rules):
        print(f"{i+1}. {rule['action']} {rule['ip']} {rule['protocol']} {rule['port']}")
    print("----------------------\n")

def main():
    while True:
        print("Firewall Rule Simulator")
        print("1. Add Rule")
        print("2. Check Packet")
        print("3. Show Rules")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            ip = input("Enter IP address: ")
            protocol = input("Enter Protocol (TCP/UDP): ")
            port = input("Enter Port: ")
            action = input("Enter Action (ALLOW/DENY): ")
            add_rule(ip, protocol, port, action)

        elif choice == '2':
            ip = input("Enter packet IP: ")
            protocol = input("Enter packet Protocol (TCP/UDP): ")
            port = input("Enter packet Port: ")
            result = check_packet(ip, protocol, port)
            print(f"\n🔥 Result: Packet is {result}\n")

        elif choice == '3':
            show_rules()

        elif choice == '4':
            print("Exiting Firewall Simulator.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()

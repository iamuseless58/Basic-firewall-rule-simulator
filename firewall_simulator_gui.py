import json
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

firewall_rules = []
RULES_FILE = "firewall_rules.json"

def add_rule(ip, protocol, port, action):
    rule = {'ip': ip, 'protocol': protocol.upper(), 'port': int(port), 'action': action.upper()}
    firewall_rules.append(rule)

def check_packet(ip, protocol, port):
    for rule in firewall_rules:
        if rule['ip'] == ip and rule['protocol'] == protocol.upper() and rule['port'] == int(port):
            return rule['action']
    return "ALLOW (Default Policy)"

def save_rules():
    with open(RULES_FILE, 'w') as f:
        json.dump(firewall_rules, f)

def load_rules():
    global firewall_rules
    try:
        with open(RULES_FILE, 'r') as f:
            firewall_rules = json.load(f)
    except FileNotFoundError:
        firewall_rules = []

def update_rule_list():
    rule_listbox.delete(*rule_listbox.get_children())
    for i, rule in enumerate(firewall_rules):
        rule_listbox.insert('', 'end', values=(i+1, rule['ip'], rule['protocol'], rule['port'], rule['action']))

def gui_add_rule():
    ip = ip_entry.get()
    protocol = protocol_var.get()
    port = port_entry.get()
    action = action_var.get()
    if ip and protocol and port and action:
        add_rule(ip, protocol, port, action)
        update_rule_list()
        save_rules()

def gui_check_packet():
    ip = packet_ip_entry.get()
    protocol = packet_protocol_var.get()
    port = packet_port_entry.get()
    if ip and protocol and port:
        result = check_packet(ip, protocol, port)
        messagebox.showinfo("Packet Result", f"Packet is {result}")

root = tk.Tk()
root.title("Firewall Rule Simulator")

entry_frame = tk.LabelFrame(root, text="Add Firewall Rule")
entry_frame.pack(padx=10, pady=10, fill="x")

tk.Label(entry_frame, text="IP:").grid(row=0, column=0)
ip_entry = tk.Entry(entry_frame)
ip_entry.grid(row=0, column=1)

tk.Label(entry_frame, text="Protocol:").grid(row=0, column=2)
protocol_var = tk.StringVar(value="TCP")
protocol_menu = ttk.Combobox(entry_frame, textvariable=protocol_var, values=["TCP", "UDP"], width=5)
protocol_menu.grid(row=0, column=3)

tk.Label(entry_frame, text="Port:").grid(row=0, column=4)
port_entry = tk.Entry(entry_frame, width=5)
port_entry.grid(row=0, column=5)

tk.Label(entry_frame, text="Action:").grid(row=0, column=6)
action_var = tk.StringVar(value="ALLOW")
action_menu = ttk.Combobox(entry_frame, textvariable=action_var, values=["ALLOW", "DENY"], width=7)
action_menu.grid(row=0, column=7)

add_button = tk.Button(entry_frame, text="Add Rule", command=gui_add_rule)
add_button.grid(row=0, column=8, padx=5)

rule_frame = tk.LabelFrame(root, text="Firewall Rules")
rule_frame.pack(padx=10, pady=5, fill="both", expand=True)

cols = ("#", "IP", "Protocol", "Port", "Action")
rule_listbox = ttk.Treeview(rule_frame, columns=cols, show="headings")
for col in cols:
    rule_listbox.heading(col, text=col)
    rule_listbox.column(col, anchor="center")
rule_listbox.pack(fill="both", expand=True)

packet_frame = tk.LabelFrame(root, text="Check Packet")
packet_frame.pack(padx=10, pady=10, fill="x")

tk.Label(packet_frame, text="IP:").grid(row=0, column=0)
packet_ip_entry = tk.Entry(packet_frame)
packet_ip_entry.grid(row=0, column=1)

tk.Label(packet_frame, text="Protocol:").grid(row=0, column=2)
packet_protocol_var = tk.StringVar(value="TCP")
packet_protocol_menu = ttk.Combobox(packet_frame, textvariable=packet_protocol_var, values=["TCP", "UDP"], width=5)
packet_protocol_menu.grid(row=0, column=3)

tk.Label(packet_frame, text="Port:").grid(row=0, column=4)
packet_port_entry = tk.Entry(packet_frame, width=5)
packet_port_entry.grid(row=0, column=5)

check_button = tk.Button(packet_frame, text="Check Packet", command=gui_check_packet)
check_button.grid(row=0, column=6, padx=5)

load_rules()
update_rule_list()
root.mainloop()

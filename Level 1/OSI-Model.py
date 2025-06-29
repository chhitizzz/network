# OSI Layer Explorer - CLI Version

osi_layers = [
    {
        'layer': 'Layer 7 - Application',
        'description': 'The layer users interact with. Examples: HTTP, FTP, DNS, POP3',
        'protocols': ['HTTP', 'HTTPS', 'FTP', 'DNS', 'POP3']
    },
    {
        'layer': 'Layer 6 - Presentation',
        'description': 'Formats data for the application layer. Handles encryption/decryption (e.g. SSL/TLS)',
        'protocols': ['SSL', 'TLS']
    },
    {
        'layer': 'Layer 5 - Session',
        'description': 'Manages sessions between applications. Starts, stops, restarts sessions.',
        'protocols': ['NetBIOS', 'PPTP']
    },
    {
        'layer': 'Layer 4 - Transport',
        'description': 'Ensures complete data transfer with TCP/UDP. Adds port information.',
        'protocols': ['TCP', 'UDP']
    },
    {
        'layer': 'Layer 3 - Network',
        'description': 'Routes packets via IP. Manages logical addressing and path selection.',
        'protocols': ['IP', 'ICMP']
    },
    {
        'layer': 'Layer 2 - Data Link',
        'description': 'Frames data for physical transfer. Uses MAC addresses for node-to-node communication.',
        'protocols': ['Ethernet', 'PPP']
    },
    {
        'layer': 'Layer 1 - Physical',
        'description': 'Transmits raw bit stream over physical medium. Includes cables, signals, voltages.',
        'protocols': ['DSL', 'USB']
    }
]

def display_menu():
    print("OSI Model Explorer")
    print("-------------------")
    for i, layer in enumerate(osi_layers):
        print(f"{i + 1}. {layer['layer']}")
    print('0. Exit')

def display_layer_details(choice):
    layer = osi_layers[choice - 1]
    print(f"\n{layer['layer']}")
    print(f"Description: {layer['description']}")
    print(f"Example Protocols: {', '. join(layer['protocols'])}")

def simulate_packet_flow():
    print("\nSimulating Packet Flow Through OSI Layers")
    print("--------------------------------------------")
    for layer in reversed (osi_layers):
        print(f"Encapsulating at {layer['layer']}")
    print("\nNow sending packet...")
    for layer in osi_layers:
        print(f"Decapsulating at {layer['layer']}")

def main():
    while True:
        display_menu()
        try:
            choice = int(input("Select a layer to explore (or 0 to simulate/exit): "))
            if choice == 0:
                simulate_packet_flow()
                break
            elif 1 <= choice <= len(osi_layers):
                display_layer_details(choice)
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid input. Enter a number.")

if __name__ == "__main__":
    main()
import argparse
import ipaddress
import socket

def get_ip_address():
    """Get the container's IP address."""
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except Exception as e:
        return f"Error fetching IP: {str(e)}"

def check_collision(ip_file_path):
    """Check for overlapping IP ranges."""
    try:
        with open(ip_file_path, "r") as file:
            ip_ranges = [line.strip() for line in file.readlines() if line.strip()]

        networks = [ipaddress.ip_network(ip, strict=False) for ip in ip_ranges]
        collisions = set()

        for i, net1 in enumerate(networks):
            for net2 in networks[i+1:]:
                if net1.overlaps(net2):
                    collisions.add(str(net1))
                    collisions.add(str(net2))

        if collisions:
            print("Colliding IP Ranges:")
            for net in sorted(collisions):
                print(net)
        else:
            print("No collisions detected.")
    except Exception as e:
        print(f"Error checking collisions: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Simple IP Tool")
    parser.add_argument("--check-collision", type=str, dest="ip_file_path", help="Path to file containing IP networks")
    args = parser.parse_args()

    if args.ip_file_path:
        check_collision(args.ip_file_path)
    else:
        print("Container IP Address:", get_ip_address())

if __name__ == "__main__":
    main()
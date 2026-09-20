"""Validate four decimal IPv4 octets with a simple parsing exercise."""


def is_valid_ipv4_address(ip_address):
    """Accept ASCII octets 0-255; leading zeroes are allowed in this exercise."""
    if not isinstance(ip_address, str):
        return False
    parts = ip_address.split(".")
    if len(parts) != 4:
        return False
    return all(
        1 <= len(part) <= 3 and part.isascii() and part.isdigit()
        and 0 <= int(part) <= 255
        for part in parts
    )


if __name__ == "__main__":
    for address in ("192.168.0.1", "256.100.50.0", "192.168.0.01"):
        print(f"{address}: {is_valid_ipv4_address(address)}")

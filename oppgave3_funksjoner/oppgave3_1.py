"""
Oppgave 3.1
Lag en funksjon som tar inn en streng og sjekker om det er en gyldig IPv4-adresse.
En gyldig IPv4-adresse har fire deler atskilt med punktum (.), der hver del er et heltall mellom 0 og 255.
Funksjonen skal returnere True hvis det er en gyldig adresse, og False ellers.

Eksempel:
Input: "192.168.0.1" → Output: True
Input: "256.100.50.0" → Output: False
"""


def is_valid_ipv4_address(ip_address):
    parts = ip_address.split('.')

    if len(parts) != 4:
        return False

    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False

    return True


# Test tilfeller
print(is_valid_ipv4_address("192.168.0.1"))  # Output: True
print(is_valid_ipv4_address("256.100.50.0"))  # Output: False
print(is_valid_ipv4_address("192.168.0"))  # Output: False
print(is_valid_ipv4_address("192.168.0.1.1"))  # Output: False
print(is_valid_ipv4_address("192.168.0.-1"))  # Output: False
print(is_valid_ipv4_address("192.168.0.01"))  # Output: True

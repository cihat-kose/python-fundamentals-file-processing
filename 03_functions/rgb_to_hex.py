"""Convert integer RGB components to an uppercase hexadecimal color."""


def rgb_to_hex(red, green, blue):
    """Return #RRGGBB; reject non-integers and components outside 0-255."""
    for name, value in (("red", red), ("green", green), ("blue", blue)):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if not 0 <= value <= 255:
            raise ValueError(f"{name} must be between 0 and 255")
    return f"#{red:02X}{green:02X}{blue:02X}"


if __name__ == "__main__":
    print(rgb_to_hex(205, 92, 92))
    print(rgb_to_hex(0, 0, 0))
    print(rgb_to_hex(255, 255, 255))

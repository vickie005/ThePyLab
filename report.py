def create_report(spacecraft):
    return f"""
    ============= REPORT ============

    Name: {spacecraft.get('name', 'Unknown')}
    Distance: {spacecraft.get("distance", "Unknown")}AU

    ==================================
    """

def main():
    spacecraft = {"name": "Vic Webb Space Telescope"}
    print(create_report(spacecraft))

if __name__ == "__main__":
    main()
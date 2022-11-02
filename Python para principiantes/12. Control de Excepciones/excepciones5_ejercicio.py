loaded_config = """# Rocket Ship Configuration File!
fuel_tanks=4
oxygen_tanks=3
initial_propulsion_level=84
$ End of file"""

# Enter code below
parsed_config = {}
for line in loaded_config.split('\n'):
    try:
        key, value = line.split('=')
    except ValueError:
        print(f'Unable to parse {line}')

print(parsed_config)
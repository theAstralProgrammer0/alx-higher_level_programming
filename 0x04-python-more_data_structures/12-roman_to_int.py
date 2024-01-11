#!/usr/bin/python3
def roman_to_int(rom_string):
    rom_dict = {
            '4': {
                'VIII': 8,
                'LXXX': 80,
                'DCCC': 800
                },
            '3': {
                'III': 3,
                'VII': 7,
                'XXX': 30,
                'LXX': 70,
                'CCC': 300,
                'DCC': 700,
                'MMM': 3000
                },
            '2': {
                'II': 2,
                'IV': 4,
                'VI': 6,
                'IX': 9,
                'XX': 20,
                'XL': 40,
                'LX': 60,
                'XC': 90,
                'CC': 200,
                'CD': 400,
                'DC': 600,
                'CM': 900,
                'MM': 2000
                },
            '1': {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
                }
            }
    val_list = []
    iter_list = []

    while rom_string:
        match_found = False

        for digit, sub_dict in sorted(rom_dict.items(),
                                      key=lambda x: int(x[0]), reverse=True):
            for key, value in sub_dict.items():
                if rom_string.startswith(key):
                    val_list.append(value)
                    rom_string = rom_string[len(key):]
                    match_found = True
                    break

            if match_found:
                break

        if not match_found:
            iter_list.append(rom_string[-1])
            rom_string = rom_string[:-1]

    return sum(val_list)

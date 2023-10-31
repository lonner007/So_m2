import sys
import random

def trim(s):
    inicio = s.find_first_not_of(" \t\n\r")
    fim = s.find_last_not_of(" \t\n\r")

    if inicio is None:
        return ""

    return s[inicio:fim+1]

def gets_physical_page_number_from_table(virtual_page_number, file_name):
    line_number_to_access = virtual_page_number
    current_row_number = 1

    with open(file_name, 'r') as input_file:
        for line in input_file:
            current_row_number += 1
            if current_row_number > line_number_to_access:
                return line.strip()

    return "error"

def gets_value_from_memory(physical_page_number, page_offset):
    line_number_to_access = physical_page_number + page_offset
    current_row_number = 1

    with open("data_memory.txt", 'r') as input_file:
        for line in input_file:
            current_row_number += 1
            if current_row_number > line_number_to_access:
                return line.strip()

    return "error"

def creates_virtual_page_number(bits_quantity):
    if bits_quantity == 32:
        numero_aleatorio = random.randint(1, 1000)
    else:
        numero_aleatorio = random.randint(1, 1000000)

    return numero_aleatorio

def main(argv):
    input_by_user = ""
    file_name = ""
    physical_page_number = ""
    bits_quantity = 32
    page_offset = 256
    virtual_page_number = 0

    if len(argv) == 2:
        if trim(argv[1]) in ["addresses_16b.txt", "addresses_32b.txt"]:
            file_name = argv[1]
            if file_name == "addresses_16b.txt":
                bits_quantity = 16
                virtual_page_number = creates_virtual_page_number(bits_quantity)
            else:
                bits_quantity = 32
                virtual_page_number = creates_virtual_page_number(bits_quantity)

            physical_page_number = gets_physical_page_number_from_table(virtual_page_number, file_name)
            print("\nVirtual address:", virtual_page_number)
            print("Page number:", gets_physical_page_number_from_table(virtual_page_number, file_name))
            print("Page offset:", page_offset)
            print("Value read:", gets_value_from_memory(int(physical_page_number), page_offset))
            return

        input_by_user = argv[1]

        try:
            number = int(input_by_user)
        except ValueError:
            print("Value is not a number!")
            return

        virtual_page_number = int(input_by_user)
        file_name = "addresses_" + str(bits_quantity) + "b.txt"

        if 0 < virtual_page_number < 1001:
            physical_page_number = gets_physical_page_number_from_table(virtual_page_number, file_name)
            print("\nVirtual address:", virtual_page_number)
            print("Page number:", physical_page_number)
            print("Page offset:", page_offset)
            print("Read value:", gets_value_from_memory(int(physical_page_number), page_offset))
            return
        else:
            print("Virtual address does not exist!")
            return

    if len(argv) == 1:
        virtual_page_number = creates_virtual_page_number(bits_quantity)
        file_name = "addresses_" + str(bits_quantity) + "b.txt"
        physical_page_number = gets_physical_page_number_from_table(virtual_page_number, file_name)
        print("\nVirtual address:", virtual_page_number)
        print("Page number:", physical_page_number)
        print("Page offset:", page_offset)
        print("Read value:", gets_value_from_memory(int(physical_page_number), page_offset))
        return

    print("Comando inexistente/inválido!")

if __name__ == "__main__":
    main(sys.argv)

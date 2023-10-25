katz_deli = []


def line(deli_line):
    line_message = "The line is currently: "
    for i, name in enumerate(deli_line, 1):
        name_in_line = f"{i}. {name}"
        line_message = line_message + name_in_line
        if i < len(deli_line):
            line_message += " "
    if len(deli_line) == 0:
        print("The line is currently empty.")
        return
    print(line_message)

def take_a_number(deli_line, name):
    deli_line.append(name)
    name_index = deli_line.index(name)
    num_in_line = name_index + 1
    print(f"Welcome, {name}. You are number {num_in_line} in line.")

def now_serving(deli_line):
    if len(deli_line) == 0:
        print("There is nobody waiting to be served!")
    else:
        first_in_line = deli_line[0]
        deli_line.remove(first_in_line)
        print(f"Currently serving {first_in_line}.")

# line(["Peyton", "Kassidy", "Angelus"])
OTHER_DELI = ["Logan", "Avi", "Spencer"]
test_line = ["Peyton", "Kassidy", "Angelus"]
take_a_number(test_line, "James")
now_serving(OTHER_DELI)
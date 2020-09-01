
members = list()

with open("input.txt", "r") as input_data:
    for number_line, line in enumerate(input_data):
        if number_line != 0:
            member = tuple(int(el) for el in line.split())
            members.append(member)


def extract_member_info(member_tuple: tuple):
    """extract tuple in two elements"""
    return member_tuple[0], member_tuple[1]


def change_neighboring_elements(array: list, index: int):
    """changing neighboring elements in list"""
    array[index + 1], array[index] = array[index], array[index + 1]
    return array, True


need_to_change = True

while need_to_change:

    need_to_change = False

    for member_number, member in enumerate(members):

        if member_number != len(members) - 1:

            current_member_id, current_member_rank = extract_member_info(member)
            next_member_id, next_member_rank = extract_member_info(members[member_number + 1])

            if current_member_rank < next_member_rank:

                members, need_to_change = change_neighboring_elements(members, member_number)

            elif current_member_rank == next_member_rank and current_member_id > next_member_id:

                members, need_to_change = change_neighboring_elements(members, member_number)

for member in members:

    print(member[0], member[1])

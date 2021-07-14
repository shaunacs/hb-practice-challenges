passwords_file = open('passwords.txt')
passwords_file = passwords_file.readlines()

passwords = []
for line in passwords_file:
    passwords.append(line.rstrip().split(' '))

for password in passwords:
    password[1] = password[1].rstrip(':')

for password in passwords:
    password[0] = password[0].split('-')

def num_is_valid(password_lst):
    """Returns number of passwords valid based on criteria"""

    num_valid = 0

    for password in password_lst:
        min_num = int(password[0][0])
        max_num = int(password[0][1])
        required = password[1]
        given_password = password[2]
        required_count = 0
        for char in given_password:
            if char == required:
                required_count += 1
        if required_count >= min_num and required_count <= max_num:
            num_valid += 1

    return num_valid


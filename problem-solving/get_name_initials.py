def get_name_initials(name: str):
    lis = name.split()
    if len(lis) < 2:
        return "Name must contain at least two words."
    f = lis[0][0]
    l = lis[1][0]

    return f"{f.upper()}{l.upper()}"

print(get_name_initials("Ahmed Abdullatif"))  # Output: AA
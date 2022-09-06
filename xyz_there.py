def xyz_there(string: str) -> bool:
    if string[:3] == "xyz":
        return True

    for i in range(len(string)):
        if string[i - 1] != "." and string[i: i + 3] == 'xyz':
            return True
    return False

print(xyz_there('abcxyz'))
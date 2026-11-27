def normalize(lines):
    result = []
    for line in lines:
        value = line.strip()
        if value:
            result.append(value)
    return result

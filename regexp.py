def calculate(data, findall):
    matches = findall(r"([a-c])([-+]?)=([a-c]?)([-+]?\d*)")  # Регулярка делит на группы
    for v1, s, v2, n in matches:  # Передаем кортеж из групп такой структуры: var1, [sign]=, [var2], [[+-]number]
        if not s:
            data[v1] = (data.get(v2, 0) + int(n or 0))
        elif s == '-':
            data[v1] -= (data.get(v2, 0) + int(n or 0))
        else:
            data[v1] += (data.get(v2, 0) + int(n or 0))

    return data

def likes(team: list) -> str:

    if len(list) == 0:
        return "no one likes this"
    elif len(list) == 1:
        return "{list[0]} likes this"
    elif len(list) == 2:
        return "{list[0]} and {list[1]} like this"
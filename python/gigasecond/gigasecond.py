from datetime import timedelta as td


def add(moment):
    giga_delta = td(seconds=1000000000)
    new_time = moment + giga_delta
    return new_time

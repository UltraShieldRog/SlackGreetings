def time_converter(elapsed):
    hour = int(elapsed / 3600)
    left = elapsed % 3600
    minute = int(left / 60)
    seconds = left % 60
    return '{} h {} m {} s'.format(hour, minute, seconds)
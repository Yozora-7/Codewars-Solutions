"""
Clock shows h hours, m minutes and s seconds after midnight.

Your task is to write a function which returns the time since midnight in milliseconds.

"""

def past(h, m, s):
    hours = h * 60 * 60 * 1000
    minutes = m * 60 * 1000
    seconds = s * 1000 # convert each variable to milliseconds
    return hours + minutes + seconds

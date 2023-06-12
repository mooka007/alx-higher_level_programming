#!/usr/bin/python3
# Author - MoOka
def multipe_returns(sentence):
    if sentence == "":
        char = None
    else:
        char = sentence[0]
    return (len(sentence), char)

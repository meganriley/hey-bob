def response(hey_bob):
    bob = hey_bob.strip()
    if bob == '':
        return 'Fine. Be that way!'
    elif bob[-1] == '?' and bob.isupper():
        return 'Calm down, I know what I\'m doing!'
    elif bob[-1] == '?':
        return "Sure."
    elif bob.isupper():
        return 'Whoa, chill out!'
    else:
        return 'Whatever.'

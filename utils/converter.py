from datetime import datetime
import functools
import signal
import re

def date_convert(_input):
    return datetime.strptime(_input, '%m/%d/%Y').strftime('%B %d, %Y')

# timecontrol decorator
def timeout(sec):
    def decorator(func):
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            def _handle_timeout(signum, frame):
                err_msg = f'Function {func.__name__} timed out after {sec} seconds'
                raise TimeoutError(err_msg)
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(sec)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result
        return wrapped_func
    return decorator

def find_match_in_sentence(input_sentence, choices):
    input_sentence = re.sub('[^\w\s]', '', input_sentence)
    words = input_sentence.split()
    choices_lower = [choice.lower() for choice in choices]
    for word in words:
        if word.lower()   in choices_lower:
            return [choice for choice, choice_lower in zip(choices, choices_lower) if choice_lower == word.lower()][0]
    return 'NotFound'

def find_match_value(input_sentence):
    input_sentence = re.sub('[^\w\s]', '', input_sentence)
    values = re.findall('\d+', input_sentence)
    if len(values)>0:
        return int(values[0])
    return -1

def person_convert(profile):
    profile = profile.replace('I am ', 'You are ')
    profile = profile.replace('I was ', 'You were ')
    profile = profile.replace('My ', 'Your ')
    profile = profile.replace('I ', 'You ')
    profile = profile.replace('my ', 'your ')
    return profile

def can_positive_int(s):
    try:
        t = int(s)
        if t >= 0 :
            return True
        else:
            return False
    except:
        return False
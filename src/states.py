STATE_MENU = 0
STATE_ZONE = 1
STATE_MAP = 2

state = {
    'current': STATE_ZONE,
    'last': -1
}

def get_current():
    return state['current']

def get_last():
    return state['last']

def set_current(current_state):
    state['current'] = current_state

def set_last(last_state):
    state['last'] = last_state
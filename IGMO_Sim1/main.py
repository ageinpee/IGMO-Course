from enum import Enum
import uuid


class LKW_state_enum(Enum):
    LOADING = 0
    LOADING_QUEUE = 1
    WEIGHTING = 2
    WEIGHTING_QUEUE = 3
    EMPTYING = 4

next_state = {LKW_state_enum.LOADING: LKW_state_enum.WEIGHTING_QUEUE,
                  LKW_state_enum.LOADING_QUEUE: LKW_state_enum.LOADING,
                  LKW_state_enum.WEIGHTING: LKW_state_enum.EMPTYING,
                  LKW_state_enum.WEIGHTING_QUEUE: LKW_state_enum.WEIGHTING,
                  LKW_state_enum.EMPTYING: LKW_state_enum.LOADING_QUEUE}



class LKW:

    def __init__(self, id, state, waiting_time):
        self.id = id
        self.state = state
        self.waiting_time = waiting_time

        next_event_at = 0
        next_event_type = next_state[self.state]


def run(rounds, no_LKW, no_loadingstations, no_scales):


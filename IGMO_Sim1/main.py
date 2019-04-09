from enum import Enum
import uuid
import random


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

    def next_state(self):
        self.state = next_state[self.state]
        self.waiting_time = self.update_waiting_time(self.state)

    def update_waiting_time(self, state):
        rand = random.randomrange(0, 100)
        print(rand)
        if state == LKW_state_enum.LOADING:
            if rand < 10:
                return 16.0
            elif rand < 30:
                return 10.0
            elif rand > 30:
                return 12.0
        elif state == LKW_state_enum.WEIGHTING:
            if rand < 20:
                return 24.0
            elif rand < 35:
                return 18.0
            elif rand > 35:
                return 16.0
        elif state == LKW_state_enum.EMPTYING:
            if rand < 10:
                return 120
            elif rand < 15:
                return 80
            elif rand > 15:
                return 60
        else:
            return 0


def run(rounds, no_LKW, no_loadingstations, no_scales):


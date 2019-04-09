import uuid
from .LKW import LKW
from .LKW import LKW_state_enum

def run(rounds, no_LKW, no_loadingstations, no_scales):
    list_of_LKWs = []

    for lkw in no_LKW:
        list_of_LKWs.append(LKW(uuid.uuid1(), LKW_state_enum.LOADING_QUEUE, 0))

    print(list_of_LKWs)


run(0, 5, 0, 0)
"""
This problem was asked by Snapchat.
Given an array of time intervals (start, end) for classroom lectures (possibly
overlapping), find the minimum number of rooms required.
For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

"""

time_set = [(30, 75), (10, 15), (11, 25), (0, 50), (32, 50), (60, 150)]

EVENTS = dict(
    start="START",
    end="END"
)


class Event(object):
    def __init__(self, time, type):
        self.time = time
        self.type = type

    def __str__(self):
        print(self.time)


def form_event_list(time_set):
    event_list = []

    for start, end in time_set:
        event_list.append(Event(start, EVENTS['start']))
        event_list.append(Event(end, EVENTS['end']))

    return sorted(
        event_list, key=lambda x: x.time
    )


def find_min(event_list):
    number_of_classes = 0
    class_count = 0

    for event in event_list:
        if event.type == EVENTS['start']:
            class_count += 1
        elif event.type == EVENTS['end']:
            class_count -= 1

        number_of_classes = max(number_of_classes, class_count)

    return number_of_classes


events = form_event_list(time_set)

for event in events:
    print(event.time, event.type)

print(find_min(events))
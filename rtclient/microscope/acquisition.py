
class Acquisition:
    """
    Store and iterates over a set of events that run forever
    
    """

    def __init__(self, events):
        self.events = events
        self.next_event_no = 0
        self.one_loop_length = len(self.events)

    def __next__(self):
        if self.next_event_no > self.one_loop_length - 1:
            return None
        else:
            current_event = self.events[self.next_event_no]
            self.next_event_no += 1
            return current_event
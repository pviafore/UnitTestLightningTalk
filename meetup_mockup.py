class Meetup(object):

    def __init__(self, organizer):
        self.organizer = organizer

    def get_attendees(self):
        return [self.organizer]
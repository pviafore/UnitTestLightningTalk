class Meetup(object):

    def __init__(self, organizer, email=None):
        self.attendees = [organizer]
        self.emails = []
        if email:
            self.emails.append(email)

    def get_attendees(self):
        return self.attendees

    def add_attendee(self, attendee, email=None):
        if email:
            self.emails.append(email)
        self.attendees.append(attendee)

    def send_message_to_all_attendees(self, message, emailer):
        for email_address in self.emails:
            emailer.email(email_address, message)
        
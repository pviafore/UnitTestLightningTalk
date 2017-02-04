import unittest
from meetup_mockup import Meetup


class MockEmailer(object):
    def __init__(self):
        self.messages_received = {}

    def email(self, to, message):
        if to in self.messages_received:
            assert False
        self.messages_received[to] = message
        

class TestMeetupMockup(unittest.TestCase):

    def test_new_meetup_has_only_organizer_as_attendee(self):
        meetup = Meetup("Pat Viafore")
        assert meetup.get_attendees() == ["Pat Viafore"]

        meetup2 = Meetup("Zane Viafore")
        assert meetup2.get_attendees() == ["Zane Viafore"]

    def test_can_add_attendees(self):
        meetup = Meetup("Pat Viafore")
        meetup.add_attendee("Zane Viafore")
        assert ["Pat Viafore", "Zane Viafore"] == sorted(meetup.get_attendees())

    def test_can_send_out_message(self):
        meetup = Meetup("Pat Viafore", "patviafore@gmail.com")
        meetup.add_attendee("Zane Viafore", "icantevenreadyet@gmail.com")
        emailer = MockEmailer()
        meetup.send_message_to_all_attendees("Hooray, Python", emailer)
        assert emailer.messages_received["patviafore@gmail.com"] == "Hooray, Python"
        assert emailer.messages_received["icantevenreadyet@gmail.com"] == "Hooray, Python"

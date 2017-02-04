import unittest
from meetup_mockup import Meetup

class TestMeetupMockup(unittest.TestCase):

    def test_new_meetup_has_only_organizer_as_attendee(self):
        meetup = Meetup("Pat Viafore")
        assert meetup.get_attendees() == ["Pat Viafore"]

        meetup2 = Meetup("Patrick Viafore")
        assert meetup2.get_attendees() == ["Patrick Viafore"]

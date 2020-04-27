import unittest
from unittest.mock import patch, Mock
from datetime import datetime
from get_booking_status import get_booking_status


class TestGetBookingStatus(unittest.TestCase):
    def test_if_booking_status_is_cancelled(self):
        booking = Mock(cancelled=True)

        result = get_booking_status(booking)

        self.assertEqual(result, 'Cancelled')

    def test_if_is_fully_paid_should_return_true(self):
        booking = Mock(cancelled=False)
        booking.is_fully_paid.return_value = True

        result = get_booking_status(booking)

        self.assertEqual(result, 'Paid')

    @patch('get_booking_status.datetime')
    def test_if_booking_is_upcoming(self, datetime_mock):
        booking = Mock(cancelled=False, start=datetime(year=2020, month=4, day=26))
        booking.is_fully_paid.return_value = False
        datetime_mock.now.return_value = datetime(year=2020, month=4, day=25)

        result = get_booking_status(booking)

        self.assertEqual(result, 'Upcoming')

    @patch('get_booking_status.datetime')
    def test_if_all_conditions_are_false_should_return_message(self, datetime_mock):
        booking = Mock(cancelled=False, start=datetime(year=2020, month=3, day=26))
        booking.is_fully_paid.return_value = False
        datetime_mock.now.return_value = datetime(year=2020, month=4, day=26)

        result = get_booking_status(booking)

        self.assertEqual(result, 'Waiting taxes')


if __name__ == '__main__':
    unittest.main()

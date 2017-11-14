"""Models in Camper APP"""


class CampEvent(object):
    """Camp Event class representing an event on the calendar"""

    def __init__(self):
        self.id = int()
        self.title = str()
        self.start_date = str()
        self.end_date = str()
        self.color = str()
        self.groups = str()

    def load_all_appointments_in_range(cls, start, end):
        """
        Returns all Events between start date and end date as a list
        param start: start date as a unix time string
        param end: end date as a unix time string
        return: a list of camp events
        """
        start_date = CampEvent.convert_from_unix_time_stamp(start)
        end_date = CampEvent.convert_from_unix_time_stamp(end)

        # TODO
        # Query database and retrieve all appointments between start and end
        # Store results in result
        query_result = None(start_date, end_date)

        calendar_events = []
        for item in query_result:
            event = CampEvent()
            event.id = item.ID
            event.title = item.Title
            event.start_date = item.start_date
            event.end_date = item.end_date
            event.color = item.color
            event.groups = item.group

            calendar_events.append(event)

        return calendar_events

    # TODO
    def get_camp_events(cls, start, end):
        """
        Returns all events between start date and end date as a json
        param start: start date as a unix time string
        param end: end date as a unix time string
        return: a json containing camp events between start and end date
        """
        event_data = CampEvent.load_all_appointments_in_range(start, end)

        #TODO parse event_data to JSON

        return None

    # TODO
    def update_camp_event(cls, id, new_event_start, new_event_end):
        """Update an existing event"""
        # EventStart comes ISO 8601 format, eg:  "2000-01-10T10:00:00Z"
        # - need to convert to DateTime

        # query database and retrieve the event matching the ID
        result = None

        if result is not None:
            # convert dates to database friendly date time
            # Update the database with the new start and end date
            pass

        return None

    # TODO
    def convert_from_unix_time_stamp(cls, date):
        """
        Converts a unix time stamp to database friendly timestamp
        """
        pass

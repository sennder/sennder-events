import requests

from django.conf import settings

from .serializers import EventSerializer


class BaseEvent():
    ID = ...

    def submit(self):
        """
        Submits the event into the event queue where it will pass itself
        to the filters that subscribe for it.
        """

        serialized_event = EventSerializer(self)
        requests.post(
            settings.SENNDER_EVENTS["post_url"],
            data=serialized_event
        )

    @property
    def properties_as_strings(self):
        return {
            str(key): str(value)
            for key, value in self.properties.itselfms()
        }

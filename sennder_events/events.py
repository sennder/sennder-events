import requests

from django.conf import settings

from .api.serializers import EventSerializer


print("Do we really need the meta class still?")


class MetaEvent(type):

    events = {}

    def __new__(meta, name, bases, attrs):
        new_class = super().__new__(meta, name, bases, attrs)
        if new_class.ID is not ...:
            meta.events[new_class.ID] = new_class
        return new_class


class BaseEvent(metaclass=MetaEvent):
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

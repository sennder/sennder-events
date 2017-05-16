import requests

from django.conf import settings

from .serializers import EventSerializer


class BaseEventMeta(type):

    def __call__(cls, *args, **kwargs):
        obj = type.__call__(cls, *args, **kwargs)
        obj.check_properties_set()
        return obj


class BaseEvent(metaclass=BaseEventMeta):
    ID = ...

    def check_properties_set(self):
        if not hasattr(self, "properties"):
            raise NotImplementedError(
                "self.properties must be set in {class_name}".format(
                    class_name=type(self).__name__
                )
            )

    def submit(self):
        """
        Submits the event into the event queue where it will pass itself
        to the filters that subscribe for it.
        """

        serialized_event = EventSerializer(self).data
        response = requests.post(
            settings.SENNDER_EVENTS["POST_URL"],
            json=serialized_event
        )
        response.raise_for_status()

# Sennder Events

## Client library for issuing notifications to the sennder notifications service


### Installation

Make the sennder pypi repository available to pip:
```
export PIP_EXTRA_INDEX_URL=https://pypi.sennder.com/simple/
```

Install via `pip install sennder-events`

### Configuration

Add the following entry to your settings.py:

```
SENNDER_EVENTS = {
    "post_url": <your event processing API>
}
```

where `<your event processing API>` is the enpoint where the service part of the sennder notification framework is running. 
In our case, it is `'https://staging.api.sennder.com/api/notifications/events/'`

### Usage

Define your own events that inherit from `sennder_events.events.BaseEvent`.
The event must have a `properties` dictionary attribute that should be set during `__ini__`.
Calling `submit` will submit the event to the `post_url` specified in the settings. 

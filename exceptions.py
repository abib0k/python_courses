class EventException(Exception):
    pass
class Notification(EventException):
    pass

try:
    raise ZeroDivisionError
except Exception as e:
    if isinstance(e, Notification):
        print("Not a biggie, continue...")
    if issubclass(type(e), EventException):
        print("Custom failure, but painful one")
    else:
        print("It is a good day to die :(")

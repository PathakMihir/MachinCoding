from threading import Lock


class Connection:
    _instance = None
    _lock = Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
            return cls._instance
        else:
            print("Object Already created")
            return cls._instance

if __name__=="__main__":
    connection1=Connection()
    connection2=Connection()

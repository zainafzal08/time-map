class Event():
    def __init__(self, name):
        self.name = name
        self.start_date = None
        self.end_date = None
        self.info = None

class User():
    def __init__(self, name):
        self.name = name
        self.profile_pic = None
        self.groups = [] # list of group id's and names
        self.events = [] # list of event objects

class Group():
    def __init__(self, name):
        self.name = name
        self.members = [] # list of user objects
        self.events = [] # list of event objects
        # availability object summarising group
        # availability
        self.availability_summary = None
        # list of best times
        # tuple (start_time,end_time,list(who can make it))
        self.best = []

class Availability():
    def __init__(self):
        pass

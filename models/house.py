class House:
    def __init__(self, address, state, city, room, measure, owner):
        self.address = address
        self.state = state
        self.city = city
        self.room = room
        self.measure = measure
        self.owner = owner

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def get_city(self):
        return self.city

    def set_city(self, city):
        self.city = city

    def get_room(self):
        return self.room

    def set_room(self, room):
        self.room = room

    def get_measure(self):
        return self.measure

    def set_measure(self, measure):
        self.measure = measure

    def get_owner(self):
        return self.owner

    def set_owner(self, owner):
        self.owner = owner

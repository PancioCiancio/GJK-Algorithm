from property_keys import PropertyKey

class Properties:
    def __init__(self):
        self.entities = {}

    def create_entity(self) -> int:
        """ Creates a new entity and return its ID. """
        entity_id = len(self.entities)
        self.entities[entity_id] = {}
        return entity_id

    def set_property(self, entity_id: int, key: PropertyKey, value):
        """ Sets a property for the given entity """
        self.entities[entity_id][key] = value

    def get_property(self, entity_id: int, key: PropertyKey, default=None):
        """ Gets the given entity's property value, returning default if missing. """
        return self.entities[entity_id].get(key, default)

    def has_property(self, entity_id: int, key: PropertyKey) -> bool:
        """ Checks if an entity has a specific property """
        return key in self.entities[entity_id]
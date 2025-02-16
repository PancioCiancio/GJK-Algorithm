from enum import Enum
from .entity_registry import EntityRegistry

class PropertiesRegistry:

    def __init__(self, entity_registry: EntityRegistry):
        self.entities = {}

        # Used to generate entity ids.
        self.entity_registry = entity_registry


    def create_entity(self) -> int:
        """ Creates a new entity and return its ID. """
        entity_id = self.entity_registry.generate_entity()

        self.entities[entity_id] = {}
        
        return entity_id


    def destroy_entity(self, entity_id: int):
        """ Destroy the entry of the dictionary assigned to the entity id """
        self.entities.pop(entity_id)
        self.entity_registry.destroy_entity(entity_id)


    def set_property(self, entity_id: int, key: str, value):
        """ Sets a property for the given entity """
        self.entities[entity_id][key] = value


    def get_property(self, entity_id: int, key: str, default=None):
        """ Gets the given entity's property value, returning default if missing. """
        return self.entities[entity_id].get(key, default)


    def has_property(self, entity_id: int, key: str) -> bool:
        """ Checks if an entity has a specific property """
        return key in self.entities[entity_id]
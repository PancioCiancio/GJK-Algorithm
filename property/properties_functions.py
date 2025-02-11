from properties import Properties
from property_keys import PropertyKey

def set_transform(system: Properties, entity: int, position, rotation, scale):
    """ Set all entity's properties for transform """
    system.set_property(entity, PropertyKey.POSITION, position)
    system.set_property(entity, PropertyKey.ROTATION, rotation)
    system.set_property(entity, PropertyKey.SCALE, scale)

def get_transform(system: Properties, entity: int):
    """ Return all the entity's transform properties """
    return {
        PropertyKey.POSITION: system.get_property(entity, PropertyKey.POSITION, (0, 0)),
        PropertyKey.ROTATION: system.get_property(entity, PropertyKey.ROTATION, 0),
        PropertyKey.SCALE: system.get_property(entity, PropertyKey.SCALE, (1, 1)),
    }
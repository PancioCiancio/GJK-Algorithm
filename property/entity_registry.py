class EntityRegistry:
    """ 
    Generate entity IDs.

    @TODO:
    For simplicity we always advance the index and removed entity will be lost for ever.
    Implement a pool and add a versioning to each entity to know if they are recycled.
    """

    def __init__(self):
        self.enitity_id = 0


    def generate_entity(self) -> int:
        """ Return the new generated entity id """
        entity_id = self.enitity_id

        # Advancce the entity id by one.        
        self.enitity_id += 1

        return entity_id


    def destroy_entity(self, entity_id: int):
        """ Does nothing for now """
        pass
        
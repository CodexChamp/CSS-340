from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        USER = 'aacuser'
        PASS = 'C0de1sFun'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30564
        DB = 'AAC'
        

        # Initialize Connection
        self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}')
        self.database = self.client[DB]
        

    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            # self.database.animals.insert(data) # data should be dictionary
            # Store the results of the insert to variable
            insert_result = self.database.animals.insert_one(data)  # data should be dictionary

            # If insert was successful, return True, else, return False
            if insert_result.inserted_id is not None:
                status = True
            else:
                status = False
            return status
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Method to implement the R in CRUD.
    def read(self, data):
        # Verify that search criteria was provided, else raise an exception
        if data is not None:
            animals_collection = self.database.animals.find(data)

            # Return the animalsCollection cursor
            return list(animals_collection)
        else:
            raise Exception("No search criteria provided")
    def update(self, search_criteria, update_data):
        # Verify that search criteria and update data are provided
        if search_criteria is not None and update_data is not None:
            try:
                # Perform the update and store the result
                result = self.database.animals.update_many(search_criteria, {"$set": update_data})
                return result.modified_count  # Return the number of documents modified
            except Exception as e:
                print(f"Error: Update failed. Exception: {e}")
                return 0  # Return 0 if no documents were updated
        else:
            raise Exception("Search criteria or update data is missing")

    def delete(self, search_criteria):
        # Verify that search criteria is provided
        if search_criteria is not None:
            try:
                # Perform the delete operation and store the result
                result = self.database.animals.delete_many(search_criteria)
                return result.deleted_count  # Return the number of documents deleted
            except Exception as e:
                print(f"Error: Delete failed. Exception: {e}")
                return 0  # Return 0 if no documents were deleted
        else:
            raise Exception("Search criteria is missing")
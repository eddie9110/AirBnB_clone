#!/usr/bin/python3
""" File Storage module """
import json
from datetime import datetime
import os


class FileStorage:
    """ This class handles the storage of data """
    __file_path = "file.json"
    __objects = {}

    def classes(self):
        """the available commands wrt classes available """
        from models.base_model import BaseModel
        from models.state import State
        from models.amenity import Amenity
        from models.city import City
        from models.review import Review
        from models.user import User
        from models.place import Place

        cmd_store = {
                "BaseModel": BaseModel,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review,
                "User": User}
        return cmd_store

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with the key <obj class name>.id """
        ke_y = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[ke_y] = obj

    def save(self):
        """ mtd saves python dictionary to json file """
        save_file = {}
        for key, value in FileStorage.__objects.items():
            save_file[key] = value.to_dict().copy()
        with open(FileStorage.__file_path, "w") as fl:
            json.dump(save_file, fl)

    def reload(self):
        """ method responsible for deserialisation of JSON
        files to __objects if the JSON file __file_path exists """
        if not os.path.isfile(FileStorage.__file_path):
            return
        try:
            with open(FileStorage.__file_path, "r") as fl:
                obj_dict = json.load(fl)
        except Exception:
            return
        obj_dict = {w: self.classes()[e["__class__"]](**e) for w, e in
                    obj_dict.items()}
        FileStorage.__objects = obj_dict

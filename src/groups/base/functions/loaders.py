import json


class Loaders:
    """
    The loaders class.    
    """

    @staticmethod
    def load_json(json_string: str) -> dict:
        """
        Loads a JSON string into a dictionary.
        """
        return json.loads(json_string)
    
    @staticmethod
    def load_json_file(json_file_path: str) -> dict:
        """
        Loads a JSON file into a dictionary.
        """
        with open(json_file_path, "r") as json_file:
            return json.load(json_file)
        
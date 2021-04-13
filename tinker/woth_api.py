import requests

class WothAPI():
    # Woth Endpoint URL
    woth_url = "https://wordofthehour.org/cache/wordofthehour.json?src=python_woth_api"
    # Get raw data from endpoint
    @staticmethod
    def __fetch_raw():
        return requests.get(WothAPI.woth_url).json()
    # Get data from endpoint and put it into a simpler format
    @staticmethod
    def __fetch_all_fields():
        # Get raw data from endpoint
        raw_data = WothAPI.__fetch_raw()
        # Distinguish between old and new translations
        old_trans = {}
        new_trans = {}
        for field in raw_data:
            if len(field) > 5 and field[-5:] == "_edit":
                new_trans[field[:-5]] = raw_data[field]
            else:
                old_trans[field] = raw_data[field]
        # Overwriting old translations with new translations
        final_data = {}
        for field in old_trans:
            final_data[field] = old_trans[field]
        for field in new_trans:
            final_data[field] = new_trans[field]
        return final_data
    # Get only translation data (excluding id, sentences, and definitions)
    @staticmethod
    def fetch():
        # Get all data fields
        all_fields = WothAPI.__fetch_all_fields()
        # Initialize new data dictionary
        new_data = {}
        new_data["definitions"] = {}
        new_data["translations"] = {}
        # Fill in new data
        for field in all_fields:
            if field == "id":
                new_data["id"] = all_fields[field]
            elif len(field) > 12 and field[-12:] == "_definitions":
                new_data["definitions"][field[:-12]] = all_fields[field]
            elif len(field) > 9 and field[-9:] == "_sentence":
                # Sentences are not currently supported
                # We may add support for example sentences in the future
                continue
            else:
                if field == "english":
                    new_data["word"] = all_fields[field]
                new_data["translations"][field] = all_fields[field]
        return new_data
from woth_api import WothAPI
woth_data = WothAPI.fetch()
print(woth_data)
print(woth_data["word"])

#woth api taken from https://github.com/MichaelWehar/Word-of-The-Hour-API

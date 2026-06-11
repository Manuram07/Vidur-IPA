import re


def extract_memory(message):

    msg = message.lower()

    # My name is Ram
    if "my name is" in msg:

        value = message.split("my name is")[-1].strip()

        return {
            "key": "name",
            "value": value
        }

    # My goal is AI Engineer
    if "my goal is" in msg:

        value = message.split("my goal is")[-1].strip()

        return {
            "key": "goal",
            "value": value
        }

    return None
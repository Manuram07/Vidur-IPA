def extract_task(message):

    msg = message.lower()

    patterns = [
        "add",
        "create task",
        "todo",
        "to do",
        "i need to"
    ]

    for p in patterns:

        if p in msg:

            title = message

            for remove in patterns:
                title = title.lower().replace(remove, "")

            title = title.strip()

            return {
                "title": title
            }

    return None
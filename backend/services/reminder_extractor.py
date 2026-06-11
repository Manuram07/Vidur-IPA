def extract_reminder(message):

    msg = message.lower()

    if "tomorrow" in msg:

        title = (
            message
            .replace("Remind me", "")
            .replace("tomorrow", "")
            .strip()
        )

        return {
            "title": title,
            "remind_at": "tomorrow"
        }

    return None
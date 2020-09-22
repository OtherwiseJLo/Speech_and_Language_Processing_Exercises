import re
goodbye = re.compile(r"((good)?-?bye|exit|farewell)", re.IGNORECASE)


def parse_user_input(user: str) -> str:
    return f"ELIZA: {user}\nUSER: "


def run():
    user_input = ""
    response = "ELIZA: Hello, how are you?\nUSER: "
    while not bool(goodbye.search(user_input)):
        user_input = input(response)
        response = parse_user_input(user_input)
    print("ELIZA: COME BACK SOON!")

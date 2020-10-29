def hashPasscode(passcode: str) -> str:
    hash = 0

    for i, char in enumerate(passcode):
        print(char)
        hash += ord(char) * (31**(len(passcode) - i))

    return hash

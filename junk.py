def spam():
    print("SPAM!")

print(f"{__name__ = }")

if __name__ == "__main__":  # if run directly as script, NOT imported as module
    print("running as a script!")
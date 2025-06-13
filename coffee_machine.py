def greet(name: str) -> str:
    return f"Hello, {name}! 👋"

if __name__ == "__main__":
    user = input("Your name: ")
    print(greet(user))

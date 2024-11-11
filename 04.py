
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter a correct user name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command."
    return inner

contacts = {}

@input_error
def add_contact(args):
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added."

@input_error
def get_phone(args):
    name = args[0]
    return f"{name}: {contacts[name]}"

@input_error
def show_all(args):
    if not contacts:
        return "No contacts found."
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()

def main():
    print("Bot is running. Type 'exit' to quit.")
    
    while True:
        command = input("Enter a command: ").strip().lower()
        if command == "exit":
            print("Goodbye!")
            break
        
        if command.startswith("add"):
            args = input("Enter the name and phone separated by space: ").split()
            print(add_contact(args))
        
        elif command == "phone":
            args = input("Enter the name to find phone: ").split()
            print(get_phone(args))
        
        elif command == "all":
            print(show_all([]))
        
        else:
            print("Unknown command. Try 'add', 'phone', or 'all'.")

if __name__ == "__main__":
    main()

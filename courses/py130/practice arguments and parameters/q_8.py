def print_message(*, level="INFO", message="this is an informational message"):
    print(level, message)

print_message(message="This is a test message.", level="WARNING")
# [WARNING] This is a test message.

print_message(message="This is an informational message.")
# [INFO] This is an informational message.
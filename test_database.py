from database import (
    create_table,
    add_message,
    get_messages,
    update_message,
    delete_message
)

# Prepare database
create_table()

# CREATE
print("\n--- CREATE ---")
message_id = add_message(
    "Training Student",
    "My first SQLite database message"
)
print("Created message ID:", message_id)

# READ
print("\n--- READ ---")
print(get_messages())

# UPDATE
print("\n--- UPDATE ---")
updated = update_message(
    message_id,
    "My updated SQLite training message"
)
print("Records updated:", updated)
print(get_messages())

# DELETE
print("\n--- DELETE ---")
deleted = delete_message(message_id)
print("Records deleted:", deleted)

# READ AGAIN
print("\n--- FINAL DATABASE CONTENT ---")
print(get_messages())

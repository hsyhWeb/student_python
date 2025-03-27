# common.py
file_path = None

message_text = None
def update_values(new_path, new_message):
    global file_path, message_text
    file_path = new_path
    message_text = new_message


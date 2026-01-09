class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []  # List to store call history
        self.messages = []      # List to store messages

    # Method to make a call
    def call(self, other_phone):
        call_record = f"{self.phone_number} called {other_phone.phone_number}"
        print(call_record)
        self.call_history.append(call_record)

    # Method to show call history
    def show_call_history(self):
        print(f"Call history for {self.phone_number}:")
        if not self.call_history:
            print("No calls yet.")
        for record in self.call_history:
            print(record)

    # Method to send a message
    def send_message(self, other_phone, content):
        message = {
            'to': other_phone.phone_number,
            'from': self.phone_number,
            'content': content
        }
        self.messages.append(message)
        print(f"Message sent from {self.phone_number} to {other_phone.phone_number}: '{content}'")

    # Show outgoing messages
    def show_outgoing_messages(self):
        print(f"Outgoing messages from {self.phone_number}:")
        outgoing = [msg for msg in self.messages if msg['from'] == self.phone_number]
        if not outgoing:
            print("No outgoing messages.")
        for msg in outgoing:
            print(f"To {msg['to']}: {msg['content']}")

    # Show incoming messages
    def show_incoming_messages(self):
        print(f"Incoming messages for {self.phone_number}:")
        incoming = [msg for msg in self.messages if msg['to'] == self.phone_number]
        if not incoming:
            print("No incoming messages.")
        for msg in incoming:
            print(f"From {msg['from']}: {msg['content']}")

    # Show messages from a specific number
    def show_messages_from(self, other_phone):
        print(f"Messages from {other_phone.phone_number} to {self.phone_number}:")
        from_messages = [msg for msg in self.messages if msg['from'] == other_phone.phone_number and msg['to'] == self.phone_number]
        if not from_messages:
            print("No messages from this number.")
        for msg in from_messages:
            print(msg['content'])


# ------------------- TESTING -------------------
# Create phone objects
phone1 = Phone("123-456-7890")
phone2 = Phone("987-654-3210")

# Make calls
phone1.call(phone2)
phone2.call(phone1)

# Show call history
phone1.show_call_history()
phone2.show_call_history()

# Send messages
phone1.send_message(phone2, "Hello!")
phone2.send_message(phone1, "Hi, how are you?")
phone1.send_message(phone2, "I'm good, thanks!")

# Show outgoing and incoming messages
phone1.show_outgoing_messages()
phone1.show_incoming_messages()
phone2.show_outgoing_messages()
phone2.show_incoming_messages()

# Show messages from a specific number
phone1.show_messages_from(phone2)
phone2.show_messages_from(phone1)

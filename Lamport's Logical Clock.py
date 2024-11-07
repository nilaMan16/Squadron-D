class LamportClock:
    def __init__(self):
        self.time = 0

    def increment(self):
        self.time += 1

    def update(self, received_time):
        self.time = max(self.time, received_time) + 1

    def get_time(self):
        return self.time



# Process A
clock_A = LamportClock()
# Process B
clock_B = LamportClock()

# Internal event in Process A
clock_A.increment()
print(f"Process A time after internal event: {clock_A.get_time()}")

# Message sent from Process A to Process B
message_time = clock_A.get_time()

# Process B receives message and updates its clock
clock_B.update(message_time)
print(f"Process B time after receiving message: {clock_B.get_time()}")

# Internal event in Process B
clock_B.increment()
print(f"Process B time after internal event: {clock_B.get_time()}")

# Message sent from Process B to Process A
message_time = clock_B.get_time()

# Process A receives message and updates its clock
clock_A.update(message_time)
print(f"Process A time after receiving message: {clock_A.get_time()}")

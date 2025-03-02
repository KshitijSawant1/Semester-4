class PrinterSpoolerQueue:
    def __init__(self, maxsize):
        self.queue = [None] * maxsize
        self.maxsize = maxsize
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return self.rear == self.maxsize - 1

    def add_print_job(self, job):
        if self.is_full():
            print("Printer queue is full. Cannot add more jobs.")
            return
        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.queue[self.rear] = job
        print(f"Print job added: {job}")

    def process_print_job(self):
        if self.is_empty():
            print("No print jobs in the queue to process.")
            return

        # Process the job at the front and update front pointer
        job = self.queue[self.front]
        print(f"Processing print job: {job}")
        
        # Check if we are removing the last element
        if self.front == self.rear:
            self.front = self.rear = -1  # Reset queue to empty state
        else:
            self.front += 1

    def display_queue(self):
        if self.is_empty():
            print("Printer queue is empty.")
            return
        print("Current print jobs in queue:")
        for i in range(self.front,self.rear+1,1):
            print(f"Job = {self.queue[i]}" )
        print()

# Simulate Printer Spooler
psq = PrinterSpoolerQueue(5)

# Adding print jobs to the queue
psq.add_print_job("Document1.pdf")
psq.add_print_job("Document2.docx")
psq.add_print_job("Photo.jpg")
psq.add_print_job("Spreadsheet.xlsx")
psq.add_print_job("Presentation.pptx")

# Display queue
psq.display_queue()

# Processing print jobs
while not psq.is_empty():
    psq.process_print_job()

# Final queue status
psq.display_queue()

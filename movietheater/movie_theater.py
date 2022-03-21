class Main():
    def __init__(self,input_dict):
        self.input_data = input_dict
        self.rows = 10
        self.col = 20
        self.total_seats = self.rows * self.col
        self.buffer_seats = 3
        self.buffer_rows = 1
        self.seatMap = [[False for x in range(self.col)] for y in range(self.rows)] 

    def main(self):
        pass
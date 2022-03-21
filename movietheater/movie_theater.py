from collections import defaultdict
from posixpath import split
class Main():
    # Init fucntion
    def __init__(self,input_dict):
        self.input_data = input_dict
        self.rows = 11
        self.col = 20
        self.total_seats = self.rows * self.col
        self.buffer_seats = 3
        self.buffer_rows = 1
        # Seat Map represnts the entire theater in the form of a 2D boolean matrix
        self.seatMap = [[False for x in range(self.col)] for y in range(self.rows)]
        # Seat Remaning represnts the remaining seats in each row
        self.seatRemaning = [self.col]*self.rows
        # Final result
        self.final_res = defaultdict(list)

    # String reprentation of the class
    def __str__(self):
        print(f"Input data: {self.input_data}")
        print(f"Seat map: {self.seatMap}")
        print(f"Seat Remaning: {self.seatRemaning}")
        print(f"Final result: {self.final_res}")

    # Entry point of the program
    def make_reservation(self):
        for key,value in self.input_data.items():
            # Checking the edge cases for any invalid request
            # if key == "R012":
            #     import pdb
            #     pdb.set_trace()
            
            if value<=0: 
                self.final_res[key] = "Invalid Reservation"
                continue
            if value>self.get_total_seats():
                self.final_res[key] = "House full"
                continue
            req_number = key
            seat_requested = value
            # If seat requested is less than 20 then we just need to call assign_seats function once
            # otherwise we need to call assign_seats function recusrively until requested seats are satisfied
            if seat_requested >20:
                val= 0
                while seat_requested>20:
                    self.assign_seats(req_number,20)
                    seat_requested = seat_requested - 20
                if seat_requested>0:
                    self.assign_seats(req_number,seat_requested)
                    seat_requested = 0
            else:
                self.assign_seats(req_number,seat_requested)
        return self.final_res
    
    # Function for assigning seats
    def assign_seats(self,req_number,seat_requested):
        # if req_number == "R012":
        #     import pdb
        #     pdb.set_trace()
        total_required_seats = seat_requested
        book_seats = []
        for row_index in range(self.rows-1,0,-1):
            if self.get_seat_remaining_in_row(row_index)>=seat_requested:
                # Check if the seats are available in a group
                avl_seats = self.find_seats_together(seat_requested,row_index)
                # If it is possible to make groups seat together
                if avl_seats[0]!=-1:
                    last_seat_index = avl_seats[1]+seat_requested-1
                    # Mark the seats as occupied
                    row = avl_seats[0]
                    for seat_index in range(avl_seats[1],last_seat_index+1):
                        self.seatMap[row][seat_index] = True
                    self.fill_buffer_seats(avl_seats[0],avl_seats[1],seat_requested,last_seat_index)
                    self.seatRemaning[avl_seats[0]] -=seat_requested
                    self.total_seats -= seat_requested
                    counter = 0
                    while counter<total_required_seats:
                        self.final_res[req_number].append(f"{chr(avl_seats[0]+65-1)}{avl_seats[1]+counter+1}")
                        counter+=1
                    return
                else:
                    split_row = self.rows-1
                    while (total_required_seats>0 and split_row>=0):
                        if self.get_seat_remaining_in_row(split_row)>1:
                            for find_seat in range(self.col-1):
                                if self.seatMap[split_row][find_seat]==False:
                                    self.seatMap[split_row][find_seat] = True
                                    book_seats.append(str(split_row)+ " " + str(find_seat))
                                    self.final_res[req_number].append(f"{chr(split_row+65-1)}{find_seat+1}")
                                    self.total_seats-=1
                                    self.seatRemaning[split_row]-=1
                                    total_required_seats-=1
                        split_row-=1
                    self.fill_partition_buffer(book_seats)
                    return
                
                                


    # This function checks if it possible to make groups seat together
    def find_seats_together(self,seat_requested,row_index):
     
        res = [-1,-1]
        for row in range(row_index,-1,-1):
            # This row have sufficient seats but we need to check if the seats are available in 
            # a group.
            if self.get_seat_remaining_in_row(row)>=seat_requested:
                # Check if the seats are available in a group
                seat_counter = 0
                seat_count_remaining = seat_requested
                while seat_count_remaining>0:
                    # A particular seat in between is already occupied so we will reset the counter
                    if self.seatMap[row][seat_counter]:
                        seat_count_remaining = seat_requested
                    else:
                        seat_count_remaining -=1
                    if seat_counter!=self.col-1:
                        seat_counter = seat_counter + 1
                    else:
                        break
                if seat_count_remaining==0:
                    res = [row,seat_counter-seat_requested]
                    return res
        return res

    # This function takes care of filling buffer seats (both row buffer and col buffer )
    def fill_buffer_seats(self,row_index,col_index,seat_requested,last_seat):
        for num_row in range(1,self.buffer_rows+1):
            if row_index-num_row>0:
                for safety in range(seat_requested):
                    self.seatMap[row_index-num_row][col_index+safety] = True
                    self.seatRemaning[row_index-num_row] -=1
                    self.total_seats-=1
            if num_row+row_index<self.rows-1:
                for safety in range(seat_requested):
                    self.seatMap[row_index+num_row][col_index+safety] = True
                    self.seatRemaning[row_index+num_row] -=1
                    self.total_seats-=1
            for j in range(1,self.buffer_seats+1):
                if j+last_seat<=self.col-1:
                    self.seatMap[row_index][last_seat+j] = True
                    self.seatRemaning[row_index] -=1
                    self.total_seats-=1
                if col_index-j>=0 and not self.seatMap[row_index][col_index-j]:
                    self.seatMap[row_index][col_index-j] = True
                    self.seatRemaning[row_index] -=1
                    self.total_seats-=1

    # Fills the partition buffer in case of split seating arrangement
    def fill_partition_buffer(self,booked_seats):
        for seat_booked in booked_seats:
            seat = seat_booked.split(" ")
            get_col = int(seat[1])
            get_row = int(seat[0])
            row_counter = 1
            while row_counter<self.buffer_rows and get_row-row_counter>self.rows:
                row_above = get_row+row_counter
                row_below = get_row-row_counter
                if row_above<self.rows-1 and not self.seatMap[row_above][get_col]:
                    self.seatMap[row_above][get_col] = True
                if row_below>0 and not self.seatMap[row_below][get_col]:
                    self.seatMap[row_below][get_col] = True
                row_counter+=1
            col_counter = 1
            while col_counter<self.buffer_seats and get_col-col_counter>self.col:
                seat_l = get_col+col_counter
                seat_r = get_col-col_counter
                if seat_r<self.col and self.seatMap[get_row][seat_r]==False:
                    self.seatMap[get_row][seat_r] = True
                if seat_l>=0 and self.seatMap[get_row][seat_l]==False:
                    self.seatMap[get_row][seat_l] = True
                col_counter+=1
    
    def get_total_seats(self):
        total_seats = 0
        for i in range(1,len(self.seatMap)):
            for j in range(len(self.seatMap[i])):
                if self.seatMap[i][j]==False:
                    total_seats+=1
        return total_seats
    
    def get_seat_remaining_in_row(self,row_index):
        total_seats = 0
        for i in range(len(self.seatMap[row_index])):
            if self.seatMap[row_index][i]==False:
                total_seats+=1
        return total_seats
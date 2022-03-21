# walmart_backend_challange


[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![forthebadge](https://forthebadge.com/images/badges/gluten-free.svg)](https://forthebadge.com)

[![forthebadge](https://forthebadge.com/images/badges/powered-by-coffee.svg)](https://forthebadge.com)

## Problem Statement
Implement an algorithm for assigning seats within a movie theater to fulfill reservation requests. Assume the movie theater has the seating arrangement of 10 rows x 20 seats, as illustrated to the right. Your homework assignment is to design and write a seat assignment program to maximize both customer satisfaction and customer safety. For the purpose of public safety, assume that a buffer of three seats and/or one row is required.

**Input Description**
You will be given a file that contains one line of input for each reservation request. The order of the lines in the file reflects the order in which the reservation requests were received. Each line in the file will be comprised of a reservation identifier, followed by a space, and then the number of seats requested. The reservation identifier will have the format: R####. See the Example Input File Rows section for an example of the input rows.

**Output Description**
The program should output a file containing the seating assignments for each request. Each row in the file should include the reservation number followed by a space, and then a comma-delimited list of the assigned seats. See the Example Output File Rows section for an example of the output file content.

### My Approach

Steps taken to solve the problem:

1. As in the problem statement it is mentoined that input will be provided through an input file of an specified format so I wrote an input parser which can parse the given input file and generate a dictioanry with key being the request id (*R001*) and value being the number of seats that need to be booked for that given id.
2. The most important part of the problem statement is to create the algorithm for assigning the seats as efficiently as possible. For this I developed a greedy approach based algorithm. The algorithm branches into two major chunks based on whether it is possible to assign seats together in a group or not. 
3. As customer satisfication is of utmost priority, so in my algorithm I first recursively check for free chunk of space in each row. If for a particular request id there is a contiguous block of free space equal to the number of requested seats is availlable in any row, I assign that block to that particular request id. Otherwise if no such contiguos block is available I assign seats seperately based in the availability of seats in each row.
4. If for any request_id number free seats in the theatre becomes less than number of requested seat, that particular request is not fufilled and a message of **House Full** is displayed against that particular request id in the final result.
5. After iterating through all possible requests, the final output is written to an output file using a writer function which takes care of generating the output in the format provided in the problem statement.

### My Assumptions

While designing the solution of this project, I took a couple of assumptions which are as follows:

1. Price of each seat in the theatre is constant irresptive of the position of the seat.
2. Customers have no say in the location of the seats they are assigned to, they only care about the getting certain number of seats booked.
3. I have assumed that theatre is designed in such a way that back seats have better view than the front seats and it is okay to assing better on first come first serve basis
4. I have assumed that all the members of a same group wants to sit together irresoective of the location of seat they get.

### Scope of improvement

The solution for this problem statement is designed and developed in a very short period of time, and hence it is far from an ideal implementation for such projects. I have mentoined a couple of things which can be done to bring it close to a real world implementation of such a system  
1. Right now I am greedilty assigning seats starting from the last row on first come first serve basis. A better implementation can be to assign seats based on location , such as the best located seats of the theater should be assigned first.
2. Right now I am assuming that the utmost priority of all members of a group is to seat together irrespective of the seat that they are getting. A better implementation can be to take some kind of input from members which can coomunicate their priorities clearly.
3. Right now my algorithm uses a Greedy based approach to assign seats. Some better and more efficient approach can be devised for the same.
4. Due to lack of time, I have written a small test suite with just three test cases, for a real world application an extensive test suite would be required.
5. The logic for adding row and column buffer is quite complicated and comprises of multiple if and else check. In real world scenario this logic can be simplified to make the code more readable and less error prone.

	










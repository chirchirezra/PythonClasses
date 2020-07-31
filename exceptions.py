import sys

my_dict = {'a':5,'b':29,'c':67,'d':'Python dict '}

# try:
#     raw_key = input("Kindly enter the key \n >")
#     print(my_dict[str(raw_key)])
# except KeyError as e:
#     print('The supplied key could\'t be matched')

try:
    
    args= [arg for arg in sys.argv]
    for i in args:
        try:
            integer = int(i)
            print(i)
        except ValueError:
            print('All input values must be integers')
        


except(IndexError,ValueError):
    print('Kindly enter an integer')

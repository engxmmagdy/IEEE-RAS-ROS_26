

string = "___ROS___"

def write_log(string):
    with open("messages.txt","a") as file:
        file.write(string)
        file.write("\n")


def read_logs():
    with open("messages.txt","r") as file:
        for line in file:
            print(line.strip())
    

write_log(string)
read_logs()
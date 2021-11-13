Users_File = open("Users.txt", "w", encoding='utf8')

Master_List = []
Duplicate_Users = 0
Messages_Sent = 0
Zero_Message_Andy = 0
Number_Of_File = int(input("HOW MANY FILES DO YOU HAVE TO IMPORT?\n"))

while Number_Of_File > 0:
    temp_File = open(input("WHAT FILE WOULD YOU LIKE TO IMPORT?\n"), encoding='utf8')
    temp_List = temp_File.readlines()
    Master_List = Master_List + temp_List
    temp_File.close()
    Number_Of_File = Number_Of_File - 1

# print(Master_List)
for x in Master_List:
    if (x[0] == "[" and x[19] == "]"):
        Messages_Sent += 1


User_List = []
loop_position = 0
for x in Master_List:
    if (x[0] == "[" and x[19] == "]" and Master_List[loop_position + 1].__contains__("Joined the server.")):
        # print(x.split("] ", 1)[1])
        Temp_String = x.split("] ", 1)[1]
        Temp_String = Temp_String[0:-1]
        if (Temp_String in User_List or Temp_String.__contains__("Deleted User#0000")):
            Duplicate_Users += 1
        else:
           # User_List.append(x.split("] ", 1)[1])
            User_List.append(Temp_String)
    loop_position += 1
print(User_List)
rows, cols = (len(User_List), 5)
Master_Data = []
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(0)
    Master_Data.append(col)

loop_position = 0
for row in Master_Data:
    Temp_String = str(User_List[loop_position])
    Master_Data[loop_position][0] = Temp_String
    loop_position += 1

loop_position = 0
for x in Master_List:
    if (x[0] == "[" and x[19] == "]" and "Joined the server." not in str(Master_List[loop_position + 1]) and "Deleted User#0000" not in x and " (pinned)" not in x):
        Temp_User = x.split("] ", 1)[1]
        Temp_User = Temp_User[0:-1]
        Temp_String = str(Master_List[loop_position + 1])
        Word_count = len(Temp_String.split())
        Letter_Count = len(Temp_String)+1
        if(any(Temp_User in sublist for sublist in Master_Data)):
            for i in range (0, len(Master_Data)):
                if Master_Data[i][0] == Temp_User:
                    Master_Data[i][1] += 1
                    Master_Data[i][3] += Word_count
                    Master_Data[i][4] +=Letter_Count
        else:
            print(Temp_User + " NOT FOUND")
            Master_Data.append([Temp_User, 1, 0, Word_count, Letter_Count])
    loop_position += 1


for i in range (0, len(Master_Data)):
    if Master_Data[i][1] != 0:
        Master_Data[i][2] = round((Master_Data[i][1]/Messages_Sent)*100, 2)


for i in range (0, len(Master_Data)):
    if Master_Data[i][1] == 0:
        Zero_Message_Andy += 1
print(str(Messages_Sent))
Master_Data.sort(key=lambda row: (row[1], row[3]), reverse=True)
Users_File.write(str(len(User_List)) + " unique users have joined the server\n")
Users_File.write("There are " + str(Duplicate_Users) + " People who have joined more then once\n")
Users_File.write(str(Zero_Message_Andy) + " People are zero message Andys\n\n")
Users_File.write("Here is the sorted data\n\n")
Users_File.write("['Username#0000', messages sent, percentage of server messages, word count, keyboard clicks] \n\n")
for row in Master_Data:
    Users_File.write(str(row) + "\n")

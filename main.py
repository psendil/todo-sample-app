from ToDoSampleApp import ToDo
from ToDoDynamo import Dynamo

todo_item = ToDo("milk", "today", "noon", "get milk")

print (todo_item.get_description())
print (todo_item.get_title())

table_name = Dynamo("todo",todo_item)

if not table_name.checkTable():
    table_name.createTable()
    table_name.putItem()
else:
    print ("table already exists")
    table_name.putItem()
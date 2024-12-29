## Create a To List To Keep Track Of Task

to_do_list =["Buy Groceries","Clean the House","Pay bills"]

##Adding More Task
to_do_list.append("Schedule Metting")
to_do_list.append("Go For Run")

## Removing a Completed task
to_do_list.remove("Clean the House")

##Checking if a task is in the list 

if "pay bills" in to_do_list:
    print("Dont's forget the Pay bills") 
    
print("To Do List Remaining Task ")
for task in to_do_list:
    print(f"-{task}")
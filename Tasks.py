from datetime import datetime
import uuid


class Tasks:
    task_no = 1

    def __init__(self, title):
        self.id = str(uuid.uuid4())

        self.task_name = title
        self.created_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.updated_time = 'NA'
        self.completed = False
        self.completed_time = 'NA'
        self.task_idno = Tasks.task_no
        Tasks.task_no += 1

    def updateName(self, update_name):
        self.task_name = update_name
        self.updated_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def complete(self):
        self.completed = True
        self.completed_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def print_tasks(self):
        return f" ID-{self.id}\n Task - {self.task_name}\n Created time -  {self.created_time} \n Updated time - {self.updated_time} \n Completed - {self.completed} \n Completed time - {self.completed_time}"

    def print_tasksto_update(self):
        return f" Task No-{self.task_idno}\n ID-{self.id}\n Task - {self.task_name}\n Created time -  {self.created_time} \n Updated time - {self.updated_time} \n Completed - {self.completed} \n Completed time - {self.completed_time}"


class TaskList:
    def __init__(self):
        self.task_collection = []

    def add_task(self, task_name):

        self.task_collection.append(task_name)

    def view_tasks(self):

        for task in self.task_collection:

            print(task.print_tasks())
            print("\n")

    def incomplete_tasks(self):
        task_found = True

        for task in self.task_collection:
            if task.completed == False:
                print(task.print_tasksto_update())
                print("\n")
                task_found = False
        if task_found:
            print("No task to update")

    def complete_tasks(self):
        task_found = True

        for task in self.task_collection:
            if task.completed == True:
                print(task.print_tasksto_update())
                print("\n")
                task_found = False
        if task_found:
            print("\nNo complete Task found...\n")

    def update_tasks(self):
        task_found = False

        for task in self.task_collection:
            if task.completed == False:
                print(task.print_tasksto_update())
                print("\n")
                task_found = True

        if task_found:
            print("Select which task to update..\n")

            update_no = int(input("Enter Task No: "))
            for task_id in self.task_collection:
                if task_id.task_idno == update_no:
                    update_name = input("Enter new Task:")
                    task_id.updateName(update_name)
                    print("\nTask updated successfully!..\n")
        else:
            print("No task to update")

    def uncomplete_task(self):
        task_found = False

        for task in self.task_collection:
            if task.completed == False:
                print(task.print_tasksto_update())
                print("\n")
                task_found = True

        if task_found == False:
            print("\nNo task found\n")

        return task_found

    def complete_task(self, task_id):
        for task in self.task_collection:
            if task.task_idno == task_id:
                task.complete()


def main():
    task_list = TaskList()

    while True:

        print("1.Add New Task")
        print("2.Show All Task")
        print("3.Show all incomplete tasks")
        print("4.Show all completed tasks")
        print("5.Update Task")
        print("6.Mark A Task completed")

        userinput = int(input("Enter A option :"))

        if userinput == 1:
            new_task = input("Enter New Task: ")
            create_task = Tasks(new_task)
            task_list.add_task(create_task)

            print("\nTask added successfully!!\n\n")
        elif userinput == 2:
            print("\n")
            task_list.view_tasks()
            print("\n")
        elif userinput == 3:
            task_list.incomplete_tasks()
        elif userinput == 4:
            task_list.complete_tasks()
        elif userinput == 5:

            task_list.update_tasks()
        elif userinput == 6:

            taskfound = task_list.uncomplete_task()
            if (taskfound):
                print("Select which task to complete:")
                complete_no = int(input("Enter Task no:"))
                task_list.complete_task(complete_no)
                print("\nTask complete successfully\n")


main()

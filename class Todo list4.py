class TodoList:
    tasks=[]

    def add_task(self, task):
        self.tasks.append(task)

    def show_tasks(self):
        count = 1
        while count <= len(self.tasks):
            print(f"{count}. {self.tasks[count-1]}")
            count+=1

    def remove_task(self, index):
        self.tasks.remove(self.tasks[index-1])


my_list = TodoList()
my_list.add_task("Купить хлеб")
my_list.add_task("Сделать зарядку")
my_list.show_tasks()
my_list.remove_task(1)
my_list.show_tasks()
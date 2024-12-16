import task_1
import task_2
import task_3
import task_4
import task_5
import task_6



class Tasks:
    def task_1(self):
        task_1.run()

    def task_2(self):
        task_2.run()

    def task_3(self):
        task_3.run()

    def task_4(self):
        task_4.run()

    def task_5(self):
        task_5.run()

    def task_6(self):
        task_6.run()



if __name__ == "__main__":
    tasks = Tasks()
    flag = True
    while flag:
        command = input("Task: ")
        if command.isdigit():
            command = int(command)
            match command:
                case 1:
                    tasks.task_1()
                case 2:
                    tasks.task_2()
                case 3:
                    tasks.task_3()
                case 4:
                    tasks.task_4()
                case 5:
                    tasks.task_5()
                case 6:
                    tasks.task_6()
            flag = False







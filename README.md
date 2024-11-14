# MyToDo
It is a basic GUI application that allows us to track and analyze our tasks daily. To be honest, I was not interested in designing and it was my first time using this library. So, sorry for the design :)


Everyone is doing some routine tasks daily. Being one of them and wanting to get experience in another programming language's GUI libraries have made me try this project. So, I have decided to go with Python's Tkinter library. It is a very basic Python GUI application.

This application allows you to apply basic CRUD operations, which means create (add) new tasks, read them, delete them, and update them.



- The application basically looks like this. In the top section, the buttons can be used to perform these CRUD operations. Also, the Analyze button can be used to analyze how good you are at performing these tasks.

![image](https://user-images.githubusercontent.com/44292203/202788856-17e0ca24-0477-4995-aba7-7a56ba68e14c.png)

- And checklist buttons stay as ticked in a day. When the new day begins, the data gets reset. Also, when you forget to update last day's data or you were not able to be on the computer, you can edit your last day's data by clicking the "Update Last Day Data" button.

- Having no data will cause the program to welcome you like that:

![image](https://user-images.githubusercontent.com/44292203/202730689-ad32e0c9-5a86-42ff-8ca4-227370ec0af3.png)




# Buttons

- Let's start by adding new tasks. When you click the button, a frame that looks exactly like below will welcome you. You need to enter the task number you want to add. Warning: The text must be an integer or higher than 0, or you will see an error message!

![image](https://user-images.githubusercontent.com/44292203/202723047-5e8e15ca-0962-4d34-bc33-68e75ec2cc83.png)

- Then, you need to add the tasks you want to add by the number you have just entered. Entering the task that you have already added will cause an error message too!

![image](https://user-images.githubusercontent.com/44292203/202723729-6b48c3e9-9cc4-4be5-934c-da2dc91d4fd3.png)

- After adding all the tasks you want to add, the main frame will welcome you, as you can see below in the screenshot with the added new task.

![image](https://user-images.githubusercontent.com/44292203/202793174-757bb080-b002-49d1-80f0-e91b803de279.png)

- Let's continue with the second button, which helps us to perform the update process. When you think that the task does not suit you or another opinion, you can just update the task by clicking the update button. This screen will welcome you. You can also scroll down to see all of your tasks.

![image](https://user-images.githubusercontent.com/44292203/202793299-a5e1e5d3-c009-4138-8659-88661d093ffe.png)

- I just want to update the task I've just added. So I've written some text for the entry that I want to update.

![image](https://user-images.githubusercontent.com/44292203/202725925-6e9870dc-2084-42bf-81df-03ea05835069.png)

- Clicking the button will update the task immediately. 
 
![image](https://user-images.githubusercontent.com/44292203/202793426-30419945-f515-42a4-a732-1019c738f4ec.png)

- And now, I want to delete a task. Let's delete the task lastly added. On this screen, I just scroll down to the task I want to delete and click the button below.

![image](https://user-images.githubusercontent.com/44292203/202793560-9bb68022-03ea-4b6b-90aa-d0375d9ca02e.png)

- And it is done!

![image](https://user-images.githubusercontent.com/44292203/202793636-bb5ab8bc-1827-4993-bf6b-276eb62d9603.png)

- How to update the last day's data? For this, just click on the button, and this frame will welcome you with the last day's data, whether it is ticked or not. You can just click the checkbox of the task you want to update.

![image](https://user-images.githubusercontent.com/44292203/202794166-4626c111-c9d6-4092-a35b-2650f1b6770b.png)

- And let's analyze myself. By clicking this button, this frame will welcome you. Here, you can see your past data. 3 different types of data we have. Last day's, 15 days of and 30 days of data. How good were you to accomplish your task day by day? And how many tasks have you added day by day? You can see both of them from the opened frame.

![image](https://user-images.githubusercontent.com/44292203/202794294-a6202aeb-a529-4c6d-801e-f91a17d4c8df.png)

# And the data is being saved by how?

- A file named MyToDo. CSV helps us to save our data. I've decided to use a csv file to keep the data. The file looks like the below. Tasks that you were able to do will take the value 1, while the others take 0. A date is being added if you run the program in a day. Running the program every day will keep your everyday's data.

![image](https://user-images.githubusercontent.com/44292203/202794646-1802ec73-2dbb-455a-9f5e-d74fc2c048a1.png)

- Performing CRUD operations or ticking a checkbox will update the data in the csv file immediately. Also, let's assume that you want to add new data after 15 days of using this application. After the add operation, the value of the added day will get 0 while the past days get the NaN value. Adding new tasks after a few days means this task was not part of you before. So, you can only update starting from the last day. Of course you can edit the values of that column from the csv file.


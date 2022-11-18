# MyToDo
It is a basic GUI application that provides us to track and analyse our tasks daily.


Everyone is doing some routine tasks daily. Being one of them and wanting to get experience in another programming language's GUI libraries have made me to try this project. So, I have decided to go with Python's Tkinter library. It is a very basic Python GUI application.

This application allow you to apply basic CRUD operations which means Create (Add) new tasks, Read them, Delete them and Update them.



- The application basically looks like this. In the top section, the buttons can be used to performs this CRUD operations. Also Analyse button can be used to analyse how good are you to perform these tasks.

![image](https://user-images.githubusercontent.com/44292203/202720025-0dcfce7d-fdd6-4825-ac93-9a0742fda8c0.png)

- And checklist buttons stay as ticked in a day. When the new day begins, the data gets resetted. Also, when you forget to update last day's data or you were not be able to be on the computer, you can edit your last day's data by clicking "Update Last Day Data" button.



# Buttons

- Let's start from adding new tasks. When you click the button, a frame which looks exact like below will welcome you. You need to enter the task number you want to add. Warning: The text must be integer or higher than 0 or you will see an error message!

![image](https://user-images.githubusercontent.com/44292203/202723047-5e8e15ca-0962-4d34-bc33-68e75ec2cc83.png)

- Then, you need to add the tasks you want to add by the number you have just entered. Entering the task that you have already added will cause an error message too!

![image](https://user-images.githubusercontent.com/44292203/202723729-6b48c3e9-9cc4-4be5-934c-da2dc91d4fd3.png)

- After adding all the tasks you want to add, main frame will welcome you as you can see below in the screenshot with the added new task.

![image](https://user-images.githubusercontent.com/44292203/202724180-eed55a40-3bc3-47ce-b99f-55198fa5f927.png)

- Let's continue with the second button which helps us to perform Update process. When you think that the task does not suit you or another opinion, you can just update the task by clicking the update button. This screen will welcome you. You can also scroll down to see all of your tasks.

![image](https://user-images.githubusercontent.com/44292203/202724578-945c4a96-06c2-40cb-ab33-ed877ca5c675.png)

- I just want to update the task I've just added. So I've written some text which to entry that I want to update to.

![image](https://user-images.githubusercontent.com/44292203/202725925-6e9870dc-2084-42bf-81df-03ea05835069.png)

- Clicking the button will update the task immediately.  
 
![image](https://user-images.githubusercontent.com/44292203/202726087-84965d49-9183-49c1-a161-2797907f8612.png)

- And now, I want to delete a task. Let's delete the task lastly added. In this screen, I just scroll down to the task I want to delete and click to the button below.

![image](https://user-images.githubusercontent.com/44292203/202726529-98663759-6d7e-4777-b2cd-05b512e43bb7.png)

- And it is done!

![image](https://user-images.githubusercontent.com/44292203/202726747-748c7368-3a43-4eef-bcac-d76d61b4b98b.png)

- How to update the last day's data? For this, just click to the button and this frame will welcome you with the last day's data whether it is ticked or not. You can just click the checkbox of the task you want to update.

![image](https://user-images.githubusercontent.com/44292203/202726863-02312cdc-9049-4cc7-9a07-83a0919fff50.png)

- And let's analyse myself. By clicking this button, this frame will welcomes you. Here, you can see your past data. 3 different type of data we have. Last day's, 15 days of and 30 days of data. How good were you to accomplish your task day by day? and how many tasks you have added day by day? you can see both of them from the opened frame.

![image](https://user-images.githubusercontent.com/44292203/202727232-b2d86a7f-63ef-496c-9ecf-b60b470ca50d.png)

# And the data is being saved by how?

- A file named MyToDo.csv helps us to save our data. I've decided to use csv file to keep the data. The file looks like the below. Tasks that you were able to done will take the value 1 while the others take 0. Date is being added if you run the program in a day. Running the program everyday will keep your everyday's data.

![image](https://user-images.githubusercontent.com/44292203/202728681-9c27115a-2d92-40ce-9094-0744b7f13484.png)

- Performing CRUD operations or ticking a checkbox will update the data in the csv file immediately. Also, let's assume that you want to add new data after 15 days of using this application. After the add operation, the value of added day will get 0 while the past days get NaN value. Adding new tasks after a few days means this task was not a part of you before. So, you can only update starting from last day. Of course you can edit values of that column from the csv file.


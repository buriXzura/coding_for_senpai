## SSL Course Project: Plagiarism Checker

**What we’ve implemented so far:**

*   **User registration** under a known organisation using email id
*   **Login** that validates both the user’s password and the corresponding organisation password and returns a JWT that **authenticates** the user
*   **Route guards**: only the /login and /register routes can be accessed by a user who is not logged in. An attempt by such a user to access any other route will redirect them to /login.
*   **Change of password**: re-validates the current password, and then allows the user to update the password, ensuring that the new password is a different one
*   Uploading and downloading files: the user can **upload** files to the server, **download** them, and **delete** them from the server as well
*   (Not integrated) **multiple file upload** by concatenating POST requests and using ng2 file upload Module
*   (Not integrated) Django **Rest API** to upload file

**What technology (languages, frameworks, etc.) we’ve used:**

*   Frontend: Angular CLI: 10.1.7, Node: 12.0
*   User data backend: Express JS (Node 10.1.0)
*   File upload/download backend: Express JS (Node 10.1.0)
*   (Alternate File upload backend): Django 2.7.1

**How the tool is supposed to be run:**


*   Angular CLI, node (including versions 10.1.0 and 12.0) and nvm should be installed on the system
*   Clone this repository into a suitable directory
*   **Navigate into jwt-server and run <code>npm-install</code>
*   Still within jwt-server, run <code>npm start </code> (this starts the backend server)
*   In a new terminal, navigate into jwt-client and if the node version in use is not 12.0, run <code>nvm use 12.0</code>. Then run <code>npm-install</code>
*   Finally, run <code>ng serve -o </code>to start the web interface
*   Navigation in the web interface is self-explanatory as of now

**What is yet to be done:**

*   Along with using the **Bag of Words** strategy, we will create an **“image”** for each file to keep track of the position of words along with their frequency
*   We will be calculating the **cosine similarity** of the source files pairwise after sorting and padding their images
*   We will check for the repetition of code in the file by checking the similarity within an image stacked through it
*   We will be integrating the core logic with the backend using **Django**
*   We will separate out the part of code for the **specific language** case (like the imports in python, headers in c++, etc) to reduce the false positives

The list of sites/tutorials whose code/guidance we have used for our project thus far can be found in the **References** folder.

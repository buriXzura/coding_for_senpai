## SSL Course Project: Plagiarism Checker

**Part 1: The Core Logic**

*  Implemented **Winnowing Algorithm** for similarity detection
*  Implemented **RKR-GST (Running Karp Rabin-Greedy String Tiling) Algorithm** for stub code removal

**Part 2: The Frontend**

*   **User registration** under a known organisation using email id
*   **Login** that validates both the user’s password and the corresponding organisation password and returns a JWT that **authenticates** the user
*   **Route guards**: only the /login and /register routes can be accessed by a user who is not logged in. An attempt by such a user to access any other route will redirect them to /login.
*   **Change of password**: re-validates the current password, and then allows the user to update the password, ensuring that the new password is a different one
*   **Multiple file upload** by concatenating POST requests and using ng2 file upload Module. Uploaded files are saved in the django-server directory
*   **Stub file upload** to upload a stub file
*   **Delete** method available for uploaded code/stub files, and generated result/plot files. 
*   **Download** method available for the generated csv file, surface plot, heatmap, and markers text file
*  **Show Plots** for rendering the generated png and text file
*  **Selective plotting** allowing the user to get the plots for the selected files

**Part 3: Integration**

*   User data backend: Express JS (Node 10.1.0)
*   Login/authentication implemented mainly in the files: <code>jwt-server/index.js</code>, <code>jwt-server/profie.js</code>, <code>jwt-client/src/app/auth.service.ts</code>, <code>jwt-client/src/app/server.service.ts</code>
* Main API endpoints: user registration (POST), user login (POST), user profile retrieval (GET), password validation before changing password (POST), change password (POST)
*   File upload/download backend: Django 2.7.1
*   File upload/download/creation/deletion implemented mainly in the files: <code>django-server/plag_check.py</code>, <code>django-server/plots_create.py</code>, <code>django-server/uploadapp/views.py</code>
* Main API endpoints: Requesting the server as defined in the url.py using the file.service.ts

**What technology (languages, frameworks, etc.) we’ve used:**

*   Frontend: Angular CLI: 10.1.7, Node: 12.0
*   User data backend: Express JS (Node 10.1.0)
*   File upload/download backend: Django 2.7.1
*  JS: express, cors, body-parser, express-bearer-token, bcryptjs, sqlite3, njwt
*  Python: re,os,sys,csv,matplotlib,numpy
*  Django server: autopep8==1.4.3, django-cors-headers==2.5.0, django rest framework==3.9.2, pycodestyle==2.5.0, pytz==2018.9

**How the tool is supposed to be run:**

*   Angular CLI, node (including versions 10.1.0 and 12.0) and nvm should be installed on the system
*   Clone this repository into a suitable directory
*   Run <code>python3 -m venv .env</code> (this creates a virtual environment)
*   Activate the virtual environment by running <code>source .env/bin/activate</code>
*   Navigate into django-server and run <code> pip install -r requirements.txt </code> to install the Python packages
*   Start the file backend server using <code> python manage.py runserver </code>
*   In a new terminal, navigate into jwt-server and run <code>npm-install</code>
*   Still within jwt-server, run <code>npm start </code> (this starts the backend server)
*   In a new terminal, navigate into jwt-client and if the node version in use is not 12.0, run <code>nvm use 12.0</code>. Then run <code>npm-install</code>
*   Finally, run <code>ng serve -o </code>to start the web interface

**Navigation in the web interface:**

*   Upload the files to be compared under the Upload FIles section
*   Go to the main page and upload the stub-file if any
*   Select if files are of type .py
*   Click 'Compute' to compute the result as .csv for the uploaded files
*   Select the files for which you want the plot
*   Click Show Plots to generate SurfacePlot and HeatMap of the similarity measure
*   Markers maps the plot-marks to filenames
*   If you update the uploaded files then follow the same procedure as above


The list of sites/tutorials whose code/guidance we have used for our project thus far can be found in the **References** folder.

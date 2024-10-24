Project Title: Grazioso Salvare Web App

Grazioso Salvare asked us to create a web app that helps them find and navigate animal shelter databases to meet their specific needs. The project has three main layers. First, we use MongoDB to store all the raw data. The middle layer is where we use PyMongo to handle all the CRUD (Create, Read, Update, Delete) operations with MongoDB. Finally, the top layer is built with Plotly-Dash, which provides the dashboard interface for the client.

Motivation

Grazioso Salvare focuses on finding dogs that could be great candidates for search-and-rescue training. These dogs play a crucial role in helping save lives by rescuing animals. The features we developed in this app will let the client and others using this open-source tool easily navigate through large amounts of data. In the end, Grazioso Salvare will be able to sort through the entire database and find candidates for training quickly.

Installation

To set up the project, you'll need access to a Linux terminal and the Mongo shell. Once you’re connected to your local server, you'll use PyMongo, which is a driver module for interacting with MongoDB through Python. PyMongo helps establish a connection between your Python app and MongoDB databases. We used Jupyter Notebook to build a library and a test script for the Python module. Jupyter Plotly Dash is what we used to create the dashboard and all its client-side functionality.

Install Python: [Download Python](https://www.python.org/)
Install PyMongo: [PyMongo on PyPI](https://pypi.org/project/pymongo/)
Install Plotly Dash: [Dash Installation Guide](https://dash.plotly.com/installation)
Jupyter install:Project Jupyter | Installing Jupyter

Jupyter Installation:

To get started with Project Jupyter, follow these steps:

1. Set Up the Environment: Create an environment for the database by uploading a file to load the dataset.  
2. Create User Accounts: Set up authentication by making an admin account and a user account for the database.  
3. Develop the Module: Use Jupyter Notebook to create a Python module and a test script.
4. Test CRUD Functionality: Run the test script to ensure that the CRUD functionality is working for your module.  
5. Build the Dashboard: Use Jupyter Plotly Dash to create and run the web-based dashboard.
6. Launch the App: Once your dashboard has all the required widgets and features, go ahead and run the application:  
7. Dashboard Examples: The dashboard i created has the uses of filtering which type of rescue animal you want and the data file, map, and graph changing in response.
         



Project Challenges:

I ran into a lot of roadblocks while developing the dashboard. At first, the application would run, but some data didn’t show up, and the graphs weren’t displaying correctly. After troubleshooting and fixing several errors the graph wouldn’t pdate when I used the filter tools. My bug that plaqued me for days was I was using the filter name (age_in_weeks) when it is (Age_upon_outcome_in_weeks) and It was a huge relief to know I was stumped on something so dumb for so long.



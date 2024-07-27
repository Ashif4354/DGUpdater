You need to have a mongodb database preferrably on cloud. You can use mongodb atlas for the same, MongoDB have a serverless db cluster which is very cheap (0.1$ / 1M reads). they also have a good free tier. After configuring, get the connection url and save it.

You need to get two connection string from mongo db, one with write access and one with read access. 
the one with write access will be used by the developer to write data to the database and the one with read access will be used by the client to read data from the database. both the connection string should have access to the same cluser and databases.


# Initialization
You have open a terminal and navigate into th directory which you want to initialize for auto updation. Then run the following command:

```bash
dgupdater init
```

This will ask you for the application name, application version, mongodb connection string with read access, mongodb connection string with write access. After providing the required information, it will create a file named 'dgupdaterconf.json' in the current directory. This file will be used to store the configuration of the application.

The mongodbconnection string with write access will be stored in a different place

It will be stored in the following location:
```bash
Windows: C:\Users\<username>\AppData\local\DarkGlance\dgupdater\dgupdaterconf.json
Linux: /home/<username>/.config/DarkGlance/dgupdater/dgupdaterconf.json
Mac: Users/<username>/Library/Application Support/DarkGlance/dgupdater/dgupdaterconf.json
```

Then it will check if the application is already registered in the database or not. If it is not registered, it will register the application in the database. or it will ask to overwrite the application details.

It will also create a file named .dgupdaterignore in the current directory.
this file works just like the .gitignore file. you can add the files and directories which you want to ignore while updating the application.

If you want tp change the mongodb connection string, you can do it by running 'dgupdater init' again and providing the new connection string.


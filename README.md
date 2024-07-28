# DGUPDATER

## Requirements for using dgupdater

*  You need to have a mongodb database preferrably on cloud. You can use mongodb atlas for the same, MongoDB has a serverless db cluster which is very cheap (0.1$ / 1M reads). They also have a good free tier. 
After configuring, get the connection string and save it.

* You need to create two database users in the database, one with only read access and one with only write access.
The user with write access will be used by the developer to write data to the database and the user with read access will be used by the client to read data from the database.

* When initializing the application, it will ask two connection strings, one with write access and one with read access.
 So replace the username and password in the connection string with the username and password of the user with write and read access respectively.

## Initialization
You have open a terminal and navigate into the directory which you want to initialize for auto updation. Then run the following command:

```bash
dgupdater init
```

* This will ask you for the application name, application version, mongodb connection string with read access, mongodb connection string with write access. After providing the required information, it will create a file named 'dgupdaterconf.json' in the current directory. This file will be used to store the configuration of the application.

* The mongodbconnection string with write access will be stored in a different place as follows
```bash
Windows: C:/Users/<username>/AppData/local/DarkGlance/dgupdater/dgupdaterconf.json
Linux: /home/<username>/.config/DarkGlance/dgupdater/dgupdaterconf.json
Mac: Users/<username>/Library/Application Support/DarkGlance/dgupdater/dgupdaterconf.json
```

* Then it will check if the application is already registered in the database or not. If it is not registered, it will register the     application in the database. or it will ask whether to overwrite the application details.

* It will also create a file named .dgupdaterignore in the current directory.
this file works just like the .gitignore file. you can add the files and directories which you want to ignore while updating the application.

* If you want to change the mongodb connection string, you can do it by running 'dgupdater init' again and providing the new connection string.

* After initializing the application, you can continue building the application and when you are ready to update the application, you   can commit the changes.

## Commiting the changes

* After making the changes in the application, you can commit the changes by running the following command:

```bash
dgupdater commit
```

* This will ask for the new version number of the application. 
* After providing the version number, it will ask confirmation to commit the changes. If you confirm, it will commit the changes.

* In this process the following things will happen:

    1. The files and directories mentioned in the .dgupdaterignore file will be ignored.
    2. It will create a directory named 'dgupdater_release' in the root directory
    3. It will create another directory named 'chunks' in the dgupdater_release directory.
    4. It will then create a new dgupdaterconf.json file in the dgupdater_release directory with the updated data.
    5. It will then divide the files into smaller chunks and save them in the chunks directory.
    6. The commiting process is complete.

* Now you can publish the application.

## Publishing the application

* After commiting the changes, you can publish the application by running the following command:

```bash
dgupdater publish
```

* This willl ask confirmation to publish the application. If you confirm, it will publish the application.
* In this process the following things will happen:

    1. It will verify all the release files
    2. It will update the config json object in db with new data
    3. It will delete any previous release files(chunks) from the database if it exists.
    4. It will upload the new release files(chunks) to the database.
    5. It will make the appplication ready to update by updating the 'update_ready' field in the config json object to true.

* The application is now ready to be updated by the client.

## Updating the application (by the client)
### Sorry still working on this part. Will update soon.

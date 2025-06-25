# DGUPDATER
⚠️ This tool is currently supported only on **Windows OS** due to its reliance on native `.exe` files bundled within the package.

## Introduction

* THIS IS A NO/LOW CODE TOOL

DGUPDATER is a command line tool which helps developers to update their python applications automatically. It is a simple tool which can be used to update the application without the need of re-downloading the whole application. It is very useful when you have a large application and you want to update only a small part of the application. 

***Note: This tools is only for releasing new updates by the developer and updating the application to the newer version by the client.***

***This tool is not for creating the application or exporting the application. You have to do that yourself.***

***Sometimes you or the user of your application may need to disable antivirus or windows defender to run the application.***

## Requirements for using dgupdater

*  You need to have a mongodb database preferably on cloud. You can use mongodb atlas for the same, MongoDB has a serverless db cluster which is very cheap (0.1$ / 1M reads). They also have a good free tier (Shared 512Mb). 
After configuring, get the connection string and save it.

* You need to create two database users in the database, one with only read access and one with only write access.
The user with write access will be used by the developer to write data to the database and the user with read access will be used by the client to read data from the database.

* When initializing the application, it will ask two connection strings, one with write access and one with read access.
 So replace the username and password in the connection string with the username and password of the user with write and read access respectively.

## Installation
You can install this package from pypi 

* Using PIP
```
pip install dgupdater
```

* Using Poetry
```
poetry add dgupdater
```

* Using uv 
```
uv add dgupdater
```

* Manually
```
git clone https://github.com/Ashif4354/DGUpdater.git
cd dgupdater
pip install .
```

## Initialization
You have to open a terminal and navigate into the directory which you want to initialize for auto updation. Then run the following command:

```
dgupdater init
```

* This will ask you for the application name, MongoDB connection string with read access, MongoDB connection string with write access. After providing the required information, it will create a file named `dgupdaterconf.json` in the current directory. This file will be used to store the configuration of the application.

* The mongodbconnection string with write access will be stored in a different place as follows
```
Windows: C:/Users/<username>/AppData/local/DarkGlance/dgupdater/dgupdaterconf.json
```

* Then it will check if the application is already registered in the database or not. If it is not registered, it will register the     application in the database. or it will ask whether to overwrite the application details.

* It will also create a file named `.dgupdaterignore` in the current directory.
This file works just like the `.gitignore` file. You can add the files and directories which you want to ignore while updating the application.

* It will also create a file named `dgupdaterupdate.exe` in the current directory. This file is used to update the application. It should not be deleted, and it should be shipped with the application.

* If you want to change the MongoDB connection string, you can do it by running `dgupdater init` again and providing the new connection string.

* After initializing the application, you can continue building it. When you're ready to release a new update, you can commit the changes.

## Committing the changes

* After making the changes in the application, you can commit the changes by running the following command:

```
dgupdater commit
```

* This will ask for the new version number of the application. 
* After providing the version number, it will ask confirmation to commit the changes. If you confirm, it will commit the changes.

* In this process the following things will happen:

    1. The files and directories mentioned in the `.dgupdaterignore` file will be ignored.
    2. It will create a directory named `dgupdater_release` in the root directory
    3. It will create another directory named `chunks` in the `dgupdater_release` directory.
    4. It will then create a new `dgupdaterconf.json` file in the `dgupdater_release` directory with the updated data.
    5. It will then divide the files into smaller chunks and save them in the `chunks` directory.
    6. The committing process is complete.

* Now you can publish the new changes.

## Publishing new changes

* After committing the changes, you can publish the application by running the following command:

```
dgupdater publish
```

* This will ask confirmation to publish the application. If you confirm, it will publish the application.
* In this process the following things will happen:

    1. It will verify all the release files
    2. It will update the config json object in db with new data
    3. It will delete any previous release files(chunks) from the database if it exists.
    4. It will upload the new release files(chunks) to the database.
    5. It will make the application ready to be updated by updating the 'update_ready' field in the config json object to true.

* The application is now ready to be updated by the client.

## check_update()

* You need to call `check_update()` in the entry point of the application before anything starts in your application or wherever you seem fit to call it, to check for the new updates.
```python
from dgupdater import check_update

# Call this function in the entry point of the application
check_update()
```
* In this process the following things will happen:

    1. It will try to locate the `dgupdaterconf.json` file. and the location where the file is found will be considered as the root directory of the application.
    2. Then it will check if a new update is available in the db or not
    3. Then it will ask the user if they want to update the application or not.
    4. If the user confirms, it will start the updation process, and close the current window.
    5. Then it will download all the chunks from the database and merge them to create the new release files.
    6. Then it will replace the old files with the new files.
    7. It will also delete any old version files which are not present in the new version.
    8. The application is now updated to the new version.
    9. The user needs to restart the application to see the changes.

## Shipping Instructions
* You need to ship the `dgupdaterupdate.exe` and `dgupdaterconf.json` file along with the application.


## 🏁 Conclusion
DGUPDATER aims to eliminate the hassle of manual updates for both developers and users. Whether you're maintaining a small utility app or a large-scale tool, this CLI will help you roll out updates faster, smarter, and without breaking a sweat.
No more full downloads or clunky patchwork — just smooth, incremental updates ✨.
So go ahead, build boldly, and let DGUPDATER handle the rest.

Any bugs? Feature ideas?
Contribute or raise issues on GitHub 🛠️

Made with ❤️ by DarkGlance (DG) – Namma pakkam irundhu oru tharamana update experience! 😎

    

    

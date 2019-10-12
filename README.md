
### Create Virtual Environment

In a terminal run the following commands from the root folder of the forked project.

```
virtualenv -p python3.7 venv
```

Once that completes, also run this command from the same folder.

```
source venv/bin/activate
```

Now that you are working in the virtualenv, install the project dependencies with the following command.

```
pip3 install -r requirements.txt
```


### Run Application Locally

To run the application on your machine `flask run`
Check to make sure it works at `http://localhost:5000` in the browser.

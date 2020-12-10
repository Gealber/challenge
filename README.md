# Cuban Engineer challenge. Fizzbuzz
 This is a simple fizzbuzz implementation with python, but with a little of 
customization. Instead of doing the simple and straightforward fizzbuzz algorithm,
I implemented a very simple API using flask. So to be able to run and test the project
you will need a set of requirements.

# About the test

The algorithm itself is not a big deal, very simple indeed, but I do enjoy it for this reasons:
* Forced me to think out of the box, not for the algorithm, but instead on how to present a very simple
task, like this one, in an atractive way. Or at least in a way that show me as a good candidate for the job.
* Helped me to refresh my knowlegde on Flask, given that I've been working lately with Go(at work) 
and C(Just personal stuffs).
* Give me the time to make the tests and check that everything is working properly or at least as I intended.


# Requirements
* flask
* pytest

```
pip install -r requirements.txt
```

# How to installed?

Well you can install this as a module on your local machine, just doing this
```bash
pip install -e .
```
**NOTE**: Take a look at the **.** at the end of the command.

This will install all the necesary requirements for the project to run.

# How to run it?

> In case you are in Ubuntu or any other Linux based OS, you could make use of the script `**run.sh**`.

```bash
./run.sh
```

This simple bash script will run the flask development server on port **5000**. The endpoint that will be
available is called `fizzbuzz`, to see more detail about the documentation of the *API* take a look at the
files `openapi.yaml` or `openapi.json`.

> Windows

```
set FLASK_APP=challenge
set FLASK_ENV=development
flask run
```

> Mac, sorry never seen one but I think with the `run.sh` script you will be ok.
 
# Any doc boy?

Yeap that's covered also, check out `openapi.json` or `openapi.yaml`.

# What about tests?

Well I try to follow the TDD(Test Driven Development) methodology, so I make the tests at first and then
try it to make it pass with my code. The tests on this project are very simple, given that is a simple API.
Anyway to run the tests just do this:

```bash
pytest
```

Just that, we are in Python. Of course to be able to do this we will need to install the module on your machine.
So before running the tests make ssure you run previously, `pip install -e .`.

# What's is left that I could do?

Well I would like to have more time to use:
* **Docker**
* **gRPC**

The idea behind using Docker is to make it more portable and easy to run it and check it on every machine. 
While with gRPC, the idea is to return the result of the query as  stream of data, instead of a list. This way the client
would close the connection when he/she doesn't need more and of course is more fun, gRPC rocks.

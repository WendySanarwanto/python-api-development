# python-api-development
Exercise artefact of Freecodecamp's [Python API Development](https://youtu.be/0sOvCWFmrtA) online course, authored by [Sanjeev Thiyagarajan](https://github.com/Sanjeev-Thiyagarajan). 

## How to run the program in local machine

* Clone this repository through running this `git` command:

  ```bash
  git clone https://github.com/WendySanarwanto/python-api-development.git
  ```

* Change current directory into the cloned local repository:

  ```bash
  cd python-api-development
  ```

* Create a new Python Virtual Environment: 

  ```bash
  python3 -m venv venv1
  ```
  Note that `venv1` command argument define the name of the virtual environment we want to create. 

* Activate the created Python Virtual Environment:

  ```bash
  source ./venv1/bin/activate
  ```

* Install FastApi library and its all dependencies:

  ```bash
  pip install "fastapi[all]"
  ```

* Run the API program:

  ```bash
  uvicorn main:app --reload --port 18000 --workers 4
  ```

* Run `curl` command to test the GET posts API:

  ```bash
  curl http://127.0.0.1/posts
  ```


END--
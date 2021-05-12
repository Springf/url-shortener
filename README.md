## URL shortener
This is a command line utility to show case how to use the core shortener API.
In this utility it implemented a in memory backend store to store the URLs.

## Project Structure
```
+-- core
| git submodule point to the url-shortener-core
+-- store
|   in_memory_store.py #in memory implementation of backend store
+-- tests
|   unit test cases files
main.py #command line utility to call the api
```

## Setup
The code is tested with python 3.8+.

To setup the project, assuming python is installed.

Clone the project and create python venv:
```
git clone https://github.com/Springf/url-shortener.git
cd url-shortener
python -m venv venv
```
Activate the venv:

Windows: `venv\Scripts\activate.bat`

Linux: `source venv/bin/activate`

Install the package: `pip install -r requirements.txt`

## Test

Run unit tests: `pytest tests`

## Run
`python main.py`

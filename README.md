# SERVER SCRIPT ---- PYTHON
## Project Setup

### Requirements
```
- Python 3.10+
- Pip
- Virtualenv
```
### App Setup (Ubuntu System)
- **sudo apt update**
- **sudo apt install python3 python-pip python3-venv**
- **python3 -m venv name**
- **source name/bin/activate**
- **pip install -r requirements.txt**

### Running the Server
- **python3 src/app_server.py**
### Testing the server
- **telnet localhost 8080**

``
Type a string, it returns STRING EXIST if its
present in the file else, it returns STRING NOT FOUND.
You can you "test_string" to get STRING EXIST without randomly guessing
``
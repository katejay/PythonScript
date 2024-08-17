
# A Guide for Python to SQL Integration

Python script for deleting user details from database

I have prepared a Python script that allows us to clear user data from the stage environment.

The script includes all necessary information such as user IDs and product codes.

To use the script:
- Run the Python script.
- Select the user ID for which you want to clear data from the list.
- Choose the product code (it can be DS, MS, or Both).


Before running the script, ensure you have Python set up and the required libraries installed.

Here is step by step guide to setup prerequisite

- Step 1: Download *`Python`* :
```bash
https://www.python.org/downloads/
```
-----
- Step 2: Check if Python is installed by running :
```bash
python3 --version
```
-----
- Step 3: If Python is installed but pip is not, you can install pip using the following methods :
```bash
python3 -m ensurepip --upgrade
```
- Using *`get-pip.py`*: Download the script and run it :
```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```
-----
- Step 4: Verify the *`pip`* installation :
```bash
pip --version
```
-----
- Step 5: Install the required libraries :
```bash
pip install paramiko pymysql
```
-----
- Step 6: Download and run the *`DeleteUserDetails.py`* script :
```bash
python3 DeleteUserDetails.py
```
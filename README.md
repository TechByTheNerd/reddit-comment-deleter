# reddit-comment-deleter

Bulk delete comments for an account on Reddit using the praw library for Python.

## Getting Started

To use this script, consider the follwing steps:

### STEP 1: Clone the Repository

From a folder where you want to store this source code, run:

```bash
git clone git@github.com:TechByTheNerd/reddit-comment-deleter.git
```

then switch into that directory with:

```bash
cd reddit-comment-deleter
```

### STEP 2: Create venv, and restore `pip` packages

Navigate into the `src` folder. Create a new virtual environment, and then restore packages:

```bash
# Change to the src folder.
cd src

# Create a new virtual environment into a hidden .venv folder
python -m venv .venv

# Activate this virtual environment depending on OS:
## On Windows:
#./.venv/scripts/activate.ps1

## On macOS or Linux:
#source ./venv/bin/activate

# Install dependencies for this project.
pip install -r requirements.txt 
```

### STEP 3: Establish `.env` file

This script needs four key-value items to be stored in the `src/.env` file:

- `client_id` - gotten from the directions down below.
- `client_secret` - gotten from the directions down below.
- `reddit_username` - your regular Reddit username.
- `reddit_password` - your regular Reddit password.

You can find documentation [here](https://github.com/reddit-archive/reddit/wiki/OAuth2) but basically to get the `client_id` and `client_secret`, navigate to:

> **https://www.reddit.com/prefs/apps**

And then choose to create an app. In the end, the `src/.env` file should look something like this, but with your information:

```conf
client_id=0hjeEqpaixZmk-eq2rWm
client_secret=heyUuwiz9eanNVewaAwWfxLowA_3Eoi
reddit_username=ExampleUserName
reddit_password=Pazzw0rd123!
```

### STEP 4: Run program

With all of that in place, from the `src` folder, run:

```bash
python ./main.py
```

This will delete up to 100 of your comments, from newest to oldest. Run multiple times to delete more.
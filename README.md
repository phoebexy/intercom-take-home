# Intercom Party List

Intercom wants to invite customers to the office for a giant PARTYYY! This program reads the full list of customers and outputs the names and user ids of matching customers (within 100km) of Intercom's office, sorted by User ID (ascending).

## Quick Start

This project is built using Python 3. To begin, clone the repo using:

```console
$ git clone git@github.com:phoebexy/intercom-take-home.git
```

Install dependencies using pip:

```console
$ pip3 install -r requirements.txt
```

## Running

To run the Party List Creator code, first make sure you have Python 3 installed on your machine. If you need help installing Python 3, check out this [Python 3 Installation & Setup Guide](https://realpython.com/installing-python/).

Then, to run the `app.py`, simply `cd intercompartylist` to go into the right directory. Once you're there run:

```console
$ python3 app.py
```

The program will write the sorted list of people to invite to `output.txt`, enjoy!

## Testing

Tests are run using pytest. Make sure you're back in the root directory. Then run:

```console
$ python -m pytest
```

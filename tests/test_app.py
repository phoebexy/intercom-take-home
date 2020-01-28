import pytest
import os
from intercompartylist.app import IntercomPartyList

# constants

DATAFILE = "resources/testlist.txt"
WRITEFILE = "resources/testwrite.txt"
OFFICE = (37.788802, -122.4025067)
STANFORD = (37.4275, -122.1697)
SALINAS = (36.6777, -121.6555)
SHORTDISTANCE = 30
LONGDISTANCE = 100
NOLIST = [{'latitude': '36.8856167', 'user_id': 2, 'name': 'Ian McArdle', 'longitude': '-118.4240951'},
          {'latitude': '35.92893', 'user_id': 1, 'name': 'Alice Cahill', 'longitude': '-120.27699'}]
YESLIST = [{'latitude': '37.5302756', 'user_id': 5, 'name': 'Nora Dempsey', 'longitude': '-122.4097222'},
           {'latitude': '37.7451022', 'user_id': 4, 'name': 'Ian Kehoe', 'longitude': '-122.238335'}]
ALLLIST = [{'latitude': '36.8856167', 'user_id': 2, 'name': 'Ian McArdle', 'longitude': '-118.4240951'},
           {'latitude': '35.92893', 'user_id': 1, 'name': 'Alice Cahill', 'longitude': '-120.27699'},
           {'latitude': '37.5302756', 'user_id': 5, 'name': 'Nora Dempsey', 'longitude': '-122.4097222'},
           {'latitude': '37.7451022', 'user_id': 4, 'name': 'Ian Kehoe', 'longitude': '-122.238335'}]
TUPLES = [(5, 'Nora Dempsey'), (4, 'Ian Kehoe')]

# fixtures


@pytest.fixture
def intercompartylist():
    return IntercomPartyList()

# Helpers


def verify_answer(answer, expected):
    assert answer == expected

# Test Cases


def test_readFile(rootdir, intercompartylist):
    """test that readFile correctly reads and parses file"""
    test_file = os.path.join(rootdir, DATAFILE)
    result = intercompartylist.readFile(test_file)
    verify_answer(result, NOLIST)


def test_withinDistance_Yes(intercompartylist):
    """test that withinDistance correctly filters within distance customers"""
    stanfordInvite = intercompartylist.withinDistance(STANFORD, OFFICE, LONGDISTANCE)
    verify_answer(stanfordInvite, True)


def test_withinDistance_No(intercompartylist):
    """test that withinDistance correctly filters out customers who are too far away"""
    stanfordNoInvite = intercompartylist.withinDistance(STANFORD, OFFICE, SHORTDISTANCE)
    salinasNoInvite = intercompartylist.withinDistance(SALINAS, OFFICE, LONGDISTANCE)
    verify_answer(stanfordNoInvite, False)
    verify_answer(salinasNoInvite, False)


def test_filterCustomers_Yes(intercompartylist):
    """test that filterCustomers correctly compiles filtered list of customers"""
    allCustomers = intercompartylist.filterCustomers(ALLLIST, OFFICE, LONGDISTANCE)
    verify_answer(allCustomers, [(5, 'Nora Dempsey'), (4, 'Ian Kehoe')])


def test_filterCustomers_No(intercompartylist):
    """test that filterCustomers correctly filters out all customers too far away"""
    noCustomers = intercompartylist.filterCustomers(NOLIST, OFFICE, LONGDISTANCE)
    verify_answer(noCustomers, [])


def test_sortFilteredCustomers(intercompartylist):
    """test that sortFilteredCustomers correctly sorts customers by id"""
    sortedTuples = intercompartylist.sortFilteredCustomers(TUPLES)
    verify_answer(sortedTuples, [(4, 'Ian Kehoe'), (5, 'Nora Dempsey')])


def test_writeOutput(rootdir, intercompartylist):
    """test that writeOutput correctly clears and writes new output text file"""
    writeFile = os.path.join(rootdir, WRITEFILE)
    with open(writeFile, 'w') as f:
        f.truncate(0)
        f.write("gibberish\n")
    intercompartylist.writeOutput(writeFile, TUPLES)
    f = open(writeFile, 'r')
    verify_answer(f.read(), '5 Nora Dempsey\n4 Ian Kehoe\n')

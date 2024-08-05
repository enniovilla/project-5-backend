# connectify. API

This is the testing document for the backend of my connectify. project. If you want to see the README, click [here](README.md).

# Testing

## Content

* [Testing](<#testing>)
    * [Code Validation](<#code-validation>)
    * [Manual Testing](<#manual-testing>)

## Code Validation 

The code has been validated by the [Code Institute's PEP8 validator](https://pep8ci.herokuapp.com/).

### Connectify_api

| File            | Status |
|-----------------|--------|
| permissions.py  | ✅     |
| serializers.py  | ✅     |
| views.py        | ✅     |
| models.py       | ✅     |
| urls.py         | ✅     |


### Attendances app

| File            | Status |
|-----------------|--------|
| models.py       | ✅     |
| serializers.py  | ✅     |
| urls.py         | ✅     |
| views.py        | ✅     |


### Comments app

| File            | Status |
|-----------------|--------|
| models.py       | ✅     |
| serializers.py  | ✅     |
| urls.py         | ✅     |
| views.py        | ✅     |

### Events app

| File            | Status |
|-----------------|--------|
| models.py       | ✅     |
| serializers.py  | ✅     |
| urls.py         | ✅     |
| views.py        | ✅     |

### Favorites app

| File            | Status |
|-----------------|--------|
| models.py       | ✅     |
| serializers.py  | ✅     |
| urls.py         | ✅     |
| views.py        | ✅     |

### Followers app

| File            | Status |
|-----------------|--------|
| models.py       | ✅     |
| serializers.py  | ✅     |
| urls.py         | ✅     |
| views.py        | ✅     |

### Profiles app

| File            | Status |
|-----------------|--------|
| models.py       | ✅     |
| serializers.py  | ✅     |
| urls.py         | ✅     |
| views.py        | ✅     |

[Back to top](<#content>)

## Manual Testing

Some manual tests have been carried out.

| Test            | Status |
|-----------------|--------|
Can retrieve followers using valid ID | ✅
Logged in user can mark as attending | ✅
Can list events | ✅
Can delete follow from my own profile | ✅
Logged out user can't create event | ✅
Can update own event | ✅
Can update own profile | ✅
Can't update someone else's profile | ✅
Can list comments | ✅
Logged in user can favorite | ✅
Can retrieve favorites using valid ID | ✅
Can't retrieve event using invalid ID | ✅
Can delete own favorites | ✅
Can't retrieve comment using invalid ID | ✅
Can retrieve comment using valid ID | ✅
Can list followers | ✅
Can't delete someone else's favorites | ✅
Can't favorite the same event twice | ✅
Can't mark attending the same event twice | ✅
Can't retrieve profile using invalid ID | ✅
Can't update someone else's comment | ✅
Can retrieve event using valid ID | ✅
Can't delete someone else's event | ✅
Can update own comment | ✅
Can't retrieve followers using invalid ID | ✅
Can't delete someone else's attendance | ✅
Can delete own attendance | ✅
Can delete own comment | ✅
Logged in user can create event | ✅
Can retrieve profile using valid ID | ✅
Can retrieve attendances using valid ID | ✅
Can list favorites | ✅
Logged out user can't favorite | ✅
Can't delete someone else's profile | ✅
Logged out user can't follow | ✅
Can list profiles | ✅
Logged in user can follow | ✅
Logged in user can create comment | ✅
Can't delete someone else's comment | ✅
Can't retrieve attendances using invalid ID | ✅
Can't update someone else's event | ✅
Logged out user can't mark as attending | ✅
Can list attendances | ✅
Can list events | ✅

[Back to top](<#content>)

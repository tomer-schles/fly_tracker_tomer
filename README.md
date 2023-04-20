# fly_tracker
An open source project that helps you get the best flight deals!

![license](https://img.shields.io/github/license/Ritik3111/fly_tracker)
![issues](https://img.shields.io/github/issues/Ritik3111/fly_tracker)

## Code Coverage

[![codecov](https://codecov.io/gh/Ritik3111/fly_tracker/branch/main/graph/badge.svg)](https://codecov.io/gh/Ritik3111/fly_tracker)

![status](https://img.shields.io/github/actions/workflow/status/Ritik3111/fly_tracker/setup.yml)

## Overview

The Fly Tracker library lets you monitor the flight prices for any route.
The user has the option to set up notifications for the tracked route which can help him book tickets when he/she wants to.

## Table of Contents

- [Installation](#Installation)
- [Usage](#Usage) 
- [Example] (#Example)

## Installation 

To install the library: 

`pip install fly_tracker`

## Usage

The library takes the following arguments:

| Argument | Name | Type | Description
| -------- | -------- | -------- | -------- |
| src | Source | string | Source City |
| dst | Destination | string |Destination City|
| price | Price | int |The threshold price that you want to set|
| date | Date | string | The date you want to fly on |

Run the following command:

python fly_tracker --src src-city --dst dest-city --price price --date date

Replace src-city, dest-city, price, and date with your desired values. This will start tracking the flight prices for the specified route.

## Example

`python fly_tracker --src "New York" --dst "Boston" --price 100 --date "12 May"`

This creates a 'Results_TimeStamp.csv' file with all airfares between New York and Boston on 12th May below 100$.

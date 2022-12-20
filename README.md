## Introduction

This project is a python command-line application to find the air Distance between all pairs of places.


## Prerequisites

* [docker](https://www.docker.com/)

## To Run the Application

    docker-compose build
    docker-compose run erebor <command line arguments>

## Sample Execution & Output

If run without command line arguments, using

```
docker-compose run erebor
```

The Application will calculate distances between places that are placed in .data/places.csv

Or if run using

```
docker-compose run erebor -n 10
```
The Application will calculate distances between 10 random places 

output *simliar* to

```
Someplace         Otherplace        152.6 km
Someplace         Otherplace        152.6 km
Someplace         Otherplace        152.6 km
Someplace         Otherplace        152.6 km

Average distance: 321.8 km. Closest pair: Thisplace – Thatplace 312.5 km.
```

---

## Local Setup
    $ git clone git@github.com:Msardari/distances.git
    $ cd distances
    $ pyvenv venv
    $ . venv/bin/activate
    $ pip install -r requirements.txt
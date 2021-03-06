# flight-optimizer

**Command Line Interface (CLI)** that searches for the cheapest airplane flights per kilometer.

### CI / CD

Github actions were used as CI / CD for this project. 

Package was published to [PYPI](https://pypi.org/project/flight-optimizer/).

All build and PYPI deployment statuses of the package can be found [on project's Github Actions](https://github.com/erikduisheev/flight-optimizer/actions)

### Installation:

```Shell
pip install flight-optimizer
```

requires python >= 3.6

### Usage:

```Shell
$ flight_optimizer --from paris --to "new york" --to londo --to moscow --all-destinations --explain-result
```

### Output:

```Shell
From Paris, Paris Orly:
To New York, John F. Kennedy International              $381 / 5834 km       = $0.07 per km
To London, Heathrow                                     $340 / 367 km        = $0.93 per km
To Moscow, Domodedovo International                     currently there is no any flights.

Explanation and suggestions:
City "londo" was misspelled. It was assumed as "London" in United Kingdom.
Maybe you meant next options: "East London" in South Africa, "Londolozi Private Game Reserve" in South Africa, "London" in Canada, "New London" in United States
```

### Options:
```Shell
  -f, --from TEXT         Departure City  [required]

  -t, --to TEXT           Destination City (can be multiple)  [required]

  -a, --all-destinations  Shows flights for every destination. 
                          (default - shows only the best destination)

  -e, --explain-result    If entered cities were misspelled, then it explains
                          what cities were searched and suggests correct city
                          name options
```

### Credits
Developed by Erik Duisheev.

Inspired by [B12 team](https://www.b12.io/about).

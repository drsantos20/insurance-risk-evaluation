# Insurance Risk Evaluation

This project is based on a health insurance score risk 

## ✅&nbsp; Prerequisites

```
docker
```

## 📦&nbsp; Run

```
cd insurance-risk-evaluation
docker-compose up -d --build
```

or

```
make start
```

## 📋&nbsp; Testing

```
docker-compose exec web pytest .
````

or

```
make test
```

## 📪&nbsp; API Resources

`Swagger` Documentation is located at [http://127.0.0.1:8002/docs](http://127.0.0.1:8002/docs) 


## ✒️&nbsp; Insurance

This endpoint is responsible for receiving an input containing the user information, like:

```JSON
{
  "age": 35,
  "dependents": 2,
  "house": {"ownership_status": "owned"},
  "income": 0,
  "marital_status": "married",
  "risk_questions": [0, 1, 0],
  "vehicle": {"year": 2018}
}
```

And responding with risk scores for each insurance line as seen below:

```JSON
{
    "auto": "regular",
    "disability": "ineligible",
    "home": "economic",
    "life": "regular"
}
```

## 📕&nbsp; Main Technical Decision

The Rules Engine was built based on the behavioral pattern Chain of Responsibility where every rule is an object derived from the `BaseRule` class that can handle requests.

[chain-of-responsibility](https://refactoring.guru/design-patterns/chain-of-responsibility)

A `Rule` object has an `apply_rule(self, user_profile, user_risk)` method that handles the request by applying rules.   

In order to create a new rule simply create a new class extending `BaseRule` and add it to the chain. 

In this project, the chain is initialized in `services.py`, the pipe operator (|) is overloaded given that chain can be written as the following:

```python
import AgeOverSixty, AgeUnderThirty, AgeBetweenThirtyAndForty

rules = (AgeOverSixty()
         | AgeUnderThirty
         | AgeBetweenThirtyAndForty
        )
```

And rules are executed for a `UserProfileDTO` object, containing all the user information received. Using a `UserProfileRisk` object to store the risks for insurance categories. As the following:

```python
base_risk = UserProfileRisk(user_profile)
risk = rules.apply_rule(user_profile, base_risk)
```

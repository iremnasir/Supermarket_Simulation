# Supermarket_Simulation
Simulating the customer behavior in a supermarket with Markov Chain Modeling, with an added parameter of existent Covid19 threat.

- The program uses two classes named as SupermarketCustomer and Supermarket.
- Several insights are driven from the data with day names in data folder_
    - Transition probability matrix (Covid/non-Covid) that underlies the choice of aisles customers visit first and in following periods
    - Number of customers entering per minute in a day
    - How much time do people spend in specific aisles

**Qualitatively there is no discrepancy between real data and simulation patterns**


## Keywords
  - Monte-Carlo simulation
  - Markov Chain modeling
  - NumPy

## Usage
    python main.py

- Within main.py user can switch ```corona``` parameter on/off as well as the ```number of days``` to be simulated

## Improvements to be made

- ~~Add reduced traffic within supermarket to Covid19 attribute~~
- Add docstrings and comments throughout the classes.
- Add visualization script
- Find ways to minimize the error introduced by randomly choosing the number of people enter per min (i.e. upper/lower bounds can be tweaked)

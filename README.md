# Premisse
> The director of a prison offers 100 death row prisoners, who are numbered from 1 to 100, a last chance. A room contains a cupboard with 100 drawers. The director randomly puts one prisoner's number in each closed drawer. The prisoners enter the room, one after another. Each prisoner may open and look into 50 drawers in any order. The drawers are closed again afterwards. If, during this search, every prisoner finds their number in one of the drawers, all prisoners are pardoned. If even one prisoner does not find their number, all prisoners die. Before the first prisoner enters the room, the prisoners may discuss strategy — but may not communicate once the first prisoner enters to look in the drawers. What is the prisoners' best strategy?

---

# How can you solve this?
There is an infinite ways to solve the problem, but I approached 2: *Random picking* and *Cycle strategy*

## Random picking

In the random strategy, each prisoner independently chooses 50 boxes out of the 100 available, without any predetermined order or coordination. This means that each prisoner selects boxes purely by chance, hoping to find their own number among the 50 they open. While this gives each prisoner a 50% chance of success individually, the overall success condition requires that every one of the 100 prisoners finds their number. Consequently, the probability that all prisoners succeed simultaneously is 0.5^100 ≈ 0.0000000000000000000000000000008%, an astronomically small number. This illustrates that, despite the seemingly fair odds for a single prisoner, the random approach is highly suboptimal when considering the group's combined success.

## Cycle strategy

The cycle strategy leverages the natural structure of permutations. Instead of each prisoner randomly choosing boxes, every prisoner begins by opening the box corresponding to their own number. The number found inside that box indicates which box to open next, creating a sequence or cycle. As the prisoner follows this chain, they continue opening boxes based on the number discovered in the previous box. If the cycle that the prisoner is following contains 50 or fewer boxes, they will eventually encounter their own number within the allowed limit. The overall success of the group depends on the condition that no cycle in the permutation exceeds 50 elements. Surprisingly, this structured approach raises the probability of all prisoners finding their number to about 31%, a significant improvement over the nearly zero chance offered by a purely random selection strategy.

---

# Code
The code approach each strategy, printing the paths, the number of prisoners that failed in that strategy and how many jumps was necessary. After, plots a graph for each approach so you can compare, make a visible comparison and highlighting the diference.

---

# How to run
**I recommend using a venv for installing the dependencies**

For this code to run, it will be necessary to download python(at least 3.12), matplotlib and networkx, you can do this with the following commands:
``` bash
pip install matplotlib
```
``` bash
pip install networkx
```

After run in the terminal:

- for linux and macOS:
```bash
python3 App.py
```
- for Windows:
```cmd
python App.py
```

---

# This is only a fun project, feel free to fork and modify

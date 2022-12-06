# [AdventOfCode 2022](https://adventofcode.com/2022)
AdventOfCode is a yearly event for which a new, two-part, coding challenge is released each day of December until the 25th.

This year I will attempt the challenge in Python and SPARK Ada. In python I will
try to produce an efficient and readable solution, but I will not spend too much time on
this. In Ada I will attempt to produce a full SPARK implementation, with provable type and
memory safety. As an extension I may
try to prove some functional properties of my SPARK implementation.

In the ReadMe.md file for each day you will find the problems themselves,
along with some notes on my solutions.

## Levels of SPARK Use
I will measure the level of SPARK usage in my solutions on the [scale](https://docs.adacore.com/spark2014-docs/html/ug/en/usage_scenarios.html#levels-of-spark-use) defined by AdaCore.
This is as follows:

* **Stone level** - valid SPARK.
* **Bronze level** - initialization and correct data flow.
* **Silver level** - absence of run-time errors (AoRTE).
* **Gold level** - proof of key integrity properties.
* **Platinum level** - full functional proof of requirements.

Here is the current status of my solutions:

| Day | Star | Solved in Python | Solved in Ada | Level of SPARK use |
| --- | ---- | ---------------- | ------------- | ------------------ |
| 01 | 01 | Yes | Yes | Gold |
| 01 | 02 | Yes | Yes | Silver |
| 02 | 01 | Yes | Yes | Silver |
| 02 | 02 | Yes | Yes | Silver |
| 03 | 01 | Yes | No | N/A |
| 03 | 02 | Yes | No | N/A |
| 04 | 01 | Yes | No | N/A |
| 04 | 02 | Yes | No | N/A |
| 05 | 01 | Yes | No | N/A |
| 05 | 02 | Yes | No | N/A |
| 06 | 01 | Yes | No | N/A |
| 06 | 02 | Yes | No | N/A |

Some python solutions will import modules from my aoc_tools package, you will need to install this using:
```pip install aoc-tools-dannyboywoop```

# Technology Choice Simulation
## What does the code do?
The code models how three technologies spread in a social network using an agent-based model organized in two
classes: an Agent class and a Simulation class. The network is created using a Barabási-Albert graph. Technologies
have equal numbers of early adopters (2), and agents have a probability to reconsider their choice later. Agents that
start without a technology can adopt one based on their neighbors’ choices. The simulation begins by assigning two
random agents as early adopters for each technology. Over 10,000 iterations, agents either copy a neighbor’s
technology or switch based on a set probability. The program tracks adoption patterns of the three technologies over
time and creates a plot that visualizes how technologies spread.

## How to use the code?
Make sure the libraries numpy, networkx and matplotlib are installed. This code does
not require any additional file to run. Simply execute the script in Python. It will
create a network of 1,000 agents using a Barabási-Albert graph, assign 3 different
technologies to agents, and simulate 10,000 iterations of technology adoption
with a default switching probability of 90%. After running the simulation, it will
generate a plot showing how the number of adopters for each technology changes over
time. The plot will display on the screen and be saved as a PDF file in the working
directory.

## Simulations with different switching probabilities (90% and 10%)
Simulations with a switching probability of 10% almost always show more regular patterns over time, with fewer
fluctuations (Figure 1.). In these cases, one technology consistently becomes dominant, maintaining a significantly
higher number of adopters, while the other technologies settle at lower levels of adoption.
In contrast, simulations with a switching probability of 90% often exhibit less regular trends with more pronounced
fluctuations (Figure 2.). The adoption levels frequently overlap and surpass each other, creating a more dynamic
competition where it is possible that no single technology consistently dominates over time. This highlights how
switching probability affects both the stability and variability of technology adoption.

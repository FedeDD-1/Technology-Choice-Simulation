# -*- coding: utf-8 -*-
"""
@author: Federico Durante
"""

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

""" Agent class """
class Agent():
    def __init__(self, id_number, S):
        """
        Agent constructor method.

        Parameters
        ----------
        id_number : int
            Agent's unique ID number.
        S : Simulation object
            The simulation the agent is part of.

        Returns
        -------
        None.
        """
        self.switching_probability = 0.9
        self.id = id_number
        self.S = S
        self.technology = None

    def choose_new_technology(self):
        """
        Method for choosing a new technology for the Agent.

        Returns
        -------
        None.
        """
        """ Obtain randomized list of neighbor agents """
        neighbors = list(nx.neighbors(self.S.G, self.id))
        np.random.shuffle(neighbors)

        """ Clear current technology choice """
        self.technology = None

        """ Copy choice of one of the neighbors (first one with a technology
        in the randomized neighbor list) """
        i = 0
        while (self.technology is None) and (i < len(neighbors)):
            neighbor_technology = self.S.agent_list[neighbors[i]].get_technology()
            if neighbor_technology is not None:
                self.technology = neighbor_technology
            i += 1

    def iterate(self):
        """
        Iterate method for the Agent. Should be run in every time period of the
        simulation. Governs the initial choice and later switching of the
        Agent's technology.

        Returns
        -------
        None.
        """
        if self.technology is None:
            self.choose_new_technology()
        elif np.random.random() < self.switching_probability:
            self.choose_new_technology()

    def set_initial_technology(self, technology):
        """
        Setter method for technology. Used for seeding technologies at the
        start of the simulation

        Parameters
        ----------
        technology : int
            Technology identifier.

        Returns
        -------
        None.
        """
        self.technology = technology

    def get_technology(self):
        """
        Getter method for the Agent's technology.

        Returns
        -------
        int
            Technology identifier.
        """
        return self.technology


""" Simulation class """
class Simulation():
    def __init__(self):
        """
        Simulation constructor method.

        Returns
        -------
        None.
        """
        self.prepare_agent_network()
        self.initialize_technologies()

    def initialize_technologies(self, number_of_technologies=3):
        """
        Method for initializing technologies in the simulation.
        Technologies are identified by numeric identifiers: 0, 1, ...
        Each technology has two random early adopters.

        Parameters
        ----------
        number_of_technologies : int, optional
            Number of technologies available in the simulation.
            The default is 3.

        Returns
        -------
        None.
        """
        """ Prepare list of technologies """
        self.technologies = [i for i in range(number_of_technologies)]

        """ Choose early adopters randomly """
        starters = np.random.choice(self.agent_list, size=2 * len(self.technologies))

        """ Seed starting technologies """
        for j, tech in enumerate(self.technologies):
            for i in range(2):
                starter = starters[j * 2 + i]
                starter.set_initial_technology(tech)

    def prepare_agent_network(self, n_agents=1000):
        """
        Method for preparing the list of agents and network of agents.

        Parameters
        ----------
        n_agents : int, optional
            Number of agents in the simulation. The default is 1000.

        Returns
        -------
        None.
        """
        """ Record the number of agents at the class level """
        self.n_agents = n_agents

        """ Prepare the network: Barabasi-Albert graph with 40 connections per
        new agent """
        self.G = nx.barabasi_albert_graph(n=self.n_agents, m=40)

        """ Prepare agent list as class level variable """
        self.agent_list = []

        """ Create agents """
        for i in range(self.G.number_of_nodes()):
            """ Create one agent with arguments:
            i : ID number
            self : reference to the Simulation object
            """
            A = Agent(i, self)
            """ Record agent object into list of agent """
            self.agent_list.append(A)
            """ Place agent on the network in node i """
            self.G.nodes[i]["agent"] = A

    def run(self, iterations=10000):
        """
        Method to run the simulation for a given number of iterations.

        Parameters
        ----------
        iterations : int, optional
            Number of iterations to run the simulation. Default value is 10,000.

        Returns
        -------
        None.
        """
        
        """ Initialize a dictionary to track technology adoption data"""
        self.adoption_data = {tech: [] for tech in self.technologies}

        """ Iterate over the total number of iterations """      
        for _ in range(iterations):
            """ Select a random agent from the list of agents """
            agent = np.random.choice(self.agent_list)
            """ Execute the agent's iteration method """
            agent.iterate()
            """ Loop through each available technology. """
            for i in self.technologies:
                """ Count how many agents are currently using technology i """
                count = sum(1 for a in self.agent_list if a.get_technology() == i)
                """ Append the count of adopters to the adoption data for i """
                self.adoption_data[i].append(count)
                


    def plot(self):
        """
        Method to plot the time development of technology adoption.
        Returns
        -------
        None.
        """
        
        """ Plotting technology adoption over time for each technology """
        for tech in self.technologies:
            plt.plot(self.adoption_data[tech], label=f"Technology {tech + 1}")
        plt.xlabel("Iterations")
        plt.ylabel("Number of Adopters")
        plt.title("Technology Adoption Over Time")
        plt.legend()
        plt.grid(True)
        plt.savefig("Assigment-05-Durante.pdf")
        plt.show()
        
""" Main entry point """
if __name__ == "__main__":
    
    """ Create simulation object """
    s = Simulation()
    
    """ Run simulation """
    s.run()
    
    """ Show results """
    s.plot()
    
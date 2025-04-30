from termcolor import colored
import random
import numpy
# -------------------------VARIABLES-------------------------
tribes = {
    "red":
    {
        "size":10,
        "initial_opinion":.5,
        "greed":0    
    },
    "blue":
    {
        "size":10,
        "initial_opinion":.9,
        "greed":0.5
    },
} 

trials = 1000


# -------------------------FUNCTIONS-------------------------
class Agent:
    def __init__(self,id,tribe):
        self.id = id
        self.tribe = tribe
        self.opinion = {} #  dictionary of opinions of other agents - value between 0,1, as average of past interactions
        self.value = 0
        self.greed = tribes[tribe]["greed"]
        self.past_interactions = []

    def get_opinion_of(self,tribe):
        if tribe in self.opinion:
            return self.opinion[tribe]
        return tribes[self.tribe]["initial_opinion"]

    def print_opinions(self):
        print(colored("Agent"+self.tribe+" "+str(self.id),self.tribe),end="")
        print(self.opinion)
    
    def update_opinion(self,value,tribe):
        self.opinion[tribe] = (self.get_opinion_of(tribe)+value)/2




class Agents():
    def __init__(self,tribes):
        self.agents=[]
        id=0
        for tribe in tribes:
            for _ in range(tribes[tribe]["size"]):
                self.agents.append(Agent(id,tribe))
                id+=1

    def print_agents_opinions(self):
        for agent in self.agents:
            agent.print_opinions()

    def print_tribes_average_opinions(self):
        for tribe_object in tribes:
            print(colored("Tribe "+tribe_object+"\t average opinion",tribe_object))
            for tribe_subject in tribes:
                print("opinion of tribe "+tribe_subject+":\t ",end="")
                print(round(numpy.mean([agent.opinion.get(tribe_subject,0) for agent in self.agents if agent.tribe == tribe_object]),3))
            print("")

        


def random_prisioners(agent1:Agent,agent2:Agent):
    chance = random.random()
    if (chance<agent1.get_opinion_of(agent2.tribe)):
        agent1_action = 1 #steal
    else: 
        agent1_action = 0 #share
    if (chance<agent2.get_opinion_of(agent1.tribe)):
        agent2_action = 1 #steal
    else: 
        agent2_action = 0 #share

    agent1.update_opinion(agent2_action,agent2.tribe)
    agent2.update_opinion(agent1_action,agent1.tribe)



# -------------------------MAIN-------------------------
def main():
    #initialise agents
    Group = Agents(tribes)
    Group.print_agents_opinions()
    
    for _ in range(trials):
        random_agents = random.sample(Group.agents,2)
        random_prisioners(random_agents[0],random_agents[1])
        Group.print_agents_opinions()
    print("\n\n")
    print(colored("FINAL:","green"))
    Group.print_tribes_average_opinions()
    
if __name__ == "__main__":
    main()

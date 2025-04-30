# Morality-Modeling
the point of this model is to measure bias in systems of tribal games, how bias can change from personal experience, and how initial conditions such as the relative size of tribes can contribute towards systematic bias.

## Overview
A set of agents is partitioned into 'tribes' whose relative size, and initial opinion are initialised at the start of model.py. Each agent of each tribe has a unqiue *opinion* dictionary of other tribes which is updated at each interaction.

Agents are chosen at random in pairs to play a game of an improvised **random prisioners dilemma**. In this each player reflects the believed play of their opponent, that is if they think they will steal, they will also steal, but if they think they will share, they will also share. The belief of their opponent action is based of a random dice roll against their opinion of the tribe of their opponent.

## Variables
- initial opinion


Future properties
- add value to keep track of tribes being rewarded for 'wining', similarly a greed function to create a preference for the random
- statistcs/birfurication tracker
- bootlegger
- other "games"
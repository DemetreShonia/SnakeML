import torch
import random
import numpy as np
from collections import deque
from game import SnakeGameAI, Direction, Point

MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001 # learn rate
class Agent:
    def __init__(self):
        self.n_games = 0
        self.epsilon = 0 # randomness
        self.gamma = 0 #discount rate
        # this will call pop left for us if we exceed memory
        self.memory = deque(maxlen = MAX_MEMORY) #pop_left
        # TODO: model, trainer

    def get_state(self, game):
        pass
    def remember(self, state, action, reward, next_state, done):
        pass
    def train_long_memory(self):
        pass
    def train_short_memory(self, state, action, reward, next_state, done):
        pass    
    def get_action(self, state):
        pass
    def train():
        plot_scores = []
        plot_mean_scores = []
        total_score = 0
        record = 0
        agent = Agent()
        game = SnakeGameAI()
        while True:
            # get old state of current state
            state_old = agent.get_state(game)

            #get move
            final_move = agent.get_action(state_old)
            #perform move and get new state
            reward, done, score = game.play_step(final_move)
            state_new = agent.get_state(game)

            # train short memory
            agent.train_short_memory(state_old,final_move,reward, state_new, done)

            #remember
            agent.remember(state_old, final_move,reward, state_new, done)

            if done:
                #train long memory # experience replay??... it plays on previous moves now, plot result
                game.reset()
                agent.n_games += 1
                agent.train_long_memory()

                if score > record:
                    record = score
                    # agent.model.save()

    if __name__ == '__main__':
        train()
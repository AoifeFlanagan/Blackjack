# Blackjack
Repository for a game of Blackjack, created with python.

## Table of Contents
* [Introduction](https://github.com/AoifeFlanagan/Blackjack#Introduction)
* [Features](https://github.com/AoifeFlanagan/Blackjack#Features)
* [Modules](https://github.com/AoifeFlanagan/Blackjack#Modules)
* [Interactive Development Environment (IDE)](https://github.com/AoifeFlanagan/Blackjack#Interactive-Development-Environment-(IDE))

## Introduction
The objective of this project was to create an interactive game of Blackjack involving one player and a computer dealer. 

## Features
* A user welcome message.
* Easy to follow, intuitive play. 
* Automatic dealing of the cards, the player and dealer are dealt two cards each from a randomly shuffled deck. 
* The player starts with a default value of 100 chips, shown at the beginning of the game.
* The player is asked how much they would like to bet. If the input is not between 1 and their chips total, the player is prompted to try again with infinite tries until they enter acceptable input.
* When the player specifies the amount of chips they wish to bet, the player is shown how many chips they have bet and how many they have remaining. 
* when deciding to hit or stand, the player is shown the cards in their hand, their total value and one card from the dealer's hand and it's value.
* If the player continues to hit, they will do so until they automatically win with a hand value of 21 or go Bust. 
* When the player decides to no longer hit, the dealer will hit until they reach at least 17. The end game scenario will then be automatically detected and made known to the player. 
* At the end of the game the player will be shown what occured during the game to result in the win/ lose/ tie scenario. For example, "The dealer scored 21 and won!", "The dealer went bust, player wins the game!" and so on. 
* The player will also be shown depending on the game outcome how many chips they won, lost or neither won or lost.
* The player will be asked if they wish to continue playing, if they have more than zero chips they will continue playing using their chips total. Otherwise, their chips will be reset to the default value. If the player chooses not to continue, a thank you for playing message is shown and the game stops.

## Modules
* Built-in, Random module.
* Built-in, clear_output() functionality from IPython.display.

## Interactive Development Environment (IDE)

### **Jupyter notebook**
The notebook server was run on Python version 3.7.6

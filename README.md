Mancala - Isholo
======

A version of Mancala taught by a man in Jollyboys Backpackers at the end of 2014.

The stonealone files should run on their own without any other files. Not exactly in the full OOP philosophy though, so there will probably only be one..

According to an extremely verbose storyteller, Mancala (or Isholo as he called it) is an ancient game played with stones, and has had great significance in shaping the past of Zambia, in that it has not had a single civil war. While the truth of this can be debated, the existence of the game cannot. 

At this point there are three variations that I will try to construct here. As all three are variations on each other, they have common rules. 

The Board
The board or table consists of four rows of eight holes. Two rows are allocated to each player. In each of the holes two stones are placed. The innermost row, and thus the row that is positioned closest to the opposing player, will be thus referred to in the coordinate system as 'a'. The outer row will be therefore referred to as 'b'. When considering the board for the opposing player, one's board undergoes something resembling rotational symmetry, such that the ordering of rows is:
b
a
a
b
Irrespective of player perspective. Each of the holes is referred to with a number from 1-8, in accordance with the eight holes in each row. Thus for any given player, their board will be referred to as:
a1 a2 a3 a4 a5 a6 a7 a8
b1 b2 b3 b4 b5 b6 b7 b8
In respect to the aforementioned rotational symmetry, the opponent's corresponding positions to the player will appear as
b8 b7 b6 b5 b4 b3 b2 b1
a8 a7 a6 a5 a4 a3 a2 a1
Giving a comprehensive board of appearance:
b8 b7 b6 b5 b4 b3 b2 b1
a8 a7 a6 a5 a4 a3 a2 a1
---------------
a1 a2 a3 a4 a5 a6 a7 a8
b1 b2 b3 b4 b5 b6 b7 b8

Sowing
The second concept common to all three variations is the concept of sowing. Sowing occurs once on each player's turn. 

Sowing utilizes a directional system best explained with "anticlockwise". When the words "one hole forwards" or a similar variation is used, it refers to one hole anticlockwise. Thus in the a row, a8 moves to a7, a3 moves to a2, and a1 moves to b1. Following this, b1 would move to b2, b5 would move to b6, and b8 would move to a8.  

To perform sowing, a hole must be chosen (in accordance to the coordinate system). All stones in this hole are removed and placed in a hand. This hand moves to the next hole forwards, drops one stone, moves forwards, drops one stone, and so on until the hand runs out of stones. Here sowing has one of two outcomes. 

a. If the final stone placed by the hand was in an empty hole, then the sowing process ends. An alternate explaination would be that if a hole had n stones, and the nth hole away contains no stones, the sowing stops. 

b. However, if the final hole had previous stones, then they are all picked up and resowed. It is as if, after placing the final stone, the game forced you to take an extra turn on the same coordinate that you finished on. This process continues indefinitely, until the 'a' case happens.

These two processes are all that is common between the three variations. Let us move on...

Game 1
This game is the most basic of the three. Every turn, each player sows a single hole. However, if the sowing process stops in the 'a' row, then a list of conditional checks happen. If the opponent has > 0 stones in their 'a' hole directly adjacent to the final sowed hole, then all stones in that column are captured and removed from the game.
The list of directly adjacent column coordinates:

	1. 8
	2. 7
	3. 6
	4. 5
	5. 4
	6. 3
	7. 2
	8. 1

Stones are captured if and only if the opponent has stones in their 'a' row. Therefore, if the opponent has stones in their 'b' row in the same column as the 'a' row, but the 'a' row hole has no stones, then nothing happens. Similarly, nothing happens unless the sowing process ends in one of the 8 'a' holes.

The objective is to remove all of your opponents stones.

Game 2
In this game the first half of the move resembles Game 1. Each player sows a square, and pieces are captured on the basis of the same conditions. However,  the captured pieces are not removed, but are transferred to the moving player's hand. From there, the moving player's hand will move backwards (clockwise motion, opposite to the direction of normal play) until they encounter an empty hole. From this there are two variations, both of which hinge on an edge case:

a. All of the captured stones are placed in this empty hole, and the player is forced to begin the sowing process from that hole.
b. The hand moves forwards (anticlockwise, standard play direction) one hole and begins dropping stones from their hand, as if they had sowed from the empty hole. However, an important distinction is that the hand does not interact with the empty hole.

These variations exist because there are occasions where there are no empty holes. The player is then forced to continue either of the above processes (although the variations must be kept consistent across a game) from the hole with the most stones, and, when there is a tie, they are allowed to choose which hole they sow from.

Again, the objective is to remove all of your opponent's stones.

Game 3
This game is unusual in that I'm not sure if it is possible to win. This game's rules takes from the first more than the second. Again, each player begins be sowing their stones, and, like in the first game, the stones are captured if they are in the 'a' row. However, instead of removing the stones or transferring them to your board, the captured stones are redistributed in any formation along the opponent's board. 

This sounds unusual until you realize the objective: to force the entirety of the opponent's 32 stones into two piles. 

# Crab Rave on the Ocean Floor

This is a write up for me to talk about the process of the elaboration I did on the day 7 puzzle of Advent of Code 2021. This discussion relies on knowing the background of the initial problem. If you haven't read [AoC Day 7 problem](https://adventofcode.com/2021/day/7), go read that first.

## Problem Restatement

I wanted to complicate the initial problem statement, because why not? In the initial problem the crabs needed to get in a line to shoot a super powered blast into the underground cave system. But what if the crab submarine's aren't powerful enough to make it through. Each crab can only remove a little bit of earth, but if they all formed a large circle on the ocean floor and then drilled down the could "spy-move laser glass cut" through the floor and make a whole for the submarine. So here is the proposed alternate problem definition.

> Santa's elves use an Ohio class submarine which measures 170 meters in length. The whale is fast approaching and the submarine needs to get into the subterranean cave system. Each crab submarine is equipped with a small laser drill which can cut through numerous layers of rock, but only right below it. For this to work, the crabs will need to form a circle on the ocean floor so they can use their laser drills to blast a whole in the ocean floor. The number of crab submarines, their speed, where they go, and how they get there will change as the problem evolves.

## Iterate, Iterate, and... Iterate

The new problem statement is certainly harder than the original, so in order to get to a solution, we're going to walk through the problem, starting simple and adding complexity until we're at the final problem.

### Initial Solution

First, tackling the initial original problem statement. When approaching the problem I brainstormed a couple of different problems. The first being a super brute force version, where for each horizontal value the total gas usage is calculated. Then the minimum value is found from the resulting set of values.

I decided to implement this solution solely because I wanted to see how ridiculous the processing times would get. I decided to make it a little smarter by checking how the locations of the crab submarines are distributed by using the mean and the median positions. If the mean is greater than the median that means that there are more crabs with smaller positional values, and vice versa. Then the computation starts from either the lowest or highest horizontal value iterating through each value and calculating the gas consumption. Starting from an end point, the gas usage values will decrease until the minimum.

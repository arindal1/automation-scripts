% Facts
adjacent(1, 2).
adjacent(1, 3).
adjacent(2, 1).
adjacent(2, 3).
adjacent(3, 1).
adjacent(3, 2).

% Rules
color(1, Red) :- color(2, Green), color(3, Blue), Red \= Green, Red \= Blue.
color(2, Green) :- color(1, Red), color(3, Blue), Green \= Red, Green \= Blue.
color(3, Blue) :- color(1, Red), color(2, Green), Blue \= Red, Blue \= Green.

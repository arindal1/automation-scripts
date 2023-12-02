% Facts
busy(john, monday, 9, 12).
busy(jane, monday, 10, 11).
busy(bob, monday, 14, 16).

% Rules
free(Person, Day, Time) :-
   \+ busy(Person, Day, Start, End),
   between(Start, End, Time).

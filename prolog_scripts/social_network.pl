% Facts
friend(john, jane).
friend(jane, bob).
friend(bob, alice).

% Rules
connected(X, Y) :- friend(X, Y).
connected(X, Y) :- friend(X, Z), connected(Z, Y).

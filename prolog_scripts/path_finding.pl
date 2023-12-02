% Facts
edge(a, b, 3).
edge(b, c, 2).
edge(c, d, 5).
edge(a, d, 10).

% Rules
path(X, Y, Path, Cost) :-
   travel(X, Y, [X], Q, Cost),
   reverse(Q, Path).

travel(X, Y, P, [Y|P], C) :-
   edge(X, Y, C).
travel(X, Y, Visited, Path, Cost) :-
   edge(X, Z, C),
   Z \== Y,
   \+member(Z, Visited),
   travel(Z, Y, [Z|Visited], Path, C1),
   Cost is C + C1.

% Facts
edge(a, b).
edge(b, c).
edge(b, d).
edge(d, e).

% Rules
path(X, Y) :- edge(X, Y).
path(X, Y) :- edge(X, Z), path(Z, Y).

% Query: Is there a path from a to e?
% ?- path(a, e).

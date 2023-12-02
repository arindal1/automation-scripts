% Facts
parent(john, jim).
parent(john, ann).
parent(jim, jill).
parent(ann, tom).

% Rules
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).

% Query: Who is Tom's ancestor?
% ?- ancestor(X, tom).

% Facts
verb(eat).
noun(apple).
noun(orange).

% Rules
sentence(X, Y, Z) :- noun(X), verb(Y), noun(Z).

% Query: Is "apple eat orange" a valid sentence?
% ?- sentence(apple, eat, orange).

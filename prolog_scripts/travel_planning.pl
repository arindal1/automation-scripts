% Facts
flight(london, new_york).
flight(new_york, boston).
flight(new_york, los_angeles).
flight(boston, chicago).
flight(boston, san_francisco).
flight(chicago, los_angeles).
flight(san_francisco, los_angeles).

% Rules
route(X, Y) :- flight(X, Y).
route(X, Y) :- flight(X, Z), route(Z, Y).

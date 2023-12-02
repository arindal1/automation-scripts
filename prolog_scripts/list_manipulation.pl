% Rules
append([], L, L).
append([H|T1], L2, [H|T3]) :- append(T1, L2, T3).

% Query: Append two lists
% ?- append([1, 2, 3], [4, 5, 6], Result).

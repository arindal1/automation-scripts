% Library for CLP
:- use_module(library(clpfd)).

% Rules
sudoku_4x4(Rows) :-
   length(Rows, 4),
   maplist(same_length(Rows), Rows),
   append(Rows, Vs), Vs ins 1..4,
   maplist(all_distinct, Rows),
   transpose(Rows, Columns),
   maplist(all_distinct, Columns),
   maplist(label, Rows).

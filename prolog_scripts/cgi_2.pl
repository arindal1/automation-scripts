:- use_module(library(http/html_write)).

% HTTP Handler
:- http_handler(root(hello), say_hello, []).

say_hello(Request) :-
    member(search(Query), Request),
    format('Content-type: text/html~n~n'),
    format('<html><head><title>Hello Prolog CGI</title></head><body>'),
    format('<h2>Hello Prolog CGI!</h2>'),
    format('<p>Query received: ~w</p>', [Query]),
    format('</body></html>').

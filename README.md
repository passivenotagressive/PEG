# PEG
PEG for creating latex tables, created with canopy: http://canopy.jcoglan.com/

File latex.py is created by canopy according to my latex.peg file that describes my grammar
File latex_nodes.py is file written by me that describes how the atributes of parse tree nodes should be counted

To get latex table from the view, like this:

\    ||| foo       | bar
\-

\-

baz ||| foobaz | barbaz

biz  ||| foobiz   | barbiz

\-

To get latex code for this type of table you should type the table in the input.txt filel, and run the act_latex.py file

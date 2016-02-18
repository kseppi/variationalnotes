# Variational Notes

These are some notes I've made to help me remember how variational inference
works.  You are welcome to use them, so long as you cite them.

## Possible Problems and Solutions

If you have trouble related to the `bayesnet` library for `tikz`, you have two
options.  One is to upgrade to texlive-2015 (which fixed the improper packaging
that causes `bayesnet` to seem to be not present in the tex distribution).  As
an alternative (which is what I did), simply clone the repository at
https://github.com/jluttine/tikz-bayesnet into your local texmf directory in the
correct structure.  (For me, the location where I cloned the repository was at
`~/texmf/tex/latex`.)

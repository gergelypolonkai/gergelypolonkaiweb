# -*- coding: utf-8 -*-
"""
    pygments.styles.solarized_dark
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Solarized style. See http://ethanschoonover.com/solarized for details.
    Solarized is created by Ethan Schoonover.
"""

from pygments.style import Style
from pygments.token import Comment, Error, Generic, Keyword, Literal, Name, Number, Operator, Other, Punctuation, String, Text, Token, Whitespace

class SolarizedDarkStyle(Style):
    """
    Solarized style.
    """

    default_style = ''

    styles = {
        Comment: '#586e75',
        Comment.Multiline: '#586e75',
        Comment.Preproc: '#586e75',
        Comment.Single: '#586e75',
        Comment.Special: '#586e75',
        Error: '',
        Generic: '',
        Generic.Deleted: '',
        Generic.Emph: '',
        Generic.Error: '',
        Generic.Heading: '',
        Generic.Inserted: '',
        Generic.Output: '',
        Generic.Prompt: '',
        Generic.Strong: '',
        Generic.Subheading: '',
        Generic.Traceback: '',
        Keyword: '#b58900',
        Keyword.Constant: '',
        Keyword.Declaration: '',
        Keyword.Namespace: '',
        Keyword.Pseudo: '',
        Keyword.Reserved: '',
        Keyword.Type: '',
        Literal: '',
        Literal.Date: '',
        Name: '',
        Name.Attribute: '',
        Name.Builtin: '#2aa198',
        Name.Builtin.Pseudo: '',
        Name.Class: '',
        Name.Constant: '',
        Name.Decorator: '',
        Name.Entity: '',
        Name.Exception: '',
        Name.Function: '#93a1a1',
        Name.Label: '',
        Name.Namespace: '',
        Name.Other: '',
        Name.Property: '',
        Name.Tag: '',
        Name.Variable: '#268Bd2',
        Name.Variable.Class: '',
        Name.Variable.Global: '',
        Name.Variable.Instance: '',
        Number: '#2aa198',
        Number.Float: '#2aa198',
        Number.Hex: '#2aa198',
        Number.Integer: '#2aa198',
        Number.Integer.Long: '#2aa198',
        Number.Oct: '#2aa198',
        Operator: '#859900',
        Operator.Word: '#859900',
        Other: '',
        Punctuation: '',
        String: '#2aa198',
        String.Backtick: '#2aa198',
        String.Char: '#2aa198',
        String.Doc: '#2aa198',
        String.Double: '#2aa198',
        String.Escape: '#2aa198',
        String.Heredoc: '#2aa198',
        String.Interpol: '#2aa198',
        String.Other: '#2aa198',
        String.Regex: '#2aa198',
        String.Single: '#2aa198',
        String.Symbol: '#2aa198',
        Text: '',
        Token: '#93a1a1',
        Whitespace: ''
    }

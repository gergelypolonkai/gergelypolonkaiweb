# gergely.polonkai.eu

I have decided to rewrite my web site engine (http://gergely.polonkai.eu/ – currently in PHP with Symfony 2) in Python, using the [Django Framework](https://www.djangoproject.com/).

## Nice. Why?

See my [blog post](http://gergely.polonkai.eu/blog/2013/09/24/from-symfony-to-django-in-two-days.html) about it. However, the story is a bit more than this.

* I am writing a C library using GLib and GObject
* for that, I have written some Python examples
* while testing “my” Python bindings, the Django Framework came into my mind, as I have already heard about it before while I was developing using Symfony 2
* I took a look, then took a big breath
* I learned Python and Django in about 6 hours (no, I haven’t mastered either of them; just learned the basics)
* I’ve converted my old, heavyweight Symfony project (~250MB with the `vendors` folder) to Django (~60MB with all the required libraries)

## I think you did this-or-that wrong

As I said, I’m no Python expert, which means there may be stuff that is against best practice. If you point me out, I will be grateful!

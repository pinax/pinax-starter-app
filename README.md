# pinax-starter-app

`pinax-starter-app` is a starter app template for Pinax apps.

Quickly setup the scaffolding for your django app.

What you get:

* test infrastructure
* Travis configuration with coveralls
* MIT LICENSE
* setup.py


## Getting Started

Execute:

```
pip install Django
django-admin.py startapp --template=https://github.com/pinax/pinax-starter-app/zipball/master --extension=py,rst,in,sh,rc,yml,cfg,ini,coveragerc <project_name>
```

After you are running you have a fresh app, first update this readme by removing
everything above and including this line.

---

![](http://pinaxproject.com/pinax-design/patches/blank.svg)

# Pinax {{ app_name|title }}

[![](https://img.shields.io/pypi/v/pinax-{{ app_name }}.svg)](https://pypi.python.org/pypi/pinax-{{ app_name }}/)
[![](https://img.shields.io/badge/license-MIT-blue.svg)](https://pypi.python.org/pypi/pinax-{{ app_name }}/)

[![Codecov](https://img.shields.io/codecov/c/github/pinax/pinax-{{ app_name }}.svg)](https://codecov.io/gh/pinax/pinax-{{ app_name }})
[![CircleCI](https://circleci.com/gh/pinax/pinax-{{ app_name }}.svg?style=svg)](https://circleci.com/gh/pinax/pinax-{{ app_name }})
![](https://img.shields.io/github/contributors/pinax/pinax-{{ app_name }}.svg)
![](https://img.shields.io/github/issues-pr/pinax/pinax-{{ app_name }}.svg)
![](https://img.shields.io/github/issues-pr-closed/pinax/pinax-{{ app_name }}.svg)

[![](http://slack.pinaxproject.com/badge.svg)](http://slack.pinaxproject.com/)


Pinax
------

Pinax is an open-source platform built on the Django Web Framework. It is an ecosystem of reusable Django apps, themes, and starter project templates.

This collection can be found at http://pinaxproject.com.


Running the Tests
-------------------

```
$ pip install detox
$ detox
```


Documentation
---------------

The `pinax-{{ app_name }}` documentation is currently under construction. If you would like to help us write documentation, please join our Pinax Project Slack team and let us know! The Pinax documentation is available at http://pinaxproject.com/pinax/.


Contribute
----------------

See this blog post http://blog.pinaxproject.com/2016/02/26/recap-february-pinax-hangout/ including a video, or our How to Contribute (http://pinaxproject.com/pinax/how_to_contribute/) section for an overview on how contributing to Pinax works. For concrete contribution ideas, please see our Ways to Contribute/What We Need Help With (http://pinaxproject.com/pinax/ways_to_contribute/) section.

In case of any questions we recommend you join our Pinax Slack team (http://slack.pinaxproject.com) and ping us there instead of creating an issue on GitHub. Creating issues on GitHub is of course also valid but we are usually able to help you faster if you ping us in Slack.

We also highly recommend reading our Open Source and Self-Care blog post (http://blog.pinaxproject.com/2016/01/19/open-source-and-self-care/).


Code of Conduct
----------------

In order to foster a kind, inclusive, and harassment-free community, the Pinax Project has a code of conduct, which can be found here  http://pinaxproject.com/pinax/code_of_conduct/. We ask you to treat everyone as a smart human programmer that shares an interest in Python, Django, and Pinax with you.


Pinax Project Blog and Twitter
--------------------------------

For updates and news regarding the Pinax Project, please follow us on Twitter at @pinaxproject and check out our blog http://blog.pinaxproject.com.

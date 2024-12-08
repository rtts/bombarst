De Bombarst
===========

This repository contains the source code of
[bombarst.created.today](https://bombarst.created.today/), a website
created by [Return to the Source](https://rtts.eu/), provided here for
everyone to use under the [GPLv3](LICENSE) license as part of our free
and open source philosophy.


Installation
------------

Install Python and run the following commands:

    pip install -r requirements.txt
    ./manage.py migrate
    ./manage.py createsuperuser
    ./manage.py runserver


Usage
-----

Visit http://localhost:8000/edit/ to edit the homepage. You can add
various types of sections and click the save icon. These sections can
then be edited by clicking their edit icons.

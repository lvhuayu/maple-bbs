#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: forms.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-06-03 19:27:58 (CST)
# Last Update:星期一 2016-6-27 14:59:44 (CST)
#          By:
# Description:
# **************************************************************************
from flask_wtf import Form
from wtforms import SelectField, StringField
from wtforms.validators import DataRequired
from flask_babel import lazy_gettext as _


class SortForm(Form):
    display = SelectField(
        _('Choice'),
        coerce=int,
        choices=[(0, 'all topic'), (1, 'one day'), (2, 'one week'), (
            3, 'one month')])
    sort = SelectField('Sort',
                       coerce=int,
                       choices=[(0, 'publish'), (1, 'author')])
    st = SelectField('Up and Down',
                     coerce=int,
                     choices=[(0, 'down'), (1, 'up')])


class SearchForm(Form):
    search = StringField(_('search'), validators=[DataRequired()])

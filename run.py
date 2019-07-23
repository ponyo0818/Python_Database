# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 22:07:44 2017

@author: Yuan
"""
SELECT hex(User.name || Course.title || Member.role ) AS X FROM
  User JOIN Member JOIN Course
  ON User.id = Member.user_id AND Member.course_id = Course.id
  ORDER BY X
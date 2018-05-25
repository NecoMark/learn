#!/usr/bin/env python  
# -*- coding:utf-8 -*-
"""
Created on 2017年11月23日

@author: ljyang
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in xrange(len(nums)-1):
            for j in xrange(i+1, len(nums), 1):
                if nums[i] + nums[j] == target:
                    return [i, j]


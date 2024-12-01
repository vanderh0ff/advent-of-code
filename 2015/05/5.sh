#!/bin/bash
grep -E '(.).\1' input.txt | grep -Ec '(..).*\1'

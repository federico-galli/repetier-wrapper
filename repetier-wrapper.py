#!/usr/bin/env python3

#Author Federico E. Galli

#Enables PrusaSlicer on Repetier-Host v2.1.3
#Install:
#1- copy repetier-wrapper.py in the prusa-slicer binary directory
#2- point to repetier-wrapper.py instead of prusa-slicer binary in Repetier-Host

import os,sys
gui = 0

def paramlist_to_param(param):
    res = (" ".join(param))
    return(res)

#where are we?
file = sys.argv[0]
pathname = os.path.dirname(file)
location = os.path.abspath(pathname)
#print(location)

if len(sys.argv)<2:
    print ("This is a wrapper intended to run Prusa Slicer on Repetier Host v2.1.3")
    sys.exit(1)

#print('original input '+str(sys.argv))

for n,i in enumerate(sys.argv):
   if i == '--gui' :
       sys.argv[n] = ''
       gui = 1
       break

if not gui : sys.argv.extend(['--slice'])

#print('result output '+str(sys.argv))

commandline_args=(paramlist_to_param(sys.argv[1:]))
os.system(location+'/prusa-slicer '+commandline_args)

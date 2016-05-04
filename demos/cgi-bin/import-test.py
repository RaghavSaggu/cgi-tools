#!/usr/bin/env python

from cgi_tools import force_C_locale, set_resource_limits

def cgi_main():
    print "Content-Type: text/plain"
    print
    print "Hello World, cgi_tools imported!"


if __name__ == "__main__":
    set_resource_limits(walltime=3)
    force_C_locale()
    cgi_main()
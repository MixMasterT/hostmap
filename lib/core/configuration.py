#!/usr/bin/env python
#
#   hostmap
#
#   Author:
#    Alessandro `jekil` Tanasi <alessandro@tanasi.it>
#
#   License:
#    This program is private software; you can't redistribute it and/or modify
#    it. All copies, included printed copies, are unauthorized.
#    
#    If you need a copy of this software you must ask for it writing an
#    email to Alessandro `jekil` Tanasi <alessandro@tanasi.it>



from lib.supadict import supaDict

class configuration(supaDict):
    """
    User configuration / options

    @author: Alessandro Tanasi <alessandro@tanasi.it>
    """
    

    
    
    
# This class must be a Singleton. There is only one set of options.
conf = configuration()
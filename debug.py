#!/usr/bin/env python
import time
from crayon.debug import debug_stream, unpack_datachunk


phones = { "b6a9336d5ccdb7c2" : "Galaxy S4", "8a94242a4db2a511" : "Xiaomi Mi3" }

if __name__ == "__main__":
    print "Listening for debug messages from test devices..."
    for msg in debug_stream("*"): 
        datachunk = unpack_datachunk(msg)
        if not msg.device_id in phones: continue
        print ""
        print "Device:", msg.device_id, "( %s )" % phones[msg.device_id]
        print "Last Updated:", time.strftime("%c") 
        print "   # XBs: ", len(datachunk.exposure_blocks)
        print "   # evts: ", sum([len(xb.events) for xb in datachunk.exposure_blocks])
        for xb in datachunk.exposure_blocks:
            print "   l1_thresh:", xb.L1_thresh
            print "   frame rate: %2.1f" % ( xb.L1_processed*1.e3/(xb.end_time - xb.start_time) )
        #print "l1_thresh: ", xb.l1thresh 

#!/bin/sh
grfcodec -e Southern_Pacific_Steam_Set-0.5/sps.grf
rm Southern_Pacific_Steam_Set-0.5/sps.bak
rm Southern_Pacific_Steam_Set-0.5/Southern_Pacific_Steam_Set-0.5.tar
tar cvf Southern_Pacific_Steam_Set-0.5/Southern_Pacific_Steam_Set-0.5.tar Southern_Pacific_Steam_Set-0.5/*.txt Southern_Pacific_Steam_Set-0.5/*.grf

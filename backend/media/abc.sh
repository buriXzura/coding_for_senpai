#!/bin/bash

VAR="This is where we select from a table."

if grep -i -q "she\|that\|for" <<< "$VAR"
then
   echo "contains the substring sequence \"select\""
fi


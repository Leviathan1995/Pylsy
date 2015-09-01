#!/bin/bash
git log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf > AUTHORS

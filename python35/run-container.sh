#!/bin/bash

docker run -it --volume $PWD:/usr/src/app/ --privileged python35_app bash

#!/bin/bash

docker run -it --volume $PWD:/usr/src/app/ --privileged python_twisted_app bash

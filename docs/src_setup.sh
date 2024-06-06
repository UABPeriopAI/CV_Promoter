#!/bin/bash

cd /workspaces/CV_Promoter/src
pip install --upgrade pip setuptools wheel\
	    && pip install -e ".[dev]"

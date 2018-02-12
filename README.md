# HDF5 performance tests on Thinkpad X200

* Ubuntu 14.04
* Python 3.6.4 / pandas 0.22.0

Comparing speed:

Operation           | Time (in seconds)
--------------------|-------------------
Write to CSV file   | 29s
Write to HDF5 file  |  2s
Read from CSV file  |  5s
Read from HDF5 file |  0.9s

Comparing file size:

File Type | File Size
----------|-----------
CSV       | 194M
HDF5      |  84M

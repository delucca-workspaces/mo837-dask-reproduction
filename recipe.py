import hpccm

# Base
Stage0 += baseimage(image='ubuntu')

# Dask Installation
Stage0 += pip(packages=['numpy', 'pandas', 'dask', 'distributed'], pip='pip3')

# Setup application
Stage0 += copy(src='src/app.py', dest='/app.py')

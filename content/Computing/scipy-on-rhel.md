---
title: Compiling SciPy on RHEL6
date: 2013-05-20 12:00
tags: python, hpc, software, scipy, linux
...


Within the past two years I've discovered something interesting about myself
(...actually really, _really_ boring about myself):
I can be happily entertained for hours on end setting up my
computational environment _just_ right.  I find that it gives me a similar
type of satisfaction to cataloguing my music collection.  I guess you could
call it a hobby.

Usually this entails installing the usual suspects (`NumPy`, `Pandas`,
`IPython`, `matplotlib`, etc.) in a python
[virtual environment](http://www.virtualenv.org/en/latest/).
When I'm particularly into it (which is always), I'll also compile the python
distribution itself.  I've had several opportunities to indulge this pasttime,
most recently in setting up my research pipeline on the
[Flux](http://cac.engin.umich.edu/resources/systems/flux)
high-performance compute cluster at The University of Michigan.

Installing `NumPy` is usually no trouble at all, but for some reason
(if you know, please tell me), `SciPy` has _always_ given me a
"BlasNotFoundError" when installing on the Red Hat Enterprise Linux distros
commonly used on academic clusters.

```console
> pip install scipy
Downloading/unpacking scipy
  Downloading scipy-0.12.0.zip (10.2MB): 100% 10.2MB downloaded
...
numpy.distutils.system_info.BlasNotFoundError:
    Blas (http://www.netlib.org/blas/) libraries not found.
    Directories to search for the libraries can be specified in the
    numpy/distutils/site.cfg file (section [blas]) or by setting
    the BLAS environment variable.
```

I _know_ BLAS and LAPACK are installed as shared libraries: at Michigan State
University I had to load the respective modules, but at UMich they're right
there in `/usr/lib64/atlas`.  So why `pip install SciPy` always gives me that
error, I have no clue.  I've set the BLAS and LAPACK environmental
variables to the relevant shared libraries.  I've run
`python setup.py build --fcompiler=gnu95` directly.  But I always got that
same error.

Anyway, I _finally_ got it to work, so I thought I'd share the steps I took
just in case it helps someone else.  My solution was found on Stack Overflow
(surprise, surprise): The accepted answer to
[this](http://stackoverflow.com/q/7496547/848121) question.

```bash
mkdir -p ~/.local/src/
cd ~/.local/src/
wget -O BLAS.tgz http://www.netlib.org/blas/blas.tgz
tar -xzf BLAS.tgz
cd BLAS
gfortran -O3 -std=legacy -m64 -fno-second-underscore -fPIC -c *.f
ar r libfblas.a *.o
ranlib libfblas.a
export BLAS=$PWD/libfblas.a

cd ~/.local/src/
wget -O LAPACK.tgz http://www.netlib.org/lapack/lapack.tgz
tar -xzf LAPACK.tgz
# The resulting directory may be named lapack-<version>/
# the following assumes that it's named LAPACK/
cd LAPACK
cp INSTALL/make.inc.gfortran make.inc
vim make.inc
# Change OPTS = -O2 to OPTS = -O2 -fPIC
# Change NOOPT = -O0 to NOOPT = -O0 -fPIC
make lapacklib
export LAPACK=$PWD/libflapack.a

cd ~/.local/src/
git clone https://github.com/scipy/scipy.git
cd scipy
python setup.py build --fcompiler gnu95
python setup.py install
# Assuming you're already in the virtualenv you want to install to.
```

I don't know which other systems this will work on, but it does successfully
install SciPy for me.  On Python 3.3.2, running the unit tests give me
several errors and failures (nothing too scary looking), but everything passes
on Python 2.7.5!

Enjoy.

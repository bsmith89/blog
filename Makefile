-include local.mk
# This file should include FTP_HOST, FTP_USER, FTP_TARGET_DIR,
# SSH_HOST, SSH_PORT, SSH_USER, SSH_TARGET_DIR, DROPBOX_DIR,
# etc.

.POSIX:
.SECONDARY:
.DELETE_ON_ERROR:

PY ?= python3
PELICAN ?= pelican
PELICANOPTS =

VENV ?= .venv
export VIRTUAL_ENV := $(abspath ${VENV})
export PATH := ${VIRTUAL_ENV}/bin:${PATH}

INPUTDIR = content
OUTPUTDIR_DEV = output_dev
OUTPUTDIR_PUB = output_pub
OUTPUTDIR_GH = output_gh

CONFFILE = pelicanconf.py
PUBLISHCONF = publishconf.py
GHCONF = githubconf.py

SSH_HOST = webhost
GH_BRANCH = gh-pages

DEBUG ?= 0
ifeq (${DEBUG}, 1)
	PELICANOPTS += -D
endif

RELATIVE ?= 0
ifeq (${RELATIVE}, 1)
	PELICANOPTS += --relative-urls
endif

help:
	@echo 'Makefile for a pelican Web site                                           '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make html                           (re)generate the web site          '
	@echo '   make clean                          remove the generated files         '
	@echo '   make devserver [PORT=8000]          start/restart develop_server.sh    '
	@echo '   make stopserver                     stop local server                  '
	@echo '   make rsync_upload                   upload the web site via rsync+ssh  '
	@echo '   make github_upload                  upload the web site via gh-pages   '
	@echo '   make upload                         carefully upload rsync, gh-pages   '
	@echo '                                                                          '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html   '
	@echo 'Set the RELATIVE variable to 1 to enable relative urls                    '
	@echo '                                                                          '

${OUTPUTDIR_DEV}: ${INPUTDIR}/**/*
	@rm -rf $@
	${PELICAN} ${INPUTDIR} -D -o $@ -s ${CONFFILE} ${PELICANOPTS}

${OUTPUTDIR_PUB}: ${INPUTDIR}/**/*
	@rm -rf $@
	${PELICAN} ${INPUTDIR} -D -o $@ -s ${PUBLISHCONF} ${PELICANOPTS}

${OUTPUTDIR_GH}: ${INPUTDIR}/**/*
	@rm -rf $@
	${PELICAN} ${INPUTDIR} -D -o $@ -s ${GHCONF} ${PELICANOPTS}
	echo 'blog.byronjsmith.com' > ${OUTPUTDIR_GH}/CNAME

html: ${OUTPUTDIR_DEV}

publish: ${OUTPUTDIR_PUB}

devserver:
ifdef PORT
	./develop_server.sh restart ${PORT}
else
	./develop_server.sh restart
endif

stopserver:
	./develop_server.sh stop
	@echo 'Stopped Pelican and SimpleHTTPServer processes running in background.'

rsync_upload: ${OUTPUTDIR_PUB}
	rsync -e "ssh -p ${SSH_PORT}" -P -rvzc --delete ${OUTPUTDIR_PUB}/ ${SSH_HOST}:${SSH_TARGET_DIR} --cvs-exclude

github_upload: ${OUTPUTDIR_GH}
	ghp-import -m "Generate Pelican site" -b ${GH_BRANCH} ${OUTPUTDIR_GH}
	git push origin ${GH_BRANCH}

upload:
	git diff --quiet  # Have you committed all your changes?
	git push
	@${MAKE} github_upload
	@${MAKE} rsync_upload

clean:
	rm -rf ${OUTPUTDIR_DEV} ${OUTPUTDIR_PUB} *.pyc __pycache__

.PHONY: html devserver stopserver rsync_upload github_upload upload clean

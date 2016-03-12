RESULT_DIR := RPMS
NAME := pushpin
VERSION := $(shell cat $(NAME).spec |grep 'Version:' |cut -d: -f2|tr -d '[:space:]')
RELEASE := $(shell cat $(NAME).spec |grep 'Release:' |cut -d: -f2|tr -d '[:space:]'| tr -d '%{dist}')
DIST := .el7.centos
MOCK_OPTS :=

sources:
	spectool -g $(NAME).spec

srpm: sources
	mock --buildsrpm --sources=. --spec="$(NAME).spec" --result=$(RESULT_DIR) $(MOCK_OPTS)

rpm: srpm
	mock --result=$(RESULT_DIR) --rebuild $(RESULT_DIR)/$(NAME)-$(VERSION)-$(RELEASE)$(DIST).src.rpm $(MOCK_OPTS)

clean:
	rm -f $(NAME).spec
	rm -f $(NAME)-$(VERSION).tar.gz
	rm -rf $(RESULT_DIR)

SHELL = /bin/bash
MAKEFLAGS += --no-print-directory

args := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
$(eval $(args):dummy;@:)

dummy:	# fake target to avoid erreur handling $(args)

run_day:
	@echo ">> Python"
	@python ./day$(args)/day*.py
	@echo ">> Golang"
	@go run ./day$(args)/main.go
	@echo ">> Ruby"
	@ruby ./day$(args)/day*.rb

run_all_python:
	@time for file in `ls ./day*/day*.py`; do echo -e "\n>> $$file"; python $$file; done

run_all:
	@for day in `ls -1d day* | grep -oP 'day(\K[0-9]{2})'`; do \
		echo ""; echo "# DAY $$day"; \
		make run_day $$day; \
		done

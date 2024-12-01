SHELL = /bin/bash
MAKEFLAGS += --no-print-directory

args := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
$(eval $(args):dummy;@:)

dummy:	# fake target to avoid erreur manipuling $(args)

run_day:
	@echo ">> Python"
	@time python ./day$(args)/day*.py
	@echo ">> Golang"
	@time go run ./day$(args)/main.go

run_all_python:
	@time for file in `ls ./day*/day*.py`; do echo -e "\n>> $$file"; python $$file; done

run_all:
	@time for file in `ls ./day*/day*.py`; do \
		echo -e "\n>> $$dir"; \
		echo -e "\n>>> Python"; \
		python $$file; \
		echo -e "\n>>> Golang"; \
		go run $$(dirname $$file)/main.go; \
		done
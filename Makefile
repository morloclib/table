.PHONY: clean
clean:
	rm nexus* pool*

.PHONY: check
check:
	morloc typecheck main.loc
	morloc make main.loc

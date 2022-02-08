.PHONY: dot clean

dot: clean
	python3.10 linkedlist.py

clean: 
	rm -rf *.png *.dot objs __pycache__
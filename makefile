all: main.py
	python main.py

run: main.py
	python main.py

clean:
	rm -f *.pyc
	rm -f *~
	rm -f *png
	rm -f *ppm
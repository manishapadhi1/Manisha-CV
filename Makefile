.PHONY: resume tailored clean-tailored

resume:
	tectonic resume.tex

tailored:
	python3 generate_tailored_cvs.py
	@mkdir -p tailored_pdfs
	@for f in tailored_tex/*.tex; do \
		label=$$(basename $$f .tex); \
		echo "Compiling $$label"; \
		tectonic --outdir tailored_pdfs $$f; \
	done

clean-tailored:
	rm -f tailored_pdfs/*.log tailored_pdfs/*.aux tailored_pdfs/*.out tailored_pdfs/*.extracted.txt

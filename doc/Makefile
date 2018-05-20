EXE=learnBoost.pdf
SRC=learnBoost.tex
BIB=learnBoost.aux

$(EXE):$(SRC)
	xelatex $(SRC)

.PHONY.:look
look:
	evince learnBoost.pdf

.PHONY.:clean
clean:
	$(RM) learnBoost.aux learnBoost.log learnBoost.pdf learnBoost.dvi learnBoost.bbl learnBoost.blg learnBoost.toc learnBoost.out learnBoost.nav learnBoost.snm learnBoost.thm learnBoost.lot learnBoost.lof

# Summary

UD_Icelandic-IcePaHC is a conversion of the [Icelandic Parsed Historical Corpus (IcePaHC)](https://linguist.is/icelandic_treebank/Icelandic_Parsed_Historical_Corpus_(IcePaHC)) to the Universal Dependencies scheme.

The conversion was done using [UDConverter](https://github.com/thorunna/UDConverter).

# Introduction

The Icelandic Parsed Historical Corpus (IcePaHC) is a one-million-word, diachronic corpus which includes 61 texts from the 12th to 21st centuries. These texts were originally manually parsed according to the Penn Parsed Corpora of Historical English (PPCHE) annotation scheme. These parsed texts were later automatically converted to the Universal Dependencies scheme to create UD_Icelandic-IcePaHC.

## Text categories

UD_Icelandic-IcePaHC contains the following main genres:
- **NAR**: Narratives (sagas, fiction)
- **REL**: Religious texts (bible, sermons)
- **SCI**: Science (linguistics, natural sciences, history)
- **BIO**: Biographical material (biographies, travelogues)
- **LAW**: Law texts

Further subclassification is reflected in the extended genre label. For example **NAR-SAG** means narrative-saga and **REL-BIB** means religious text-bible

Each sentence ID in UD-Icelandic-IcePaHC carries the following information:

```
1150.FIRSTGRAMMAR.SCI-LIN,1.1
```
- Publication year of the text (`1150`)
- Name of the text (`FIRSTGRAMMAR`)
- Text genre (`SCI-LIN`)
- Index within text (`1`)
- Index within file (`1`)

Using the sentence IDs within UD_Icelandic-IcePaHC, specific genres or periods can be extracted or filtered from the treebank CoNLL-U files.

## Data split

For further info on each text, see the [IcePaHC documentation](https://linguist.is/icelandic_treebank/Texts).

**TRAIN:**
- `1150.HOMILIUBOK.REL-SER`
- `1210.THORLAKUR.REL-SAG`
- `1250.STURLUNGA.NAR-SAG`
- `1260.JOMSVIKINGAR.NAR-SAG`
- `1270.GRAGAS.LAW-LAW`
- `1275.MORKIN.NAR-HIS`
- `1300.ALEXANDER.NAR-SAG`
- `1310.GRETTIR.NAR-SAG`
- `1325.ARNI.NAR-SAG`
- `1350.FINNBOGI.NAR-SAG`
- `1400.GUNNAR.NAR-SAG`
- `1400.VIGLUNDUR.NAR-SAG`
- `1450.ECTORSSAGA.NAR-SAG`
- `1450.JUDIT.REL-BIB`
- `1450.VILHJALMUR.NAR-SAG`
- `1480.JARLMANN.NAR-SAG`
- `1525.ERASMUS.NAR-SAG`
- `1540.NTJOHN.REL-BIB`
- `1593.EINTAL.REL-OTH`
- `1611.OKUR.REL-OTH`
- `1650.ILLUGI.NAR-SAG`
- `1659.PISLARSAGA.BIO-AUT`
- `1661.INDIAFARI.BIO-TRA`
- `1675.ARMANN.NAR-FIC`
- `1675.MAGNUS.BIO-OTH`
- `1675.MODARS.NAR-FIC`
- `1680.SKALHOLT.NAR-REL`
- `1725.BISKUPASOGUR.NAR-REL`
- `1790.FIMMBRAEDRA.NAR-SAG`
- `1791.JONSTEINGRIMS.BIO-AUT`
- `1830.HELLISMENN.NAR-SAG`
- `1835.JONASEDLI.SCI-NAT`
- `1859.HUGVEKJUR.REL-SER`
- `1861.ORRUSTA.NAR-FIC`
- `1882.TORFHILDUR.NAR-FIC`
- `1888.VORDRAUMUR.NAR-FIC`
- `1907.LEYSING.NAR-FIC`
- `1908.OFUREFLI.NAR-FIC`
- `1985.MARGSAGA.NAR-FIC`
- `1985.SAGAN.NAR-FIC`
- `2008.MAMMA.NAR-FIC`

**TEST:**
- `1150.FIRSTGRAMMAR.SCI-LIN`
- `1210.JARTEIN.REL-SAG`
- `1350.MARTA.REL-SAG`
- `1450.BANDAMENN.NAR-SAG`
- `1400.GUNNAR2.NAR-SAG`
- `1540.NTACTS.REL-BIB`
- `1628.OLAFUREGILS.BIO-TRA`
- `1745.KLIM.NAR-FIC`
- `1850.PILTUR.NAR-FIC`
- `1920.ARIN.REL-SER`

**DEV:**
- `1250.THETUBROT.NAR-SAG`
- `1350.BANDAMENNM.NAR-SAG`
- `1475.AEVINTYRI.NAR-REL`
- `1525.GEORGIUS.NAR-REL`
- `1630.GERHARD.REL-OTH`
- `1720.VIDALIN.REL-SER`
- `1888.GRIMUR.NAR-FIC`
- `1883.VOGGUR.NAR-FIC`
- `1902.FOSSAR.NAR-FIC`
- `2008.OFSI.NAR-SAG`


# Acknowledgments

This project was funded by The Strategic Research and Development Programme for Language Technology, grant no. 180020-5301. Thanks are due to Örvar Kárason, whose previous work was used as a basis for the conversion.

The Icelandic Parsed Historical Corpus (IcePaHC) is available at https://linguist.is/icelandic_treebank/Download and https://repository.clarin.is/repository/xmlui/handle/20.500.12537/62.

Morphological features were generated using ABLTagger, a PoS tagger for Icelandic, developed by Steinþór Steingrímsson, Örvar Kárason and Hrafn Loftsson and available [here](https://github.com/steinst/ABLTagger).

## References

```
@inproceedings{arnardottir-etal-2020-universal,
    title = "A {U}niversal {D}ependencies Conversion Pipeline for a {P}enn-format Constituency Treebank",
    author = "Arnard{\'o}ttir, {\TH}{\'o}runn  and
      Hafsteinsson, Hinrik  and
      Sigur{\dh}sson, Einar Freyr  and
      Bjarnad{\'o}ttir, Krist{\'\i}n  and
      Ingason, Anton Karl  and
      J{\'o}nsd{\'o}ttir, Hildur  and
      Steingr{\'\i}msson, Stein{\th}{\'o}r",
    booktitle = "Proceedings of the Fourth Workshop on Universal Dependencies (UDW 2020)",
    month = dec,
    year = "2020",
    address = "Barcelona, Spain (Online)",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.udw-1.3",
    pages = "16--25",
    abstract = "The topic of this paper is a rule-based pipeline for converting constituency treebanks based on the Penn Treebank format to Universal Dependencies (UD). We describe an Icelandic constituency treebank, its annotation scheme and the UD scheme. The conversion is discussed, the methods used to deliver a fully automated UD corpus and complications involved. To show its applicability to corpora in different languages, we extend the pipeline and convert a Faroese constituency treebank to a UD corpus. The result is an open-source conversion tool, published under an Apache 2.0 license, applicable to a Penn-style treebank for conversion to a UD corpus, along with the two new UD corpora.",
}

@inproceedings{arnardottir-etal-2023-evaluating,
    title = "Evaluating a {U}niversal {D}ependencies Conversion Pipeline for {I}celandic",
    author = "Arnard{\'o}ttir, {\TH}{\'o}runn  and
      Hafsteinsson, Hinrik  and
      Jasonarson, Atli  and
      Ingason, Anton  and
      Steingr{\'\i}msson, Stein{\th}{\'o}r",
    editor = {Alum{\"a}e, Tanel  and
      Fishel, Mark},
    booktitle = "Proceedings of the 24th Nordic Conference on Computational Linguistics (NoDaLiDa)",
    month = may,
    year = "2023",
    address = "T{\'o}rshavn, Faroe Islands",
    publisher = "University of Tartu Library",
    url = "https://aclanthology.org/2023.nodalida-1.69",
    pages = "698--704",
    abstract = "We describe the evaluation and development of a rule-based treebank conversion tool, UDConverter, which converts treebanks from the constituency-based PPCHE annotation scheme to the dependency-based Universal Dependencies (UD) scheme. The tool has already been used in the production of three UD treebanks, although no formal evaluation of the tool has been carried out as of yet. By manually correcting new output files from the converter and comparing them to the raw output, we measured the labeled attachment score (LAS) and unlabeled attachment score (UAS) of the converted texts. We obtain an LAS of 82.87 and a UAS of 87.91. In comparison to other tools, UDConverter currently provides the best results in automatic UD treebank creation for Icelandic.",
}
```

# Changelog
* 2024-11-15 v2.15
  * Fixes for (all) `leaf-det` warnings in `is_icepahc-ud-train.conllu`
  * Fixes for `flat-foreign-upos-feats` warnings in `is_icepahc-ud-train.conllu`
  * Various lemma fixes.
  * Various feature fixes.
* 2024-05-15 v2.14
  * Various lemma fixes.
  * Various feature fixes.
* 2023-11-15 v2.13
  * Various lemma fixes.
  * Various feature fixes.
* 2023-05-15 v2.12
  * Deprels for 'en', 'meðan' and 'uns' changed from `case` to `mark`.
  * Some systematic discrepancies between UPOS and universal features/IFD tags fixed.
  * Various lemma fixes.
* 2022-11-15 v2.11
  * Various lemmas fixed.
  * Validation syntax errors (too many subjects).
  * Various minor fixes for UPOS, XPOS, deprels and UD features.
  * Missing UD features added to `is_icepahc-trian.conllu`.
    * 1680.SKALHOLT.NAR-REL, sentences 150.21339 to 223.21412.
  * Missing UD features added to joined tokens, mostly pronomial clitics.
  * Incorrect `case` deprels changed to `mark` for tokens 'ef', 'þegar', 'nema', 'þótt', 'þó'.
* 2022-05-15 v2.10
  * A few errors, such as wrong lemmas, fixed.
* 2020-11-15 v2.7
  * Initial release in Universal Dependencies.


<pre>
=== Machine-readable metadata (DO NOT REMOVE!) ================================
Data available since: UD v2.7
License: CC BY-SA 4.0
Includes text: yes
Genre: fiction bible nonfiction legal
Lemmas: converted from manual
UPOS: converted from manual
XPOS: manual native
Features: automatic
Relations: converted from manual
Contributors: Arnardóttir, Þórunn; Hafsteinsson, Hinrik; Sigurðsson, Einar Freyr; Jónsdóttir, Hildur; Bjarnadóttir, Kristín; Ingason, Anton Karl; Rúnarsson, Kristján; Steingrímsson, Steinþór; Wallenberg, Joel C.; Rögnvaldsson, Eiríkur
Contributing: elsewhere
Contact: thar@hi.is, hinrik.hafst@gmail.com, einar.freyr.sigurdsson@arnastofnun.is
===============================================================================
</pre>

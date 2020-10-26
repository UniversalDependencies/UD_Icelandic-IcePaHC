# Summary

UD_Icelandic-IcePaHC is a conversion of the [Icelandic Parsed Historical Corpus (IcePaHC)](https://linguist.is/icelandic_treebank/Icelandic_Parsed_Historical_Corpus_(IcePaHC)) to the Universal Dependencies scheme.

The conversion was done using a custom-made heuristic converter.

# Introduction

The Icelandic Parsed Historical Corpus (IcePaHC) is a one-million-word, diachronic corpus which includes 61 texts from the 12th to 21st centuries. These texts were originally manually parsed according to the Penn Parsed Corpora of Historical English (PPCHE) annotation scheme. These parsed texts where then automatically converted to the Universal Dependencies scheme to create UD_Icelandic-IcePaHC.

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

For further info on each text, see the [IcePaHC documnentation](https://linguist.is/icelandic_treebank/Texts).

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

This project is funded by The Strategic Research and Development Programme for Language Technology, grant no. 180020-5301. Thanks are due to Örvar Kárason, whose previous work was used as a basis for the conversion.

Morphological features where generated using ABLTagger, a state-of-the-art PoS tagger for Icelandic. It is developed by Steinþór Steingrímsson, Örvar Kárason and Hrafn Loftsson and available from https://github.com/steinst/ABLTagger.

## References

* (citation)


# Changelog

* 2020-05-15 v2.6
  * Initial release in Universal Dependencies.


<pre>
=== Machine-readable metadata (DO NOT REMOVE!) ================================
Data available since: UD v2.6
License: CC BY-SA 4.0
Includes text: yes
Genre: fiction bible nonfiction legal
Lemmas: converted from manual
UPOS: converted from manual
XPOS: manual native
Features: automatic
Relations: converted from manual
Contributors: Sigurðsson, Einar Freyr
Contributing: elsewhere
Contact: einar.freyr.sigurdsson@arnastofnun.is
===============================================================================
</pre>

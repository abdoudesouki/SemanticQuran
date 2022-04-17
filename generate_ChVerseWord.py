#19/3/2022
http://mlode.nlp2rdf.org/semanticquran/quran1  uri Chapter
http://mlode.nlp2rdf.org/semanticquran/quran1-2-ar uri verse
http://mlode.nlp2rdf.org/semanticquran/quran1-2-1-ar uri word

classes
http://mlode.nlp2rdf.org/quranvocab#Chapter
http://mlode.nlp2rdf.org/quranvocab#Verse
http://mlode.nlp2rdf.org/quranvocab#Word

properties:
http://mlode.nlp2rdf.org/quranvocab#chapterIndex
?word rdfs:label ?lb;
 dcterms:isPartOf ?verse.
 ?word qvoc:wordIndex  ?wi.
 ?verse qvoc:verseIndex ?verseIndex.
 ?verse dcterms:isPartOf ?chapter.
 
 
 files
 ayat.tsv
 word.tsv
 
 
 Chapter
 skos:prefLabel        Litral-ar
rdfs:label             literal-multilingual
qvoc:verseCount        xsd:nonNegativeInteger
qvoc:chapterIndex      xsd:nonNegativeInteger
qvoc:chapterOrder      xsd:nonNegativeInteger
qvoc:inPage            xsd:nonNegativeInteger
qvoc:inPart            xsd:nonNegativeInteger
qvoc:inQuarter         xsd:nonNegativeInteger
qvoc:inSection         xsd:nonNegativeInteger
qvoc:inStation         xsd:nonNegativeInteger
qvoc:quranRukus        xsd:nonNegativeInteger
qvoc:revelationPlace   DBpedia-URI
owl:sameAs             DBpedia-URI
dcterms:license        URI
dcterms:provenance     Litral-en


@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix dc: <http://purl.org/dc/elements/1.1/> .
@prefix olia-ar: <http://purl.org/olia/arabic_khoja.owl#> .
@prefix gold: <http://purl.org/linguistics/gold/> .
@prefix lexvo: <http://lexvo.org/id/iso639-3/> .
@prefix qvoc: <http://www.nlp2rdf.org/quranvocab#> .

##Simple arabic file : chNo|VerseNo|text
split text to get word : 
generate uri & type info
generate label
index properties
chapters frrom ayat file with verse no=1, count of group

*Linking
DBPedia
Wiktionary
New: Wikidata
===================================================
skos:prefLabel         Litral-ar
rdfs:label             literal-multilingual
qvoc:chapterIndex      xsd:nonNegativeInteger
qvoc:verseIndex        xsd:nonNegativeInteger
qvoc:chapterName       Litral-ar
qvoc:descByJalalayn    Litral-ar
qvoc:descByMuyasser    Litral-ar
qvoc:startOfPageNo     xsd:nonNegativeInteger
qvoc:startOfPartNo     xsd:nonNegativeInteger
qvoc:startOfQuarterNo  xsd:nonNegativeInteger
qvoc:startOfStationNo  xsd:nonNegativeInteger
dcterms:license        URI
dcterms:provenance     Litral-en




names startOfPageNo , inPage changed between chapter and verse in Ontology








===================================================
skos:prefLabel        Litral-multilingual
rdfs:label            literal-multilingual
qvoc:chapterIndex     xsd:nonNegativeInteger
qvoc:verseIndex       xsd:nonNegativeInteger
qvoc:wordIndex        xsd:nonNegativeInteger
dcterms:language      Lexvo-URI
dcterms:license       URI
dcterms:provenance    Litral-en
owl:sameAs            DBpedia-URI
owl:sameAs            Wiktionary-URI




===================================================

nif , annotation char2char entity
lexical items
chapter 

lexical item ->word
--------if statement-------- label
chapter verse word ---> tanzil, start with language English



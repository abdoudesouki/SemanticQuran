PREFIX dcterms: <http://purl.org/dc/terms/>
#prefix qvoc: <http://www.nlp2rdf.org/quranvocab#> 
prefix qvoc: <http://mlode.nlp2rdf.org/quranvocab#> 

SELECT * #count(distinct ?chapter) as ?cntch,count(distinct ?verse),count(?word) as ?cntmal
 WHERE{
?word rdfs:label "زكريا"@ar;
      dcterms:isPartOf ?verse.
#?verse a <http://mlode.nlp2rdf.org/quranvocab#Verse>.
#?verse  skos:prefLabel ?verseTextAr .
?verse  rdfs:label ?verseTextAr .
  #  qvoc:verseIndex ?verseIndex;
   ?verse dcterms:isPartOf ?chapter.
FILTER(lang(?verseTextAr)="ar")
}

### a specified aya words

select * 
{
#<http://mlode.nlp2rdf.org/semanticquran/quran1> ?p ?o
<http://mlode.nlp2rdf.org/semanticquran/quran6-85-1-1-ar> ?p ?o
}

########### verses of sowra
PREFIX dcterms: <http://purl.org/dc/terms/>
prefix qvoc: <http://www.nlp2rdf.org/quranvocab#> 
prefix skos: <http://www.w3.org/2004/02/skos/core#>

SELECT *  #?lb,?verseTextAr
 WHERE{
  ?verse skos:prefLabel ?chnameAr.
  #?ch ?pp ?chix.
    ?verse a <http://mlode.nlp2rdf.org/quranvocab#Verse>.
    ?verse dcterms:isPartOf ?ch.
    ?ch a <http://mlode.nlp2rdf.org/quranvocab#Chapter>.
?verse <http://mlode.nlp2rdf.org/quranvocab#verseIndex> ?vi.
	?ch <http://mlode.nlp2rdf.org/quranvocab#chapterIndex> 2.
}
order by ?vi
#####################################words of a given verse ###

PREFIX dcterms: <http://purl.org/dc/terms/>
prefix qvoc: <http://mlode.nlp2rdf.org/quranvocab#> 

SELECT *
 WHERE{
 ?word a qvoc:Word.
 ?word rdfs:label ?lb;
      dcterms:isPartOf ?verse.
 ?word qvoc:wordIndex  ?wi.
 ?verse  rdfs:label ?verseTextAr .
 ?verse qvoc:verseIndex ?verseIndex.
 ?verse dcterms:isPartOf ?chapter.
 ?chapter qvoc:chapterIndex ?chapterIndex.
FILTER(lang(?verseTextAr)="ar")
FILTER(lang(?lb)="ar")
FILTER(?verseIndex=25)
FILTER(?chapterIndex=2)
}
order by xsd:integer(?wi)

##############################verse text
http://mlode.nlp2rdf.org/semanticquran/quran19-2
######### Lex items of a given Sowra #################
PREFIX dcterms: <http://purl.org/dc/terms/>
prefix qvoc: <http://mlode.nlp2rdf.org/quranvocab#> 
prefix skos: <http://www.w3.org/2004/02/skos/core#>
select *
where{
?li a <http://mlode.nlp2rdf.org/quranvocab#LexicalItem>.
 ?li skos:prefLabel ?lilb.
 ?li qvoc:lexicalItemIndex ?liix.
 ?li qvoc:wordIndex ?wi.
 ?li qvoc:verseIndex ?vi.
 ?li qvoc:chapterIndex 1 .
#FILTER(?lilb="زكريا")
}
order by ?vi
#####################################################
select *
where {
<http://mlode.nlp2rdf.org/semanticquran/quran18-33-1-1-ar> ?p ?o
}

describe <http://mlode.nlp2rdf.org/semanticquran/quran18-33-1-1-ar>

PREFIX dcterms: <http://purl.org/dc/terms/>
prefix skos: <http://www.w3.org/2004/02/skos/core#>
prefix qvoc: <http://mlode.nlp2rdf.org/quranvocab#>
SELECT *
 WHERE{
?li a qvoc:LexicalItem.
?li skos:prefLabe ?lilb.
#?li qvoc:lexicalItemIndex ?liix.
# ?li qvoc:verseIndex ?verseIndex.
# ?li qvoc:chapterIndex ?chapterIndex.
#FILTER(lang(?verseTextAr)="ar")
#FILTER(lang(?lb)="ar")
#FILTER(?verseIndex=85)
#FILTER(?chapterIndex=1)
#FILTER(?lb="زَكَرِيَّا"@ar)
}
#order by xsd:integer(?liix)

#######################search for word in lexitem
PREFIX dcterms: <http://purl.org/dc/terms/>
prefix skos: <http://www.w3.org/2004/02/skos/core#>
prefix qvoc: <http://mlode.nlp2rdf.org/quranvocab#>
SELECT *
 WHERE{
  ?li a qvoc:LexicalItem.
  #?li skos:prefLabel ?lilb.
  ?li rdfs:label ?lilb.
  ?li qvoc:chapterIndex ?chapterIndex.
  ?ch a qvoc:Chapter.
  #?ch rdfs:label ?chlb.
  ?ch skos:prefLabel ?chlb.
  ?ch  qvoc:chapterIndex ?chapterIndex.
  FILTER(?lilb="زكريا"@ar)
}
###################################Primary key: verse
PREFIX dcterms: <http://purl.org/dc/terms/>
prefix skos: <http://www.w3.org/2004/02/skos/core#>
prefix qvoc: <http://mlode.nlp2rdf.org/quranvocab#>
SELECT ?verseIndex,?chapterIndex,count(*) as ?cnt
 WHERE{ 
  ?vi qvoc:verseIndex ?verseIndex.
  ?vi a qvoc:Verse.
  ?vi qvoc:chapterIndex ?chapterIndex.
  #FILTER(?chapterIndex=2).
}
group by ?verseIndex ?chapterIndex
Having (count(*) > 1)
##########################################word count
PREFIX dcterms: <http://purl.org/dc/terms/>
prefix skos: <http://www.w3.org/2004/02/skos/core#>
prefix qvoc: <http://mlode.nlp2rdf.org/quranvocab#>
SELECT 
            ?verseIndex,
            ?chapterIndex,count(*) as ?cnt
 WHERE{ 
  ?wi a qvoc:Word.
  ?wi qvoc:verseIndex ?verseIndex.
  ?wi qvoc:chapterIndex ?chapterIndex.
  ?wi rdfs:label ?lb.
 # FILTER(?chapterIndex=23).
  FILTER(lang(?lb)="ar")
}
group by ?verseIndex ?chapterIndex
#Having (count(*) > 1)
order by desc(?cnt)

###-------------------------word cnt , aya cnt------------------------
PREFIX dcterms: <http://purl.org/dc/terms/>
prefix skos: <http://www.w3.org/2004/02/skos/core#>
prefix qvoc: <http://mlode.nlp2rdf.org/quranvocab#>
select ?cnt (count(?cnt) as ?cnt1)
where{
SELECT     ?verseIndex, ?chapterIndex,count(*) as ?cnt
 WHERE{ 
  ?wi a qvoc:Word.
  ?wi qvoc:verseIndex ?verseIndex.
  ?wi qvoc:chapterIndex ?chapterIndex.
  ?wi rdfs:label ?lb.
  FILTER(lang(?lb)="ar")
}
group by ?verseIndex ?chapterIndex
#Having (count(*) > 1)
}
order by desc(?cnt1)
############################################count ayat #############
PREFIX dcterms: <http://purl.org/dc/terms/>
prefix skos: <http://www.w3.org/2004/02/skos/core#>
prefix qvoc: <http://mlode.nlp2rdf.org/quranvocab#>
select sum(?cntAya)
where{
SELECT ?chapterIndex max(?verseIndex) as ?cntAya
 WHERE{ 
  ?vi qvoc:verseIndex ?verseIndex.
  ?vi a qvoc:Verse.
  ?vi qvoc:chapterIndex ?chapterIndex.
}
group by ?chapterIndex
order by desc(?cntAya)
}
#######################################Aya no of occurences###(group_concat(?hashtag;separator="|") as ?hashtags)
PREFIX dcterms: <http://purl.org/dc/terms/>
prefix qvoc: <http://www.nlp2rdf.org/quranvocab#> 
prefix skos: <http://www.w3.org/2004/02/skos/core#>

SELECT ?verseTextAr count(*) as ?vcnt count(distinct ?ch) as ?cntch
#select *
 WHERE{
  ?verse skos:prefLabel ?verseTextAr.
  #?ch ?pp ?chix.
    ?verse a <http://mlode.nlp2rdf.org/quranvocab#Verse>.
    ?verse dcterms:isPartOf ?ch.
    ?ch a <http://mlode.nlp2rdf.org/quranvocab#Chapter>.
?verse <http://mlode.nlp2rdf.org/quranvocab#verseIndex> ?vi.
	#?ch <http://mlode.nlp2rdf.org/quranvocab#chapterIndex> 1.
}
group by ?verseTextAr
having (count(*)>1)
order by desc(?vcnt)
#########################################################################
### Quraan Ayat
PREFIX dcterms: <http://purl.org/dc/terms/>
#prefix qvoc: <http://www.nlp2rdf.org/quranvocab#> DOESNOT work write explicitly/mlode
prefix skos: <http://www.w3.org/2004/02/skos/core#>

SELECT xsd:integer(?part) as ?partno #xsd:integer(?qrtr) as ?qrtrno xsd:integer(?page) as ?pageno 
xsd:integer(?chix) as ?sw_id ?chnamear xsd:integer(?vi) as ?ayano ?vpreflbl 
#xsd.integer(?part) as ?partno xsd:integer(?qrtr) as ?qrtrno xsd:integer(?page) as ?pageno 
WHERE{
  ?verse skos:prefLabel ?vpreflbl.
    ?verse a <http://mlode.nlp2rdf.org/quranvocab#Verse>.
    ?verse dcterms:isPartOf ?ch.
?verse <http://mlode.nlp2rdf.org/quranvocab#verseIndex> ?vi.
    ?ch a <http://mlode.nlp2rdf.org/quranvocab#Chapter>.
	?ch <http://mlode.nlp2rdf.org/quranvocab#chapterIndex> ?chix.
    ?ch skos:prefLabel ?chnamear.
 #?ch <http://mlode.nlp2rdf.org/quranvocab#inPage> ?page.
 ?ch <http://mlode.nlp2rdf.org/quranvocab#inPart> ?part.
 #?ch <http://mlode.nlp2rdf.org/quranvocab#inQuarter> ?qrtr.
}
order by ?chix ?vi
###############Parts start
PREFIX dcterms: <http://purl.org/dc/terms/>
prefix skos: <http://www.w3.org/2004/02/skos/core#>

select xsd:integer(?partno) xsd:integer(?vi) xsd:integer(?chix)
where{
  ?verse skos:prefLabel ?vpreflbl.
    ?verse a <http://mlode.nlp2rdf.org/quranvocab#Verse>.
    ?verse dcterms:isPartOf ?ch.
    ?verse <http://mlode.nlp2rdf.org/quranvocab#verseIndex> ?vi.
    ?verse <http://mlode.nlp2rdf.org/quranvocab#startOfPartNo> ?partno.
        ?verse dcterms:isPartOf ?ch.
    ?ch <http://mlode.nlp2rdf.org/quranvocab#chapterIndex> ?chix.
  }
order by ?partno
###############Parts start
PREFIX dcterms: <http://purl.org/dc/terms/>
prefix skos: <http://www.w3.org/2004/02/skos/core#>

select xsd:integer(?pageno) as ?pageno xsd:integer(?vi) as ?vind xsd:integer(?chix) as ?ayano
where{
  ?verse skos:prefLabel ?vpreflbl.
    ?verse a <http://mlode.nlp2rdf.org/quranvocab#Verse>.
    ?verse dcterms:isPartOf ?ch.
    ?verse <http://mlode.nlp2rdf.org/quranvocab#verseIndex> ?vi.
    ?verse <http://mlode.nlp2rdf.org/quranvocab#startOfPageNo> ?pageno.
    #    ?verse dcterms:isPartOf ?ch.
    ?ch <http://mlode.nlp2rdf.org/quranvocab#chapterIndex> ?chix.
  }
order by ?pageno
####--------------------------repeated Ayat
=Query(QUERY(Ayat!I2:I6237,"select I,count(I) group by I"),"select Col1,Col2 where Col2>1 order by Col2 desc")
####--------------------------------List of wordsPREFIX dcterms: <http://purl.org/dc/terms/>
##use R to get chapter by chapter
prefix skos: <http://www.w3.org/2004/02/skos/core#>
prefix qvoc: <http://molde.nlp2rdf.org/quranvocab#>
SELECT            ?chapterIndex, ?verseIndex,?wordIndex, ?lb
 WHERE{ 
  ?wi a <http://mlode.nlp2rdf.org/quranvocab#Word>.
 # ?wi qvoc:verseIndex ?verseIndex.
  #?wi qvoc:chapterIndex ?chapterIndex.
?wi <http://mlode.nlp2rdf.org/quranvocab#verseIndex> ?verseIndex.
?wi <http://mlode.nlp2rdf.org/quranvocab#chapterIndex> ?chapterIndex.
  ?wi skos:prefLabel ?lb.
 ?wi <http://mlode.nlp2rdf.org/quranvocab#wordIndex> ?wordIndex.
#FILTER(?chapterIndex=1).
  FILTER(lang(?lb)="ar")
}
order by xsd:integer(?chapterIndex) xsd:integer(?verseIndex) xsd:integer(?wordIndex)
##############**********************************
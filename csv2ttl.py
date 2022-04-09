# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 17:46:59 2021

@author: Abdelmonem
"""
import pandas as pd
the_data=pd.read_csv("D:\\Dropbox\\Web\\SemanticQuran\\data\\chapters.tsv",sep='\t',encoding='utf8')
print(the_data.head())
print(the_data.count())
for index, row in the_data.iterrows():
    print(index,row["sw_id"])
    

#%%
import csv
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import RDF, FOAF, RDFS, OWL, DCTERMS, SKOS, XSD
import pandas as pd
import urllib.parse

#!pip install rdflib

g = Graph()



qvoc= Namespace("http://www.nlp2rdf.org/quranvocab#")
gold= Namespace("http://purl.org/linguistics/gold/")
lexvo= Namespace("http://lexvo.org/id/iso639-3/")
semq= Namespace("http://mlode.nlp2rdf.org/semanticquran/quran")
dbpprop = Namespace("http://dbpedia.org/property/")
dbpediaOwl = Namespace("http://dbpedia.org/ontology/")



g.namespace_manager.bind("qvoc", qvoc)
g.namespace_manager.bind("semq", semq)
#g.namespace_manager.bind("cvdr", cvdr)
#g.namespace_manager.bind("lgdo", lgdo)
#g.namespace_manager.bind("vcard", vcard)

#%% read csv chapters
# Load the CSV data as a pandas Dataframe.
csv_data = pd.read_csv("D:\\Dropbox\\Web\\SemanticQuran\\data\\chapters.tsv",sep='\t',encoding='utf8')
csv_wuri = pd.read_csv("D:\\Dropbox\\Web\\SemanticQuran\\wikichaptersPy.csv",sep=',',encoding='utf8')

print(csv_data.head())
print(csv_data.count())
print(csv_wuri.count())

#%%
print(csv_data.loc[0]['sw_id'])
#%% Chapters

# Loop through the CSV data, and then make RDF triples.
for index, row in csv_data.iterrows():
     suri=URIRef(semq[str(row["sw_id"])])
     #g.add((suri, SKOS.prefLabel,Literal("سورة "+row["chnamear"], datatype=XSD.string) ))
     #g.add((suri, RDFS.label,Literal("سورة "+row["chnamear"], datatype=XSD.string) ))
     
     g.add((URIRef(semq[str(row["sw_id"])]), RDF.type,URIRef(qvoc+"Chapter") ))
     g.add((suri, URIRef(qvoc.verseCount),Literal(row["cntVerse"], datatype=XSD.nonNegativeInteger) ))
     g.add((suri, URIRef(qvoc.chapterIndex),Literal(row["sw_id"], datatype=XSD.nonNegativeInteger) ))
     g.add((suri, URIRef(qvoc.startOfPageNo),Literal(row["PageNo"], datatype=XSD.nonNegativeInteger) ))
     g.add((suri, URIRef(qvoc.startOfPartNo),Literal(row["PartNo"], datatype=XSD.nonNegativeInteger) ))
     g.add((suri, URIRef(qvoc.startOfQuarterNo),Literal(row["Rob3"], datatype=XSD.nonNegativeInteger) ))
     g.add((suri, URIRef(qvoc.startOfStationNo),Literal(row["HezbNo"], datatype=XSD.nonNegativeInteger) ))
     wuri=""
     for index, rr in csv_wuri.iterrows():
         if rr['chname'][5:]==row["chnamear"]:
             wuri=rr['wikiuri']
             break;
     if len(wuri)>0:
        print(wuri)
        g.add((suri, OWL.sameAs,wuri ))

# I remove triples that I marked as unknown earlier.
#g.remove((None, None, URIRef("http://example.org/unknown")))
#%%
mysr= pd.read_csv("D:\\SemQuran\\ar.muyassar.txt",sep='|',encoding='utf8')
jalalayn= pd.read_csv("D:\\SemQuran\\ar.jalalayn.txt",sep='|',encoding='utf8')
mysr.columns=['S','A','text']
jalalayn.columns=['S','A','text']
#mysr['A'][mysr['A'].empty()]=0
mysr['A'].fillna(0, inplace=True)
jalalayn['A'].fillna(0, inplace=True)
mysr['A']=mysr['A'].astype(int)
jalalayn['A']=jalalayn['A'].astype(int)
#mysr['S']=mysr['S'].astype(int,errors='ignore')
print(str(mysr['text'][mysr['S']=='2' ][ mysr['A']==5].tolist()[0]))
#x=mysr[['text']][  mysr['S']==1 & mysr['A']==5]
#print(x)
#%%  ====================== Verses /words==========================
csv_data = pd.read_csv("D:\\Dropbox\\Web\\SemanticQuran\\ayat.tsv",sep='\t',encoding='utf8')
print(csv_data.head())
print(csv_data.count())
for index, row in csv_data.iterrows():    
     suri=URIRef(semq[str(row["sw_id"])+"-"+str(row["ayaNo"])+"-ar"])
     g.add((suri, SKOS.prefLabel,Literal(row["text"], datatype=XSD.string) ))
     g.add((suri, RDFS.label,Literal(row["text"], datatype=XSD.string) ))
     g.add((suri, DCTERMS.isPartOf,URIRef(semq[str(row["sw_id"])])) )
     g.add((suri, URIRef(qvoc.chapterIndex),Literal(row["sw_id"], datatype=XSD.nonNegativeInteger) ))
     g.add((suri, URIRef(qvoc.verseIndex),Literal(row["ayaNo"], datatype=XSD.nonNegativeInteger) ))
     g.add((suri, URIRef(qvoc.inPage),Literal(row["PageNo"], datatype=XSD.nonNegativeInteger) ))
     g.add((suri, URIRef(qvoc.inPart),Literal(row["PartNo"], datatype=XSD.nonNegativeInteger) ))
     g.add((suri, URIRef(qvoc.inQuarter),Literal(row["Rob3"], datatype=XSD.nonNegativeInteger) ))
     g.add((suri, URIRef(qvoc.inSection),Literal(row["HezbNo"], datatype=XSD.nonNegativeInteger) ))
     g.add((suri, URIRef(qvoc.chapterName),Literal(row["chnamear"], datatype=XSD.string) ))
     tmp=mysr['text'][mysr['S']==str(row["sw_id"]) ][ mysr['A']==row["ayaNo"]].tolist()
     if len(tmp)>0:
         g.add((suri, URIRef(qvoc.descByMuyasser),Literal(tmp[0], datatype=XSD.string) ))
     tmp=jalalayn['text'][jalalayn['S']==str(row["sw_id"]) ][ jalalayn['A']==row["ayaNo"]].tolist()
     if len(tmp)>0:
         g.add((suri, URIRef(qvoc.descByJalalayn),Literal(tmp[0], datatype=XSD.string) ))
#qvoc:startOfStationNo  xsd:nonNegativeInteger
#dcterms:license        URI
#dcterms:provenance     Litral-en
     aa=row['text'].split()
     ix=1
     for w in aa:
        wuri=URIRef(semq[str(row["sw_id"])+"-"+str(row["ayaNo"])+"-"+str(ix)]+"-ar")
        g.add((wuri, SKOS.prefLabel,Literal(w, datatype=XSD.string) ))
        g.add((wuri, RDFS.label,Literal(w, datatype=XSD.string) ))
        g.add((wuri, DCTERMS.isPartOf,URIRef(semq[str(row["sw_id"])])) )
        g.add((wuri, DCTERMS.isPartOf,suri) )
        g.add((wuri, URIRef(qvoc.chapterIndex),Literal(row["sw_id"], datatype=XSD.nonNegativeInteger) ))
        g.add((wuri, URIRef(qvoc.verseIndex),Literal(row["ayaNo"], datatype=XSD.nonNegativeInteger) ))
        g.add((wuri, URIRef(qvoc.wordIndex),Literal(ix, datatype=XSD.nonNegativeInteger) ))
        ix=ix+1

'''
dcterms:language      Lexvo-URI
dcterms:license       URI
dcterms:provenance    Litral-en
owl:sameAs            DBpedia-URI
owl:sameAs            Wiktionary-URI
'''

#%%===writfile========
# Clean printing of the graph.
#print(g.serialize(format="turtle").decode())
g.serialize(destination='semq.ttl', format='ttl')
#%% ==== get wikidata uri=====================
from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
sparql.setReturnFormat(JSON)
sparql.setQuery("""
    select ?s ?lbl
     where{   
  # surah
  ?s wdt:P31 wd:Q234262.
   #?s wdt:P361 wd:Q428. partof Quran
  ?s rdfs:label ?lbl.
  filter(lang(?lbl)="ar")
   }    
    """
                )
try:
    ret = sparql.queryAndConvert()

    for r in ret["results"]["bindings"]:
        print(r)
except Exception as e:
    print(e)
#%%
sw=[]
for r in ret["results"]["bindings"]:
    row={'wikiuri':r['s']['value'],'chname':r['lbl']['value']}
    sw.append(row)
df=pd.DataFrame(sw)
df.to_csv("wikiChaptersPy.csv")
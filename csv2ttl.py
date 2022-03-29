# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 17:46:59 2021

@author: Abdelmonem
"""
import pandas as pd
the_data=pd.read_csv("D:\\Dropbox\\Web\\SemanticQuran\\chapters.tsv",sep='\t',encoding='utf8')
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


# Load the CSV data as a pandas Dataframe.
csv_data = pd.read_csv("D:\\Dropbox\\Web\\SemanticQuran\\chapters.tsv",sep='\t',encoding='utf8')

print(csv_data.head())
print(csv_data.count())

#%%
print(csv_data.loc[0]['sw_id'])
#%%

# Loop through the CSV data, and then make RDF triples.
for index, row in csv_data.iterrows():
    
     g.add((URIRef(semq[str(row["sw_id"])]), SKOS.prefLabel,Literal(row["chnamear"], datatype=XSD.string) ))
     g.add((URIRef(semq[str(row["sw_id"])]), RDFS.label,Literal(row["chnamear"], datatype=XSD.string) ))
     g.add((URIRef(semq[str(row["sw_id"])]), RDF.type,URIRef(qvoc+"Chapter") ))
     g.add((URIRef(semq[str(row["sw_id"])]), URIRef(qvoc.verseCount),Literal(row["cntVerse"], datatype=XSD.nonNegativeInteger) ))
     g.add((URIRef(semq[str(row["sw_id"])]), URIRef(qvoc.chapterIndex),Literal(row["sw_id"], datatype=XSD.nonNegativeInteger) ))
     g.add((URIRef(semq[str(row["sw_id"])]), URIRef(qvoc.inPage),Literal(row["PageNo"], datatype=XSD.nonNegativeInteger) ))
     g.add((URIRef(semq[str(row["sw_id"])]), URIRef(qvoc.inPart),Literal(row["PartNo"], datatype=XSD.nonNegativeInteger) ))
     g.add((URIRef(semq[str(row["sw_id"])]), URIRef(qvoc.inQuarter),Literal(row["Rob3"], datatype=XSD.nonNegativeInteger) ))
     g.add((URIRef(semq[str(row["sw_id"])]), URIRef(qvoc.inSection),Literal(row["HezbNo"], datatype=XSD.nonNegativeInteger) ))
    


    # g.add((URIRef(cvdr[str(row["ID"])]), URIRef(cvdo.hasCountry), URIRef(cvdr[row["COUNTRY"]])))
    
     #g.add((URIRef(cvdr[str(row["COUNTRY"])]), URIRef(cvdo.countryName), Literal(row["COUNTRY"], datatype=XSD.string)))
    
     #g.add((URIRef(cvdr[str(row["ID"])]), URIRef(cvdo.hasRegion), Literal(row["REGION"])))

    # If We want can add additional RDF/RDFS/OWL information e.g
    #g.add((URIRef(ex + subject), RDF.type, FOAF.Person))

# I remove triples that I marked as unknown earlier.
#g.remove((None, None, URIRef("http://example.org/unknown")))

#%%
csv_data = pd.read_csv("D:\\Dropbox\\Web\\SemanticQuran\\ayat.tsv",sep='\t',encoding='utf8')

print(csv_data.head())
print(csv_data.count())
for index, row in csv_data.iterrows():    
     g.add((URIRef(semq[str(row["sw_id"])+"-"+str(row(["ayaNo"]))]), SKOS.prefLabel,Literal(row["text"], datatype=XSD.string) ))
     g.add((URIRef(semq[str(row["sw_id"])+"-"+str(row(["ayaNo"]))]), RDFS.label,Literal(row["text"], datatype=XSD.string) ))
     g.add((URIRef(semq[str(row["sw_id"])+"-"+str(row(["ayaNo"]))]), DCTERMS.isPartOf,URIRef(semq[str(row["sw_id"])])) )
     g.add((URIRef(semq[str(row["sw_id"])+"-"+str(row(["ayaNo"]))]), URIRef(qvoc.chapterIndex),Literal(row["sw_id"], datatype=XSD.nonNegativeInteger) ))
     g.add((URIRef(semq[str(row["sw_id"])+"-"+str(row(["ayaNo"]))]), URIRef(qvoc.verseIndex),Literal(row["ayaNo"], datatype=XSD.nonNegativeInteger) ))
     g.add((URIRef(semq[str(row["sw_id"])+"-"+str(row(["ayaNo"]))]), URIRef(qvoc.startOfPageNo),Literal(row["PageNo"], datatype=XSD.nonNegativeInteger) ))
     g.add((URIRef(semq[str(row["sw_id"])+"-"+str(row(["ayaNo"]))]), URIRef(qvoc.startOfPartNo),Literal(row["PartNo"], datatype=XSD.nonNegativeInteger) ))
     g.add((URIRef(semq[str(row["sw_id"])+"-"+str(row(["ayaNo"]))]), URIRef(qvoc.startOfQuarterNo),Literal(row["Rob3"], datatype=XSD.nonNegativeInteger) ))
     g.add((URIRef(semq[str(row["sw_id"])+"-"+str(row(["ayaNo"]))]), URIRef(qvoc.startOfStationNo),Literal(row["HezbNo"], datatype=XSD.nonNegativeInteger) ))
     g.add((URIRef(semq[str(row["sw_id"])]), URIRef(qvoc.chapterName),Literal(row["chnamear"], datatype=XSD.string) ))

#qvoc:chapterName       Litral-ar
#qvoc:descByJalalayn    Litral-ar
#qvoc:descByMuyasser    Litral-ar
#qvoc:startOfStationNo  xsd:nonNegativeInteger
#dcterms:license        URI
#dcterms:provenance     Litral-en

#%%
# Clean printing of the graph.
#print(g.serialize(format="turtle").decode())
g.serialize(destination='semq.ttl', format='ttl')
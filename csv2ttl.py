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
cvdr = Namespace("https://covid-19ds.data/resource/")  #(for Subject/Resource)
lgdo = Namespace("http://linkedgeodata.org/page/ontology/")
vcard = Namespace("http://www.w3.org/2006/vcard/ns#")
dbpprop = Namespace("http://dbpedia.org/property/")
dbpediaOwl = Namespace("http://dbpedia.org/ontology/")



g.namespace_manager.bind("cvdo", cvdo)
g.namespace_manager.bind("cvdr", cvdr)
g.namespace_manager.bind("lgdo", lgdo)
g.namespace_manager.bind("vcard", vcard)


# Load the CSV data as a pandas Dataframe.
csv_data = pd.read_csv("D:/dice/acaps_covid19_government_measures_dataset_.csv")

print(csv_data.head())
print(csv_data.count())

#%%
print(csv_data.loc[0]['ID'])
#%%
# Here I deal with spaces (" ") in the data. I replace them with "_" so that URI's become valid.
#csv_data = csv_data.replace(to_replace=" ", value="_", regex=True)
csv_data["COUNTRY"]=csv_data["COUNTRY"].str.replace(" ","_")
csv_data["REGION"]=csv_data["REGION"].str.replace(" ","_")

# Here I mark all missing/empty data as "unknown". This makes it easy to delete triples containing this later.
#csv_data = csv_data.fillna("unknown")

# Loop through the CSV data, and then make RDF triples.
for index, row in csv_data.iterrows():
#for row in csv_data:
    # The names of the people act as subjects.
   # subject = row['Name'] #### I have made it commented #######
     #subjects = row["ID"]
    # Create triples: e.g. "Cade_Tracey - age - 27"
    #print(cvdr[str(row['ID'])], row['ISO'])
    
     g.add((URIRef(cvdr[str(row["ID"])]), URIRef(cvdo.hasISO), URIRef(cvdr[row["ISO"]])))
     
     g.add((URIRef(cvdr[str(row["ID"])]), URIRef(cvdo.hasCountry), URIRef(cvdr[row["COUNTRY"]])))
    
     g.add((URIRef(cvdr[str(row["COUNTRY"])]), URIRef(cvdo.countryName), Literal(row["COUNTRY"], datatype=XSD.string)))
    
     g.add((URIRef(cvdr[str(row["ID"])]), URIRef(cvdo.hasRegion), Literal(row["REGION"])))

    #g.add((URIRef(ex + subject), URIRef(ex + "married"), URIRef(ex + row["Spouse"])))
    #g.add((URIRef(ex + subject), URIRef(ex + "country"), URIRef(ex + row["Country"])))

    # If We want can add additional RDF/RDFS/OWL information e.g
    #g.add((URIRef(ex + subject), RDF.type, FOAF.Person))

# I remove triples that I marked as unknown earlier.
#g.remove((None, None, URIRef("http://example.org/unknown")))

# Clean printing of the graph.
#print(g.serialize(format="turtle").decode())
g.serialize(destination='my_graph.ttl', format='ttl')
# Wikidata Queries
# ==================
# 8/4/2022
# https://query.wikidata.org/
# https://www.wikidata.org/wiki/EntitySchema:E49

select *
where{   
  # surah
  ?s wdt:P31 wd:Q234262.
   #?s wdt:P361 wd:Q428. partof Quran
  ?s rdfs:label ?lbl.
  filter(lang(?lbl)="ar")
   }    
   
   select *
   {  ?s wdt:P31   wd:Q188219.#aya
   ?s wdt:P361 wd:Q428.
   ?s rdfs:label ?lbl.
   filter(lang(?lbl)="ar")
   }
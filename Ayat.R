
setwd("D:\\Dropbox\\Web\\")

#
# Author: Abdelmoneim Amer Desouki
# Statistics from Holy Quran
# ayat.tsv file contains verses ( Obtained from Semantic Quran Dataset )
# Semantic Quran A Multilingual Resource for Natural-Language Processing
#

parts=read.table('SemQuran\\parts.tsv',sep='\t',header=T)
ayat=read.table('SemQuran\\ayat.tsv',sep='\t',header=T)

ayaPartNO=integer(nrow(ayat))
pno=1
for(i in 1 :nrow(ayat)){
	print(sprintf("pno=%d, i=%d, ayat[i,1]=%d, parts[pno+1,2]=%d, parts[pno+1,3]=%d,",pno,i,ayat[i,1],parts[pno+1,2],parts[pno+1,3]))
	if(pno<30 && ayat[i,'ayano'] == parts[pno+1,2] && ayat[i,1]==parts[pno+1,3]) pno=pno+1;
	ayaPartNO[i]=pno
	# if(pno==2) browser()
}

table(ayaPartNO)

write.table(partno,file='clipboard',row.names=F)

#####\\\\
ayat=read.table('SemQuran\\ayat.tsv',sep='\t',header=T)

pages=read.table('SemQuran\\pageno.tsv',sep='\t',header=T)
ayaPageNO=integer(nrow(ayat))
pno=1
for(i in 1 :nrow(ayat)){
	print(sprintf("pno=%d, i=%d, ayat[i,1]=%d, parts[pno+1,2]=%d, parts[pno+1,3]=%d,",pno,i,ayat[i,1],pages[pno+1,2],pages[pno+1,3]))
	if(pno<604 && ayat[i,'ayano'] == pages[pno+1,2] && ayat[i,1]==pages[pno+1,3]) pno=pno+1;
	ayaPageNO[i]=pno
	# if(pno==2) browser()
}

table(ayaPartNO)

write.table(ayaPageNO,file='clipboard',row.names=F)

#####\\\\
ayat=read.table('SemQuran\\ayat.tsv',sep='\t',header=T)

qrtrs=read.table('SemQuran\\qno.tsv',sep='\t',header=T)
ayaqNO=integer(nrow(ayat))
pno=1
for(i in 1 :nrow(ayat)){
	print(sprintf("qno=%d, i=%d, ayat[i,1]=%d, qrtrs[pno+1,2]=%d, qrtrs[pno+1,3]=%d,",pno,i,ayat[i,1],qrtrs[pno+1,2],qrtrs[pno+1,3]))
	if(pno<240 && ayat[i,'ayano'] == qrtrs[pno+1,2] && ayat[i,1]==qrtrs[pno+1,3]) pno=pno+1;
	ayaqNO[i]=pno
	# if(pno==2) browser()
}

table(ayaqNO)

write.table(ayaqNO,file='clipboard',row.names=F)

###
hzbno=ceiling(ayaqNO/4)
write.table(hzbno,file='clipboard',row.names=F)

######################
library(SPARQL)
endpoint <- "http://semanticquran.aksw.org/sparql"
res_all=NULL
for(swid in 1:114){
	print(paste0('swid:',swid))
	qry <- sprintf("prefix skos: <http://www.w3.org/2004/02/skos/core#>
	prefix qvoc: <http://molde.nlp2rdf.org/quranvocab#>
	SELECT            ?chapterIndex, ?verseIndex,?wordIndex, ?lb
	 WHERE{ 
	  ?wi a <http://mlode.nlp2rdf.org/quranvocab#Word>.
	  ?wi <http://mlode.nlp2rdf.org/quranvocab#verseIndex> ?verseIndex.
	  ?wi <http://mlode.nlp2rdf.org/quranvocab#chapterIndex> ?chapterIndex.
	  ?wi skos:prefLabel ?lb.
	  ?wi <http://mlode.nlp2rdf.org/quranvocab#wordIndex> ?wordIndex.
	  FILTER(xsd:integer(?chapterIndex)=%d).
	  FILTER(lang(?lb)=\"ar\")
	}
	",swid)

# Query the endpoint, and store results in a data frame
	res <- SPARQL(url=endpoint, qry)$results
	print(paste0('#words:',nrow(res)))
	res_all=rbind(res_all,res)
}

###
w_order=order(paste(res_all[,3]+res_all[,2]*300+res_all[,1]*10000)
write.table(file='qwords1.txt',res_all[w_order,],sep='\t',)

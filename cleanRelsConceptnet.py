import pandas as pd
import sys

def getItem(pos, str):
    result = None
    items = str.split('/')
    if (len(items)>pos):
        result = items[pos]
    return result

if (len(sys.argv)<3):
    print 'usage: cleanRelsConceptnet <sourcefile> <output>'
    sys.exit()
    
sourcefile = sys.argv[1]
output = sys.argv[2]

raw_df = pd.read_csv(sourcefile, sep='\t',header=None,names=['uri',	'rel','start','end','context','strength','sourceuri','id','dataset','surfacetext'])
raw_df = raw_df[raw_df.rel != '/r/TranslationOf']
raw_df['relname'] = raw_df.rel.apply(lambda x: x.split('/')[2])

rels_df = raw_df[['start','end','relname','strength','surfacetext']]
rels_df.columns = [':START_ID', ':END_ID', ':TYPE','strength','surface']

rels_deduped = rels_df.drop_duplicates()

rels_deduped.to_csv(output,index=False)
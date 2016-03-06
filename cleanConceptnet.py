import pandas as pd
import sys

def getItem(pos, str):
    result = None
    items = str.split('/')
    if (len(items)>pos):
        result = items[pos]
    return result

if (len(sys.argv)<3):
    print 'usage: cleanConceptnet <sourcefile> <output>'
    sys.exit()
    
sourcefile = sys.argv[1]
output = sys.argv[2]

raw_df = pd.read_csv(sourcefile, sep='\t',header=None,names=['uri',	'rel','start','end','context','strength','sourceuri','id','dataset','surfacetext'])
raw_df = raw_df[raw_df.rel != '/r/TranslationOf'] #exclude for now
raw_df['endclang'] = raw_df.end.apply(lambda x: x.split('/')[2])
raw_df['startclang'] = raw_df.start.apply(lambda x: x.split('/')[2])
raw_df['startcname'] = raw_df.start.apply(lambda x: x.split('/')[3])
raw_df['endcname'] = raw_df.end.apply(lambda x: x.split('/')[3])
raw_df['startcpos'] = raw_df.start.apply(lambda x: getItem(4,x))
raw_df['endcpos'] = raw_df.end.apply(lambda x: getItem(4,x))
raw_df['startcsense'] = raw_df.start.apply(lambda x: getItem(5,x))
raw_df['endcsense'] = raw_df.end.apply(lambda x: getItem(5,x))

starts_df = raw_df[['start','startclang','startcpos','startcsense','startcname']]
starts_df.columns = ['id:ID', 'lang', 'pos','sense','name']
ends_df = raw_df[['end','endclang','endcpos','endcsense','endcname']]
ends_df.columns = ['id:ID', 'lang', 'pos','sense','name']

concept_duplicates = pd.concat([starts_df, ends_df])
concept_duplicates[':LABEL'] = 'Concept'
concept_deduped = concept_duplicates.drop_duplicates()

concept_deduped.to_csv(output,index=False)
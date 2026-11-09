
import pandas as pd

rezultate = (df
             .groupby('country')
             .size()
             .reset_index(name='ukupno_nagrada')
             .query('ukupno_nagrada >= 1')
             .sort_values('ukupno_nagrada', ascending=False)
             .reset_index(drop=True)
)
print(rezultate)


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Settings file to tune and save detector
SPECIES: INTEREST*
SITE: 
@author: jsulloa
Tomado de Latorre (2020).
"""

path_audio = {'train' : '',
              'test' : '',
              'template': ''}

detection = {'flims': (, ),
             'tlen': .,
             'th': 1e-4,
             'path_save': './features/detections_shayii.joblib'}

features = {'flims' : (, ),
            'sample_rate': ,
            'opt_spec': {'nperseg': 512, 'overlap': 0.5, 'db_range': 250},
            'opt_shape_str': 'med', # high
            'path_save': './features/features.joblib'}

selrois = {'tlen_lims': (0.2, 0.5),
           'n_clusters': 20,
           'n_samples_per_cluster': 100,
           'path_save': './trainds/df_stratsample.csv'}

trainds = {'flims': (,),
           'wl': 2,
           'path_df': './trainds/df_stratsample.csv',
           'path_save': './trainds/'}

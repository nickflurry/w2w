Model Information:
	 - type: GradientBoosting
	 - version: 0.5.0
	 - params: {'scale': True, 'center': True, 'labels': [True, False], 'multilabel': False, 'population_rates': None, 'criterion': 'friedman_mse', 'init': None, 'learning_rate': 0.01, 'loss': 'deviance', 'max_depth': 7, 'max_features': 'log2', 'max_leaf_nodes': None, 'min_impurity_decrease': 0.0, 'min_impurity_split': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'min_weight_fraction_leaf': 0.0, 'n_estimators': 700, 'presort': 'auto', 'random_state': None, 'subsample': 1.0, 'verbose': 0, 'warm_start': False, 'label_weights': OrderedDict([(False, 10)])}
	Environment:
	 - revscoring_version: '2.3.0'
	 - platform: 'Linux-4.15.0-45-generic-x86_64-with-Ubuntu-18.04-bionic'
	 - machine: 'x86_64'
	 - version: '#48-Ubuntu SMP Tue Jan 29 16:28:13 UTC 2019'
	 - system: 'Linux'
	 - processor: 'x86_64'
	 - python_build: ('default', 'Oct 22 2018 11:32:17')
	 - python_compiler: 'GCC 8.2.0'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.6.7'
	 - release: '4.15.0-45-generic'
	
	Statistics:
	counts (n=19396):
		label        n         ~True    ~False
		-------  -----  ---  -------  --------
		True     18855  -->    18482       373
		False      541  -->      280       261
	rates:
		              True    False
		----------  ------  -------
		sample       0.972    0.028
		population   0.967    0.033
	match_rate (micro=0.934, macro=0.5):
		  True    False
		------  -------
		 0.965    0.035
	filter_rate (micro=0.066, macro=0.5):
		  True    False
		------  -------
		 0.035    0.965
	recall (micro=0.964, macro=0.731):
		  True    False
		------  -------
		  0.98    0.482
	!recall (micro=0.499, macro=0.731):
		  True    False
		------  -------
		 0.482     0.98
	precision (micro=0.965, macro=0.718):
		  True    False
		------  -------
		 0.982    0.453
	!precision (micro=0.47, macro=0.718):
		  True    False
		------  -------
		 0.453    0.982
	f1 (micro=0.964, macro=0.724):
		  True    False
		------  -------
		 0.981    0.467
	!f1 (micro=0.484, macro=0.724):
		  True    False
		------  -------
		 0.467    0.981
	accuracy (micro=0.964, macro=0.964):
		  True    False
		------  -------
		 0.964    0.964
	fpr (micro=0.501, macro=0.269):
		  True    False
		------  -------
		 0.518     0.02
	roc_auc (micro=0.922, macro=0.921):
		  True    False
		------  -------
		 0.922     0.92
	pr_auc (micro=0.978, macro=0.722):
		  True    False
		------  -------
		 0.996    0.449
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'boolean'}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'true': {'type': 'number'}, 'false': {'type': 'number'}}}}}


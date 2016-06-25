def parse(params):
    new_params = dict(params)
    try:
        new_params['freq'] = int(params['freq'])
        new_params['gamma'] = float(params['gamma'])
        new_params['max_anoms'] = float(params['max_anoms'])
        new_params['nu'] = float(params['nu'])
        new_params['piecewise_median_period_weeks'] = int(params["piecewise_median_period_weeks"])
        new_params['port'] = int(params['port'])
        if params['threshold'] != u'':
            new_params['threshold'] = float(params['threshold'])
        new_params['submit_algo'] = str(params['submit_algo'])
        new_params['host'] = str(params['host'])
        new_params['user-name'] = str(params['user-name'])
        new_params['password'] = str(params['password'])
        new_params['db_name'] = str(params['db_name'])
        new_params['measurement'] = str(params['measurement'])
    except Exception as e:
        print e
    return new_params
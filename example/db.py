from .base import Parsers, Drivers, Adapters, ResultSet

def parse_query(payload, qs_params, DB_MAPS):

    query_exec = None
    result = None

    if payload:

        dbConfiguration = payload.get('dbConfiguration')
        dbConfigKey = dbConfiguration.get('dbConfigKey')
        customDbConfig = dbConfiguration.get('customDbConfig')
        query = payload.get('query')

        if dbConfigKey:
            customDbConfig = DB_MAPS.get(dbConfigKey)

        if customDbConfig:
            t_parser = customDbConfig.get('parser')
            t_adapter = customDbConfig.get('adapter')
            t_driver = customDbConfig.get('driver')
            t_resultset = customDbConfig.get('resultset')
            t_params = customDbConfig.get('params')
        else:
            raise ValueError(
                "ERROR: dbConfigKey or customDbConfig should be present"
            )

        if t_parser:

            # Parse Query
            parser = Parsers.get_for(t_parser)
            query = parser.parse_query(
                query, t_params
            )
            query_exec = query

        if t_driver and t_adapter:

            # Initialize DB
            driver = Drivers.get_for(
                t_driver, {
                    'driver_params': t_params
                }
            )
            driver.init_db_settings()
            driver.test_connection()
            db = driver.get_db_instance()

            # Run Query
            adapter = Adapters.get_for(t_adapter, {
                'db': db,
                'params': qs_params,
                'adapter_params': t_params
            })
            adapter.before_execute()
            result = adapter.execute_query(query)
            adapter.after_execute()

        if t_resultset:

            # Parse Result
            resultset = ResultSet.get_for(t_resultset)
            result = resultset.parse_resultset(result)

    else:
        raise Exception('No Object Query Found')

    return {
        "query_exec": query_exec,
        "result": result
    }
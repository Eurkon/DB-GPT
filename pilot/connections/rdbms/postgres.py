#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pilot.connections.rdbms.rdbms_connect import RDBMSDatabase


class PostgresConnector(RDBMSDatabase):
    """PostgresConnector is a class which Connector"""

    db_type: str = "postgresql"
    driver: str = "postgresql"

    default_db = ["information_schema", "performance_schema", "sys", "mysql"]

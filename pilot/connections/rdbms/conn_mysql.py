#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Optional, Any

from pilot.connections.rdbms.rdbms_connect import RDBMSDatabase


class MySQLConnect(RDBMSDatabase):
    """Connect MySQL Database fetch MetaData
    Args:
    Usage:
    """

    db_type: str = "mysql"
    db_dialect: str = "mysql"
    driver: str = "mysql+pymysql"

    default_db = ["information_schema", "performance_schema", "sys", "mysql"]

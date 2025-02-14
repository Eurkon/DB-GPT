#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from pilot.connections.rdbms.rdbms_connect import RDBMSDatabase


class OracleConnector(RDBMSDatabase):
    """OracleConnector"""

    db_type: str = "oracle"

    driver: str = "oracle"

    default_db = ["SYS", "SYSTEM", "OUTLN", "ORDDATA", "XDB"]

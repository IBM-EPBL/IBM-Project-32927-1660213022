from flask import Flask, render_template, request, redirect, url_for, session
import ibm_db
import db
import db2
import re

hostname = 'b70af05b-76e4-4bca-a1f5-23dbb4c6a74e.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud'
uid = 'jqt76961'
pwd = 'bmHWcYGRNKfYJiAA'
driver = "{IBM DB2 ODBC DRIVER}"
db_name = 'Bludb'
port = '32716'
protocol = 'TCPIP'
dsn = (
    "DATABASE ={0};"
    "HOSTNAME ={1};"
    "PORT ={2};"
    "UID ={3};"
    "SECURITY=SSL;"
    "PROTOCOL={4};"
    "PWD ={5};"
).format(db_name, hostname, port, uid, protocol, pwd)
print(dsn)
try:

    print("Connecting to db2.....")
    db2 = ibm_db.connect(dsn, "", "")
    print()
    print("Connected to database")
    print("Connection Successful!!!")

except Exception as exception:
    print("unable to connect ", exception)

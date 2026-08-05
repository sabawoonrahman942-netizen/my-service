# Zabbix Monitoring

## Overview

This project uses Zabbix to monitor the application and the server.

## Components

- Zabbix Server
- Zabbix Web Interface
- Zabbix Agent
- PostgreSQL
- Docker Compose

## Monitoring

The following metrics are monitored:

- CPU Usage
- Memory Usage
- Disk Usage
- Network Traffic
- HTTP Service Availability

## HTTP Monitoring

Item:

```
net.tcp.service[http,todo-api,5000]
```

Returns:

- 1 = Service is available
- 0 = Service is unavailable

## Trigger

Trigger Name:

```
Todo API is DOWN
```

Condition:

```
last(/devopsserver/net.tcp.service[http,todo-api,5000])=0
```

Severity:

```
High
```

## Email Notification

Configured using Gmail SMTP.

When the service goes down:

- Trigger changes to PROBLEM
- Email notification is sent automatically.

## Test

Stop the application:

```bash
docker stop todo-api
```

Expected result:

- Trigger becomes PROBLEM
- Email is received

Start the application:

```bash
docker start todo-api
```

Expected result:

- Trigger returns to OK

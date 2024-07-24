#!/bin/sh

# See https://github.com/snowflakedb/gosnowflake/issues/1182
if [ -z "$DBUS_SESSION_BUS_ADDRESS" ]; then
	export DBUS_SESSION_BUS_ADDRESS="/dev/null"
fi

exec /usr/libexec/vault/vault "$@"

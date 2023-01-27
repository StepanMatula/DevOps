#!/bin/bash

file_env() {
 local var="$1"
 local fileVar="${var}_FILE"
 local def="${2:-}"
 if [ "${!var:-}" ] && [ "${!fileVar:-}" ]; then
 echo >&2 "error: both $var and $fileVar are set (but are exclusive)"
 exit 1
 fi
 local val="$def"
 if [ "${!var:-}" ]; then
 val="${!var}"
 elif [ "${!fileVar:-}" ]; then
 val="$(< "${!fileVar}")"
 fi
 export "$var"="$val"
 unset "$fileVar"
}

file_env 'DATABASE_USER'
file_env 'DATABASE_PASSWORD'
file_env 'DATABASE_HOST'
file_env 'ACCESS_TOKEN_SECRET'

export DATABASE_URI="mongodb://$DATABASE_USER:$DATABASE_PASSWORD@$DATABASE_HOST"

exec "$@"
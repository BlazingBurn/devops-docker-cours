FROM mysql:latest

# Copy the SQL file containing data for initialization of the database to the container's entrypoint
COPY ./my_data.sql /docker-entrypoint-initdb.d/

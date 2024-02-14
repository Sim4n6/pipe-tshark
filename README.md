# Pipe Tshark Project

This project consists of two simple Flask web apps and an Nginx load balancer, all running in separate Docker containers.

## Project Structure

- `app1/`: Contains the Dockerfile and Python file for the first Flask web app.
- `app2/`: Contains the Dockerfile and Python file for the second Flask web app.
- `nginx.conf`: Contains the configuration file for the Nginx load balancer.
- `docker-compose.yml`: Defines the services that make up the app.

## How to Run


Run and build if a changge the Docker containers:

```bash
docker-compose up --build
```

You should now be able to access the Flask web apps via the Nginx load balancer at <http://localhost>.

## How to Stop

To stop the Docker containers, use the following command:

```bash
docker-compose down
```


Please replace <http://localhost> with the actual URL if you have configured it differently in your Nginx configuration.


## How to install tshark inside the container

In order to capture the traffic of the load balancer, use the following command: 

```bash
# run commands in bash inside the container
sudo docker exec -it my-docker-compose-project_load_balancer_1  /bin/bash

# install tshark inside the container (no)
apt update && apt install tshark -y

# set up tshark to capture live into /home/packets/tshark.pcap file
tshark -i any -w ./home/packets/tshark.pcap

```

## To retrieve the captured traffic live from the host side

```bash
# make a first-in-first-out pipe
mkfifo /tmp/temp.pcap

# live redirect the output from the volume synced file to the fifo  
sudo tail -n +0 -f ./packets/tshark.pcap > /tmp/sharkfin &

# run wireshark on that fifo
sudo wireshark -k -i /tmp/temp.pcap &
```

# Special thanks fly to:

-  Special thanks fly to [Gregxsundays](https://twitter.com/gregxsunday/).


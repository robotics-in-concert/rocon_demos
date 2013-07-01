rocon_demo
==========

Demo software for rocon milestones.

## Cafe Concert ##


#### Pre-requisite

```
sudo apt-get install ros-groovy-turtlebot ros-groovy-turtlebot-apps ros-groovy-turtlebot-viz
sudo apt-get install ros-groovy-turtlesim ros-groovy-rospy-message-converter ros-groovy-rosbridge-suite
sudo apt-get install ros-groovy-robot-pose-publisher ros-groovy-depth-image-proc
sudo pip install -U yujin_tools
```

#### Installation ####

```
> yujin_init_workspace --track=hydro ~/cafe_concert cafe_concert
> cd ~/cafe_concert
# Using groovy underlay...for now
> source /opt/ros/groovy/setup.bash
> rosdep install --from-paths src /opt/ros/groovy --ignore-src --rosdistro groovy -y
> yujin_init_build . -u /opt/ros/groovy
> yujin_make
```

#### Preparation for World Model Database ####

Postgresql setting for spatial world model in local machine. In order to start the cafe demo solution,
the database should contain 'docking', 'pickup', 'table1'~'table8'. Please store the data by following instruction.

```
> sudo apt-get install postgresql python-psycopg2
# Create a database
> sudo -u postgres createdb world_model
# Create a user
> sudo -u postgres createuser -D -A -P <username>
# Grant all permissions on this database to the user
> sudo -u postgres psql world_model
$ grant all privileges on database world_model to <username>
$ \q
> git clone https://github.com/WorldModel/spatial_world_model.git
> cd spatial_world_model/worldlib/scripts/
> ./setup_world_model -u <username> -p <password>
```

Remote control of postgresql configurations:

In `/etc/postgresql/9.1/main/pg_hba.conf`

```
host     world_model     <username>      0.0.0.0/0               md5
```

In `/etc/postgresql/9.1/main/postgresql.conf`

```
listen_addresses = '*'
```

Finally, restart the server:

```
> sudo service postgresql restart
```

All of these are the brief versions of

 * Ros Wiki : http://www.ros.org/wiki/spatial_world_model
 * Remote Control : https://kb.mediatemple.net/questions/1237/How+do+I+enable+remote+access+to+my+PostgreSQL+server%3F#dv

#### Annotations

Bring up the annotation app (set `WORLD_MODEL_USERNAME` and `WORLD_MODEL_PASSWORD` env variables if necessary).

```
> roslaunch cafe_rapps annotation_fake.launch
```

* Bring up the rocon_webnotator table handler interface
** files:///\<PATH_TO_WORKSPACE\>/rocon_webnotator/www/table_handler.html

* Annotate 'docking', 'pickup', and Tables.
* Video demo : http://files.yujinrobot.com/rocon/demos/cafeconcert/annotation.ogv


#### Execution ####

* Simple way to launch a demo solution in one computer

```
> echo "source ~/cafe_concert/devel/setup.bash" >> ~/.bashrc
> source ~/cafe_concert/devel/setup.bash
> rospack profile
> rocon_launch cafe_concert cafe.concert
```

* Kitchen interface : files:///\<PATH_TO_WORKSPACE\>/rocon_webinterfaces/cafe_concert/kitchen/www/index.html
* Cafe Viewer interface : files:///\<PATH_TO_WORKSPACE\>/rocon_webinterfaces/cafe_concert/cafe_viewer/www/index.html
* video demo : http://files.yujinrobot.com/rocon/demos/cafeconcert/cafe_concert.ogv

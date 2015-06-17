
import rospy
from datetime import datetime
import threading
import subprocess
import concert_msgs.msg as concert_msgs
import rocon_gateway_utils

class ClientCatched(Exception):
    def __init__(self, c, s):
        self.client = c
        self.status = s

class ConcertPing(object):

    def __init__(self, machine):
        self._sub = {}
        self._machine = machine

        CONDUCTOR_TOPIC = '/concert/conductor/graph'
        self._sub['concert_clients'] = rospy.Subscriber(CONDUCTOR_TOPIC, concert_msgs.ConductorGraph, self._process_concert_clients)
        self._ping = threading.Thread(target=self._ping_thread)
        self._ping.start()
        self._last_client_status = None

    def _ping_thread(self):
        command = 'ping %s'%self._machine
        self.loginfo("Start %s"%str(command))
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        while not rospy.is_shutdown():
            nextline = proc.stdout.readline()
            if nextline:
                t = nextline.split()[3:] 
                s = ' '.join(str(e) for e in t)
                self.log_ping(s)
        proc.terminate()

    def _process_concert_clients(self, msg):
        client, status = self._get_client(msg)

        if client and status != self._last_client_status:
            self.log_client(client, status)
            self._last_client_status = status

    def _get_client(self, msg):
        try:
            client, status = self._check(msg.pending,   "pending")
            client, status = self._check(msg.bad,       "bad")
            client, status = self._check(msg.blocking,  "blocking")
            client, status = self._check(msg.busy,      "busy")
            client, status = self._check(msg.uninvited, "uninvited")
            client, status = self._check(msg.joining,   "joining")
            client, status = self._check(msg.available, "available")
            client, status = self._check(msg.missing,   "missing")
            client, status = self._check(msg.gone,      "gone")
        except ClientCatched as c: 
            return c.client, c.status
        return None, ""

    def _check(self, client_list, status):
        if not client_list:
            return None, ""

        for c in client_list:
            if rocon_gateway_utils.gateway_basename(c.gateway_name) == self._machine:
                raise ClientCatched(c, status)

        return None, ""


    def log_ping(self, msg):
        s = "[%s][%s] : %s"%(datetime.now(), rospy.Time.now(), str(msg))
        print(s)

    def log_client(self, client, status):
        s = "[%s][%s] : \t\t\t\t\t\t\t\t%s - %s Last Time Seen[%s]"%(datetime.now(), rospy.Time.now(), client.name, status, client.conn_stats.time_since_last_seen)
        print(s)

    def loginfo(self, msg):
        rospy.loginfo("%s : %s"%(rospy.get_name(), str(msg)))

    def spin(self):
        rospy.spin()

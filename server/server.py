#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-19 10:04:30
# @Author  : JohnAlex (843765942@qq.com)
# @Link    : http://taolvezh.cn/
# @Version : $Id$

import socket
import select
import time
from mychatdbbasedriver import my_dbDriver
from myglobal import GlobalVal
from myglobal import *
from handler import ServerHandler


class Server(object):
    """docstring for Server"""

    def __init__(self, host=HOST, port=PORT):
        self.recv_buff = RECV_BUF
        self.listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listen_socket.bind((host, port))
        self.listen_socket.listen(5)

        self.sockets = []
        self.sockets.append(self.listen_socket)
        #userDataLoad()
        print("Server started on " + host + ":" + str(port))
        GlobalVal.server = self

    def clientAppend(self, sock, addr):
        while len(GlobalVal.clients.items()) > MAX_CONNECTION:
            time.sleep(10)
        sock.setblocking(0)
        self.sockets.append(sock)
        # 新建一个连接对象
        client = ServerHandler(sock, addr)
        GlobalVal.clients[sock] = client
        logging.info("Client (%s, %s) connected to server" % addr)
        logging.info("%d client connections in total" %
                     len(GlobalVal.clients.items()))

    def clientRemove(self, sock, addr):
        try:
            try:
                sock.close()
            except Exception as e:
                pass

            if sock in self.sockets:
                self.sockets.remove(sock)

            client = GlobalVal.clients[sock]
            user_Name = client.user_name
            if user_Name != '':
                if user_Name in GlobalVal.login_dict:
                    GlobalVal.login_dict.pop(user_Name)
                try:
                    for key, val in GlobalVal.room_dict.items():
                        if user_Name in val['users']:
                            val['users'].remove(user_Name)
                            if not len(val['users']):
                                GlobalVal.room_dict.pop(key)
                                if key in GlobalVal.clients.keys():
                                    GlobalVal.questions.pop(key)
                                for clientkey in GlobalVal.clients.keys():
                                    clientkey.send(
                                        addHead('s@removeroom %s' % key))
                            else:
                                for user in val['users']:
                                    GlobalVal.login_dict[user].send(
                                        addHead('s@leaveroom %s %s' % (key, user_Name)))
                                if user_Name == GlobalVal.room_dict[key]['admin']:
                                    tempadmin = GlobalVal.room_dict[
                                        key]['users'][0]
                                    GlobalVal.room_dict[key][
                                        'admin'] = tempadmin
                                    for other_online_user in val['users']:
                                        GlobalVal.login_dict[other_online_user].send(
                                            addHead('s@setadmin %s %s' % (key, tempadmin)))
                    if client.start_time != 0:
                        # GlobalVal.user_data[user_Name][
                        #     1] += round(time.time() - client.start_time)
                        newOnlineTime = my_dbDriver.get_onlineTime(username)
                        newOnlineTime += round(time.time() - client.start_time)
                        my_dbDriver.update_onlineTime(user_Name, newOnlineTime)
                    for key in GlobalVal.clients.keys():
                        try:
                            if key != sock:
                                key.send(addHead('s@logout %s' % user_Name))
                        except Exception as e:
                            self.clientRemove(key, GlobalVal.clients[key].addr)
                    # userDataDump()
                except Exception as e:
                    pass
            GlobalVal.clients.pop(sock)
            logging.info("Client (%s, %s) disconnected from server" % addr)
            logging.info("%d client connections in total" %
                         len(GlobalVal.clients.items()))
            # return 1
        except Exception as e:
            logging.error(str(e), exc_info=True)
            logging.info('remove failed, maybe have been removed')
            # return 0

        pass

    def run(self):
        while True:
            try:
                rlist, wlist, elist = select.select(
                    self.sockets, self.sockets, [])
                for rs in rlist:
                    if rs == self.listen_socket:
                        sock, addr = self.listen_socket.accept()
                        self.clientAppend(sock, addr)
                    elif GlobalVal.clients[rs].handleMsg():
                        self.clientRemove(rs, GlobalVal.clients[rs].addr)
            except Exception as e:
                logging.error(str(e), exc_info=True)
        pass


if __name__ == "__main__":
    server = Server()
    server.run()

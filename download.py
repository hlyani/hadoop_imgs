# coding: utf-8

import os

for file in os.listdir(r'/job/hadoop'):
        file = './hadoop/%s' % file

        with open(file) as f:
          lines = f.readlines()


        for line in lines:
            if '//images.handge.cn/' in line:
                _,tmp = line.split('(')
                url,_ = tmp.split(')')

                dict = url.split('/')

                os.system('mkdir %s' % dict[3])
                os.system('curl -o %s %s' %(dict[3] + '/' + dict[4],url))

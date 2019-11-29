import subprocess
import os
process = subprocess.Popen(["sudo chmod +x mf.py", "sudo mv mf.py mf"], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                           shell=True)
stdout, stderr = process.communicate()

hm_dir = os.path.expanduser('~')
os.mkdir(hm_dir + "/mf")

process2 = subprocess.Popen(["sudo mv mf {}".format(hm_dir + '/mf')], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            shell=True)
stdout, stderr = process2.communicate()

process3 = subprocess.Popen(["""echo 'export PATH=$PATH":$HOME/mf"' >> .profile"""], stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, shell=True)
stdout, stderr = process3.communicate()

import subprocess
import os
# process = subprocess.Popen(["sudo chmod +x mf.py", "sudo mv mf.py mf"], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
#                            shell=True)
# stdout, stderr = process.communicate()

hm_dir = os.path.expanduser('~')
#os.mkdir(hm_dir + "/mf")

process2 = subprocess.Popen(["sudo mv mf.py {}".format(hm_dir + '/mf')], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             shell=True)

os.chdir(hm_dir)
with open('.profile', 'a') as profile:
    profile.write('PATH=$PATH":$HOME/mf"')

#process3 = subprocess.Popen(['PATH=$PATH":$HOME/mf"'], stdout=subprocess.PIPE,
#                             stderr=subprocess.PIPE, shell=True)
# stdout, stderr = process3.communicate()

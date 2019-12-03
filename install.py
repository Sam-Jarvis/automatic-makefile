import subprocess
import os

working_dir = os.getcwd()
print('working: ', working_dir)

process = subprocess.Popen(["sudo chmod +x mf.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                           shell=True)

process2 = subprocess.Popen(["sudo mv mf.py mf"], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            shell=True)

hm_dir = os.path.expanduser('~')
print('home: ', hm_dir)
os.mkdir(hm_dir + "/mf")

process3 = subprocess.Popen(["cp mf {}".format(hm_dir + '/mf')], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            shell=True)

os.chdir(hm_dir)
with open('.profile', 'a') as profile:
    profile.write('PATH=$PATH":$HOME/mf"')

process4 = subprocess.Popen(['source .profile'], stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, shell=True)


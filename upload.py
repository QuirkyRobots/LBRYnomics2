import subprocess
import yaml

def upload():
    print("Uploading files.", flush=True)
    subprocess.run("cp plots/*.svg upload", shell=True)
    subprocess.run("cp plots/*.png upload", shell=True)
    subprocess.run("cp json/*.json upload", shell=True)
    subprocess.run("cp /home/brewer/Projects/LBRYnomics/subscriber_stats.json upload", shell=True)

    subprocess.run("mv upload/num_streams.svg upload/claims.svg", shell=True)
    subprocess.run("mv upload/num_streams.png upload/claims.png", shell=True)
    subprocess.run("mv upload/num_channels.svg upload/channels.svg", shell=True)
    subprocess.run("mv upload/num_channels.png upload/channels.png", shell=True)

    f = open("secrets.yaml")
    secrets = yaml.load(f, Loader=yaml.SafeLoader)
    f.close()

    cmd = "sshpass -p \"{p}\" scp -P 21098 upload/* {user}@{dest}"\
            .format(p=secrets["password"], user=secrets["user"],
                    dest=secrets["destination"])
    subprocess.run(cmd, shell=True)
    print("Done.\n")

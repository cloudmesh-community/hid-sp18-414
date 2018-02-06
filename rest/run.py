from eve import Eve
import json
import psutil

guide = "Eve REST\n"\
    "System info that is available:\n"\
    "    all\n    mem\n    disk\n    user\n"\
    "Example: http://127.0.0.1:5000/info/disk "\

print(guide)

app = Eve()


#Format data for output
def output(data):
    format = json.dumps(data, indent=4)+"\n"
    return format


# Returns all information
@app.route('/info/all', methods=['GET'])
def all():
    ALL = {
        "TOTAL RAM": psutil.virtual_memory().total,
        "USED RAM": psutil.virtual_memory().used,
        "AVAILABLE RAM": psutil.virtual_memory().available,
        "TOTAL DISK": psutil.disk_usage('/').total,
        "USED DISK": psutil.disk_usage('/').used,
        "AVAILABLE DISK": psutil.disk_usage('/').free,
        "CPU CORES": psutil.cpu_count(),
        "USED CPU": str(psutil.cpu_percent()) + "%",
        "USER NAME": psutil.users()[0].name,
        "USER TERMINAL": psutil.users()[0].terminal
        }
    return output(ALL)


# Returns USER info
@app.route("/info/user", methods=['GET'])
def user():
    user = {
        "USER NAME": psutil.users()[0].name,
        "USER TERMINAL": psutil.users()[0].terminal
            }
    return output(user)

# Returns RAM info
@app.route('/info/mem', methods=['GET'])
def mem():
    mem = {
        "TOTAL RAM": psutil.virtual_memory().total,
        "USED RAM": psutil.virtual_memory().used,
        "AVAILABLE RAM": psutil.virtual_memory().available
            }
    return output(mem)

# Returns DISK info
@app.route("/info/disk", methods=['GET'])
def disk():
    disk = {
        "TOTAL DISK": psutil.disk_usage('/').total,
        "USED DISK": psutil.disk_usage('/').used,
        "AVAILABLE DISK": psutil.disk_usage('/').free
            }
    
    return output(disk)



if __name__ == '__main__':
    app.run()

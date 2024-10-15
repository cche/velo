# download modsim.py if necessary

from os.path import basename, exists

import matplotlib.pyplot as plt

from modsim import State, TimeSeries, flip


# import functions from modsim
def download(url):
    filename = basename(url)
    if not exists(filename):
        from urllib.request import urlretrieve

        local, _ = urlretrieve(url, filename)
        print(f"Downloaded {local}")


download("https://github.com/AllenDowney/ModSimPy/raw/master/modsim.py")


bikeshare = State(mailly=10, moulin=2,  mecontentement_mailly=0, mecontentement_moulin=0)

# Define the limits for the number of bikes at each station
MAX_MAILLY = 10
MAX_MOULIN = 2



def velo_a_mailly():
    if bikeshare.moulin > 0:
        bikeshare.mailly += 1
        bikeshare.moulin -= 1
    else:
        bikeshare.mecontentement_moulin += 1  # Mécontentement à Moulin


def velo_a_moulin():
    if bikeshare.mailly > 0:
        bikeshare.moulin += 1
        bikeshare.mailly -= 1
    else:
        bikeshare.mecontentement_mailly += 1  # Mécontentement à Mailly


def step(p1, p2):
    if flip(p1):
        velo_a_mailly()

    if flip(p2):
        velo_a_moulin()


def run_simulation(num_steps, p1, p2):
    results = TimeSeries()
    results[0] = bikeshare.mailly
    for i in range(num_steps):
        step(p1, p2)
        results[i] = bikeshare.mailly
    return results


res = run_simulation(10000, 0.5, 0.4)

# Afficher les résultats
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

ax1.plot(res)
ax1.set_title("Vélos à Mailly")
ax1.set_xlabel("Temps")
ax1.set_ylabel("Nombre de vélos")

# Afficher le mécontentement final
mecontentements = [bikeshare.mecontentement_mailly, bikeshare.mecontentement_moulin]
stations = ['Mailly', 'Moulin']

ax2.bar(stations, mecontentements, color=['blue', 'orange'])
ax2.set_title("Mécontentement des utilisateurs")
ax2.set_xlabel("Station")
ax2.set_ylabel("Nombre de mécontentements")

plt.tight_layout()
plt.savefig("simulation_velo.png")
plt.show()

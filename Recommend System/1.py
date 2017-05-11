import random

watershed = ['02050301', '02130608', '02141003', '02141006', '05020201']
year = ['15','16','17']
month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
pollute = range(1, 101)

with open('C:/Users/justi/Desktop/Observation.csv', 'w', encoding="utf8") as f:

    for obid in random.sample(range(1,1500), 1000):
        f.write("('OB" + str(obid) + "',")
        f.write("'" + str(random.choice(watershed)) + "',")
        f.write("'20" + str(random.choice(year)) + str(random.choice(month)) + "',")
        f.write("'WaterPollution',")
        f.write("'" + str(random.choice(pollute)) + "',")
        f.write("'" + str(random.uniform(39.720836, 38.038535)) + "','" + str(random.uniform(-79.490503, -75.155779)) + "'),")
    f.close()


MFName = ['Bridge', 'Springs', 'Statue', 'Tower']

with open('C:/Users/justi/Desktop/ManmadeFeature.csv', 'w', encoding="utf8") as f:

    for mfid in random.sample(range(1,1500), 30):
        f.write("('MF" + str(mfid) + "',")
        f.write("'" + str(random.choice(watershed)) + "',")
        f.write("'" + str(random.choice(MFName)) + "',")
        f.write("'Best Feature You Should Never Miss',")
        f.write("'" + str(random.uniform(39.720836, 38.038535)) + "','" + str(random.uniform(-79.490503, -75.155779)) + "'),")
    f.close()

NFName = ['Waterfall', 'Stream', 'River', 'Forest']

with open('C:/Users/justi/Desktop/NaturalFeature.csv', 'w', encoding="utf8") as f:

    for nfid in random.sample(range(1,1500), 20):
        f.write("('NF" + str(nfid) + "',")
        f.write("'" + str(random.choice(watershed)) + "',")
        f.write("'" + str(random.choice(NFName)) + "',")
        f.write("'Best Feature You Should Never Miss',")
        f.write("'" + str(random.uniform(39.720836, 38.038535)) + "','" + str(random.uniform(-79.490503, -75.155779)) + "'),")
    f.close()
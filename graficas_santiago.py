import pandas as pd
import matplotlib.pyplot as plt
#se convierte el archivo csv a dataframe
df = pd.read_csv("FLGTDT27.CSV")
#modificaciones a la grafica
fig = plt.figure(figsize=(15,20))
fig.tight_layout()
#colores = ["blue","red","white","magenta","green"]
print(df)
print (df['T'])
#time = df['T']
""" period = df["Period(ms)"]
temperature = df["T(degC)"]
presion = df["P(Pa)"]
aceleracion_x = df["a-X(g)"]
aceleracion_y = df["a-Y(g)"]
aceleracion_z = df["a-Z(g)"]
vel_angx = df["w-X (deg/s)"]
vel_angy = df["w-Y (deg/s)"]
vel_angz = df["w-Z (deg/s)"]
angle_x =df["Angle-X (deg)"]
angle_y =df["Angle-Y (deg)"] """

""" plt.subplot(221)
plt.plot(time, temperature, label = "precio", color = "blue")
plt.title("temperatura")
#plt.legend()

plt.subplot(222)
plt.plot(time, presion, label = "cantidad", color = "green")
plt.title("presíon")
#plt.legend()

plt.subplot(223)
plt.plot(time, aceleracion_x, aceleracion_y, aceleracion_z, label = "lead", color = "black")
plt.title("aceleración")
#plt.legend()

plt.subplot(224)
plt.plot(time, vel_angx, vel_angy,vel_angz, label = "velocidad angular", color = "red")
plt.title("velocidad angular")
#plt.legend()

plt.subplot(225)
plt.plot(time, angle_x,angle_y, label = "angle", color = "b")
plt.title("angle")
#plt.legend() """

#plt.show()
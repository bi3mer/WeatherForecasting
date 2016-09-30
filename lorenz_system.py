# Plot of the Lorenz Attractor based on Edward Lorenz's 1963 "Deterministic
# Nonperiodic Flow" publication.
# http://journals.ametsoc.org/doi/abs/10.1175/1520-0469%281963%29020%3C0130%3ADNF%3E2.0.CO%3B2
#
# Note: Because this is a simple non-linear ODE, it would be more easily
#       done using SciPy's ode solver, but this approach depends only
#       upon NumPy.
# 
# Code based off of: http://matplotlib.org/examples/mplot3d/lorenz_attractor.html

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import math
import sys

const_s = 10 # -> approach 2
const_r = 28
const_b = 8.0/3.0

def lorenz(x, y, z, s=const_s, r=const_r, b=const_b):
	x_dot = s*(y - x)
	y_dot = r*x - y - x*z
	z_dot = x*y - b*z
	return x_dot, y_dot, z_dot

def build_system(stepCnt,dt, s=const_s, r=const_r, b=const_b):
	# Need one more for the initial values
	xs = np.empty((stepCnt + 1,))
	ys = np.empty((stepCnt + 1,))
	zs = np.empty((stepCnt + 1,))

	# Minutely modify these to change atmosphere
	xs[0], ys[0], zs[0] = (3., 6., 9.05) 

	# Stepping through "time".
	for i in range(stepCnt):
		# Derivatives of the X, Y, Z state
		x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i], s=s, r=r, b=b)
		xs[i + 1] = xs[i] + (x_dot * dt)
		ys[i + 1] = ys[i] + (y_dot * dt)
		zs[i + 1] = zs[i] + (z_dot * dt)

	return xs, ys, zs

def build_images(stepCnt,dt):
	cnt = 0
	for s in range(const_s*24, 2, -1):
		# maniuplate s to be in boundary
		s = float(s)/24

		# create lorenz system and graph
		xs, ys, zs = build_system(stepCnt,dt,s=s)
		fig = plt.figure()
		ax = fig.gca()
		ax.plot(ys, zs)
		ax.set_xlabel("Y Axis")
		ax.set_ylabel("Z Axis")
		ax.set_title("Lorenz Attractor, s = " + str(s))

		# save result
		file_name = str(cnt)
		if len(file_name) == 1:
			file_name = '00' + file_name
		elif len(file_name) == 2:
			file_name = '0' + file_name

		fig.savefig('LorenzPhotos/' + str(file_name) + '.png')
		
		# close and increment
		plt.close(fig)
		cnt += 1

if __name__ == "__main__":
	if len(sys.argv) >= 2:
		build_images(1000,.01)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 14:03:11 2021
@author: drnaylor
"""
import numpy as np
import random
ra = list(range(0, 500, 1))
random.shuffle(ra)
ar = np.array(ra) * 0.1
ra2 = list(range(0, 100, 1))
random.shuffle(ra2)
ar2 = np.array(ra2) * 0.1
save = np.stack([ar, ar**4 + 3*(ar**2) + 8*ar - 15], axis=-1)
save2 = np.stack([ar2, 0.2*ar2*np.exp(2*ar2)+4*ar2-3], axis=-1)
# np.savetxt("/Users/drnaylor/Desktop/task2.csv", save2, delimiter=",", fmt="%08.5f")
import matplotlib.pyplot as plt
plt.plot(save[:, 0], save[:, 1])
#plt.savefig("/Users/drnaylor/Documents/Uni/PythonCourse/PHY2029/static/images/week2/lecture-worksheet/plt1.png")
plt.figure()
plt.plot(save[:, 0], save[:, 1], "or")
#plt.savefig("/Users/drnaylor/Documents/Uni/PythonCourse/PHY2029/static/images/week2/lecture-worksheet/plt2.png")
pf = np.polyfit(save[:, 0], save[:, 1], 4)
x_fit = np.linspace(-10, 60, 2000)
fit = np.polyval(pf, x_fit)
#def legend(pf):
plt.plot(x_fit, fit, "-k")
plt.legend(["data", ""])
#plt.savefig("/Users/drnaylor/Documents/Uni/PythonCourse/PHY2029/static/images/week2/lecture-worksheet/plt3.png")
plt.figure()
plt.plot(save2[:, 0], save2[:, 1], "or")
#plt.savefig("/Users/drnaylor/Documents/Uni/PythonCourse/PHY2029/static/images/week2/lecture-worksheet/plt4.png")
plt.figure()
plt.semilogy(save2[:, 0], save2[:, 1], "or")
#plt.savefig("/Users/drnaylor/Documents/Uni/PythonCourse/PHY2029/static/images/week2/lecture-worksheet/plt5.png")
plt.figure()
plt.xlim([0, 2])
plt.ylim([-3, 20])
plt.plot(save2[:, 0], save2[:, 1], "or")
#plt.savefig("/Users/drnaylor/Documents/Uni/PythonCourse/PHY2029/static/images/week2/lecture-worksheet/plt6.png")
plt.figure()
def fit(x, a, b, c, d):
    return a*x*np.exp(b*x) + c*x + d
import scipy.optimize as opt
popt, pcov = opt.curve_fit(fit, save2[:, 0], save2[:, 1])
print(popt)
xe_fit = np.linspace(0, 10, 500)
ye_fit = fit(xe_fit, popt[0], popt[1], popt[2], popt[3])
plt.plot(save2[:, 0], save2[:, 1], "or")
plt.plot(xe_fit, ye_fit, "-k")
plt.xlim(None)
plt.ylim(None)
#plt.savefig("/Users/drnaylor/Documents/Uni/PythonCourse/PHY2029/static/images/week2/lecture-worksheet/plt7.png")
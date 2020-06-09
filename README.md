# Galaga with PyMODI

PyMODI is an open source library that uses python to control MODI modules developed by LuxRobo.
<https://github.com/LUXROBO/pymodi>

With a custom-made game console which consists of 5 MODI modules, the game, "Galaga with PyMODI," provides a fully immersive gaming experience to all the gamers around the world.

<p align="center">
    <img src="https://github.com/k2sebeom/pymodi_galaga/blob/master/src/start_screen.JPG" width=200 height=300> 
    <img src="https://github.com/k2sebeom/pymodi_galaga/blob/master/src/game_screen.JPG" width=200 height=300> 
    <img src="https://github.com/k2sebeom/pymodi_galaga/blob/master/src/end_screen.JPG" width=200 height=300> 
</p>

Press button to jump into the world of pymodi - Galaga!!

--------

## Introduction

MODI is a technology of integrable robotic modules developed and produced by a Korean venture company, <a href="https://modi.luxrobo.com/">LuxRobo Co., Ltd.<a>. 

<p align="center">
    <img src="https://modi.luxrobo.com/img/main/friends01.jpg" width=300 height=200>    
</p>

There are several different modules such as speaker, gyro, motor, mic, and infrared sensor, all of which can be controlled by MODI compatible softwares. PyMODI is an open source python library designed to control MODI modules. Galaga_with_PyMODI uses PyMODI library to control a console made by MODI technology.

## Structure

In terms of backend, PyMODI uses two different open-source python libraries.
<ul>
    <li>PyMODI: https://github.com/LUXROBO/pymodi</li>
    <li>PyGame: https://github.com/pygame/pygame</li>
</ul>

PyGame is used to construct a mainframe of the game, and to control the game, the library of PyMODI is used to get inputs from a MODI controller.

The controller of the game is a DIY MODI controller that consists of 5 MODI modules.
<ul>
    <li>Network module</li>
    <li>Speaker module</li>
    <li>Led module</li>
    <li>Gyro module</li>
    <li>Button module</li>
<ul>


Connect all 5 modules to like the following image.

<p align="center">
    <img alt="MODI Controller Image" src="github" width=500 height=500> 
</p>

## How to Play
First, clone the repository to your local device.
    $ git clone https://github.com/k2sebeom/pymodi_galaga.git

Then, you need to download two python libraries.

    $ pip install pymodi
    $ pip install pygame
 
Once you have all the files, prepare your MODI controller, prepared as explained above. Connect the controller to your device, and start the game!

    $ python galaga.py
    

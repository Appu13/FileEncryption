---
title: "FILE ENCRYPTION DOCUMENTATION"
author: [Appu13](https://github.com/Appu13) @pravinn19
---

## INTRODUCTION
This is a project to perform file encryption in python. Since we are amatures at that our codes may not be the bwst or the most optimised but we will keep this repo updated as often as possible. As such there may be errors that have crept in. Do feel to fork this repo, comment or suggest your changes and we will be sure to incorpare them

## ROADMAP OF THE APPLICATION

This application was built using the python 3.7 so it will be able to run on most of the system that has python installed.

### APPLICATION SETUP
The application consist of 4 distinct modules each responsible for one part of the application
    1) Brain 
    2) Conversion
    3) Decryption
    4) Reading files

A detailed use of each of the modules is given below

#### **Brain Module**

Simply put this is the central node of the project the execution starts here and is responsible for calling all the other modules and handling any exception that might come. When starting the project the brain module offers the user a choice as to what they want to perform viz. encryption or decryption. 

It calls the reading files module to perform its tasks. The brain module splits the recieved contents into separate strings so it is easier to process.

Then it supplies the read contents to the respective module to perform its tasks. Any errors that are generated in the modules are passed here where they are handled.

#### **Converstion Module**

This is responsible for reciving the list from the brain and calls the converting function for each of the string present in the recieved list.

It recieves the location to store the contents of the list from the reading files module and then clears the file of the contents which are present in it and then fills it with the encrypted texted.

#### **Decryption Module**

This is responsible fo reciving the list from the brain module and calls the decryptiong modeule for each of the string present in teh recieved list

The storage function in this module functions similar to the conversion module


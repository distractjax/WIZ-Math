# Plan.md

## Overview

* This project is a test prep tool for the math portion of the GRE exam.
* Development will consist of three stages:
  * Stage 1: Terminal Stage
  * Stage 2: Light Webpage
  * Stage 3: Full Webpage

## Stage 1: Terminal Stage

### Terminal Stage Overview

* At this point the entire app will run in the terminal.
* It will need to have a dictionary of problem types that activate different
 functions, generating math problems.
* The way that the math problems will work is that a solution is generated
 first, then the rest of the formula.
* Once the variables and the solution have been generated, they will be fed
 into a local AI prompt that will generate a word problem.
* That word problem will be printed to the terminal, and input will be requested
 from the user.
* If the input matches the variable that's the subject of the question, the
 program will print "Correct", else it will print "Incorrect".

## Stage 2: Light Webpage

### Light Webpage Stage Overview

* Very minimal webpage
* No CSS or style sheet, just a bit of html and javascript
* The math problem will appear in a box on the screen and the solution will
 need to be typed in a box and submitted with a button.
* A history of correct and incorrect questions and answers, with their category,
 will be saved in a sqlite database that can be viewed on another webapage.

## Stage 3: Full Webpage

### Full Webpage Stage Overview

* CSS styling, bells and whistles.
* I don't think I really need an option to make an account.
* Settings page:
  * Can adjust between different CSS themes
  * Can enter AI API key and provider
  * Can set username and password
  * Can export question/answer database
* Buttons and hamburger menu that redirect between pages.
* Option to generate questions like the questions you've gotten wrong.
* Customized study plan.
* Distributed on Docker (and maybe nixpkgs)

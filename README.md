# Chromatic-Storytelling

https://error521-chromatic-storytelling-palettegenerator-s2xol6.streamlitapp.com/

Personal project where I analyze my colour usage in my illustrations and comics

I created this project on a whim back during a public holiday in early 2021. It was just a bunch of Jupyter notebooks with OpenCV K means clustering magic initially. Then I left it there and forgot about it for the most part until I realised I wanted to learn how to deploy a machine learning web application. So I learnt streamlit in one morning and half an afternoon and now it's on the streamlit cloud. Hit the link above to try it out - it's still very barebones but it works.

## Prereq

You need sklearn and the usual data science shenanigans like numpy and matplotlib, and also PIL. I no longer remember if I installed them using conda or pip and it probably doesn't matter much.

```bash
pip install streamlit
```

## Usage

To run the palettegenerator.py as a streamlit application:

```bash
streamlit run palettegenerator.py
```

The notebook included in here is supposed to generate an extremely long barcode like barchart which takes the most dominant colour from each image file in a folder. As you can see from the ArtChromaticStorytelling2022.png I draw way too much. This isn't even my final form. I thought of making this an app too, but I haven't figured out the direction, so it's just going to remain a notebook until I think of something. 

## Extremely quick demo
![](https://github.com/error521/Chromatic-Storytelling/blob/main/2022-09-26_streamlitdemo.gif)

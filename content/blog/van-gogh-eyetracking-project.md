Title: What do people look at when they view a painting?
Slug: van-gogh-eyetracking-project
Date: 2017-02-07 08:39
Category: Research
Tags: Perception, Science, Eye tracking, Art
Authors: Daniel Schreij
Banner: http://www.vupsy.nl/vupsy/wp-content/uploads/2016/09/IMG_2789-e1475228558909-1024x343.jpg
Summary: I was part of this ambitious project in which we used a mobile eye tracker to study what people look at in various van Gogh paintings and shortly describe my experiences.

When you view a particular scene or painting, what areas or objects do you fixate your eyes on? Does everyone look at a painting in a different way, or is there some generic pattern or strategy that most of us follow? These questions have kept cognitive psychologists or perception scientists busy for a while now. Most earlier studies into this topic presented images of paintings to participants on a computer screen, while their gaze was tracked with stationary and often bulky eye trackers. These require participants to sit down and keep their head extremely still, because the slightest head movement can throw off the tracker's calibration. And of course, these types of studies need to take place in a lab, because the eye trackers are not easy to carry around.

This is not really what one would call a natural setting to study viewing behavior in. Normally we have the ability to walk around, and often we also turn our heads in the direction of the things we want to look at. Luckily, light-weight mobile eye trackers have started to hit the market in the last few years and they allow researchers to study participants in less restricted settings. Most of these mobile eye trackers are really expensive (think of $50,000+), but lately some vendors have started to offer options that are quite affordable. One of these is the [Pupil mobile eyetracker](https://pupil-labs.com/pupil/).

![Screenshot]({filename}/images/blog/pupil_eyetracker.jpg){ .center-block .half-width }

Its development started out as a project for a Master's thesis at MIT to see if it was feasible to create a cheap mobile eye tracker with components extracted from webcams, but it eventually led to the establishment of the Berlin-based company [Pupil Labs](https://pupil-labs.com/). The Pupil eye tracker can be purchased for between $1,500 and $2,500 and only weighs around 50 grams. It plugs into a laptop with two usb cables (one for the eye camera and one for the camera filming in the direction the wearer is looking at; the more expensive models have both integrated into one usb-connector). The recording software is open-source, well maintained and free to download. The only thing that currently is missing in my opinion is an officially supported software package that helps with quantitative analysis of the recorded data, but probably that is on the company's roadmap somewhere (In the meantime, I wrote [a small library of my own for this purpose](https://github.com/dschreij/PupilEyetrackerAnalysisTools), but haven't maintained it really well). Pupil does however supply software that allows one to visually inspect the recorded data, [Pupil Player](https://github.com/pupil-labs/pupil/wiki/Pupil-Player), which is great (it borders on sci-fi).

With the pupil eyetracker in our possession at the [Cognitive Psychology department](http://www.vupsy.nl) of the *Vrije* Universiteit of Amsterdam, [Francesco Walker](https://www.utwente.nl/en/et/vvr/staff/walker/) came up with a nice idea for a research project. Besides his interest in human perception, he also likes art, so why not combine the two? His suggestion was to use the Pupil to study how people appreciate visual art, or more specifically, look at paintings. He contacted various museums in Amsterdam to propose this project, but only the [Van Gogh Museum](https://www.vangoghmuseum.nl/en) (seriously, if you ever visit Amsterdam, don't skip it!) responded and was enthusiastic about it.

With our team consisting of Francesco, [Berno Bucker](http://www.vupsy.nl/staff-members/berno-bucker/), [Nicola Andersson](http://www.vupsy.nl/staff-members/nicola-c-anderson/), [Prof. Jan Theeuwes](http://www.vupsy.nl/staff-members/jan-theeuwes/) and me, we came up with the idea to see if and how background knowledge about a painting changes the way it is viewed. So we first let participants free-view each of 5 different van Gogh paintings for 30 seconds, and after this first phase, we told them more about the background of each painting. We then requested participants to view the same five paintings again for the same amount of time; all the time wearing the Pupil eye tracker that registered their gaze. We were also interested if we could find a difference in viewing behavior between young adults recruited at the university and children that were finishing elementary school during the two phases.

Now you might think "of course having knowledge about a painting will change the way someone looks at it" or even that people will simply look differently at a painting when they see it for a second time, and you are probably right, but we were particularly interested if a general pattern emerged during second viewing round that was shared by most participants. For instance, if it was told that Van Gogh painted a particular painting while he was heavily depressed, would most participants pay more attention to areas or objects on the painting that may signal his mood, such as cloudy or dark skies?

The study was challenging to perform, especially since we had to conduct it during the normal opening hours of the museum, while a lot of museum visitors were around that were very intrigued by what we were doing. Luckily this didn't negatively influence data collection and we found some interesting results. In the first phase, the viewing behavior of the children was driven more by properties of the scene, while the adults showed viewing behavior was more goal-driven. So the adults tried to find a purpose to view the paintings with, while the children just looked at areas in the painting that were more salient or conspicuous. In the second phase, the viewing behaviors converged; both groups were looked at the paintings in a more goal-driven fashion.

Here is a demo video of the study that also shows the abilities of the Pupil Player quite nicely:

<div class="embed-responsive embed-responsive-16by9">
<iframe class="embed-responsive-item" src="https://www.youtube.com/embed/0_KaItdTkEM?rel=0" allowfullscreen></iframe>
</div>

<br/>
For those who'd like to know more: a paper about this study has been submitted and is currently under review. Once (if...) it gets published, I will try to link it here.






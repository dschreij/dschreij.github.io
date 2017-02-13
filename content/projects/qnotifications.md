Title: QNotifications
Slug: qnotifications
Category: projects
Authors: Daniel Schreij
Date: 2016-07-03 21:56
Image: http://cdn1.tnwcdn.com/wp-content/blogs.dir/1/files/2014/04/Notifications.jpg
Banner: http://cdn1.tnwcdn.com/wp-content/blogs.dir/1/files/2014/04/Notifications.jpg
Summary: Pretty in-app notifications in PyQt4/5
Githublink: https://github.com/dschreij/QNotifications
Doclink: http://dschreij.github.io/QNotifications

QNotifications brings pretty in-app notifications to PyQt (4 and 5). We are nowadays  used to seeing such notifications in many web applications (see [sAlert](http://s-alert-demo.meteorapp.com) for example), but functionality like this was still lacking in PyQt. QNotifications aims to provide a system that can easily be plugged into existing PyQt projects and can project several types of notifications (info, errors, warnings, etc.) on top of other items. To integrate this module into existing applications just pass it a widget on top of which it should render the notifications.

This project is still in the starting blocks and does not offer many options for customisation yet. Notifications are always positioned at the top of the target widget and take up the whole width (with a margin). The only currently supported animation style is fading (in and out). In the future, more options will be added, but for now I have just focussed on maximizing the stability of this module.

Here is an example of what it looks like:

![Screenshot]({filename}/images/projects/QNotificationScreenshot.png)

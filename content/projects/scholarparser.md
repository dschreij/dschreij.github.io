Title: Google Scholar parser
Slug: scholar-parser
Category: projects
Authors: Daniel Schreij
Date: 2016-07-11 21:56
Image: http://www.oliversacks.com/os/wp-content/uploads/2015/04/DSC_6976-opt.jpg
Banner: http://www.oliversacks.com/os/wp-content/uploads/2015/04/DSC_6976-opt.jpg
Summary: A parser for Google Scholar profile pages
Githublink: https://github.com/dschreij/scholar_parser
Doclink: http://dschreij.github.io/scholar_parser

Scholar parser is a PHP library which extracts data from profile pages of Google scholar. It simply needs to be supplied the id of user of which to parse the page and then returns the data in JSON format. The publications can be sorted by number of citations or year or publication. It furthermore retrieves stats about the user, such as the H-index, i10-index or total number of citations.

Scholar parser uses Phantom.js as a headless browser to deal with any javascript that migth be present on the scholar source page. It furthermore implements a basic caching mechanism, to prevent it from flooding the Google Scholar server with requests each time the script is used (the default cache duration is 3 days).

To see a working demo of this library, visit the website of the [Department of Experimental and Applied Psychology](http:/www.vupsy.nl) of the *Vrije* Universiteit of Amsterdam, where scholar parser is used to populate the list of publications of each department member.
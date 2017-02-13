Title: Datamerger
Slug: datamerger
Category: projects
Authors: Daniel Schreij
Date: 2016-07-21 17:36
Image: /images/projects/DatamergerHeader.jpg
Banner: /images/projects/DatamergerHeader.jpg
Summary: GUI tool for merging tabular data of various formats
Githublink: https://github.com/dschreij/Datamerger

Datamerger is a small tool built with [PyQt](https://riverbankcomputing.com/software/pyqt/intro) that can merge separate spreadsheets into one large spreadsheet. While doing so, it takes column names into account, and therefore can correct for small inconsistenties between the spreadsheets to be merged (e.g. different column order, missing columns in some sheets). It is therefore important that each file to be merged contains a header, which is a row of textual labels at the top each column to identify the data in the rows below. Datamerger can read and write several formats: comma separated value lists (.csv), Excel 97-2003 (.xls) and Excel 2007 and higher (.xlsx)

![Datamerger]({filename}/images/projects/DatamergerScreenshot.png)

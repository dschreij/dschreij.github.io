Title: Creating a Mac OS X app from an anaconda environment
Slug: package-anaconda-environments-as-apps
Date: 2017-02-06 08:39
Category: How-to
Tags: Anaconda, Python, Mac OS X, Packaging
Authors: Daniel Schreij
Banner: /images/blog/apple-gear.jpg
Summary: This short guide describes a way to package a Python program as a Mac OS X app using environments in the Anaconda Python distribution.

Once you have created an application that you regard as useful to the larger public, you probably want to package it as a distributable. This enables users to simply install your program on their system without having the hassle of setting up an environment with all dependency libraries that your app requires to run. These should all be packaged together with your program in the distributable package. On the Mac distibutables are often provided as apps compressed in disk images (.dmg files), on Windows they often are a single-file installer (.exe, .msi, etc). Distributables can make the life of people (especially the less tech-savvy ones) who want to use your program a lot easier.

Many programming languages offer out-of-the-box tools for creating distributables, but not Python, which is in its essence not designed to be packaged. Programs such as [py2exe](http://www.py2exe.org/) (for windows), [py2app](https://pythonhosted.org/py2app/) (for Mac) or [PyInstaller](http://www.pyinstaller.org/) (for both) have been created to get this job done, and even though they often do it well, they also frequently break down, spitting out cryptical error messages that in no way helped me solving the problems that they were bumping into. Especially when your package needs to contain more complex libraries such as PyQt, the chance of breakage increases dramatically.

Another promising candidate is [pyqtdeploy](http://pyqt.sourceforge.net/Docs/pyqtdeploy/) but I found it really complex to set up when I gave it a try (although admittedly, I haven't really spent a lot of time on it yet). As I understand it, pyqtdeploy creates a distributable by building everything completely from source (even the python interpreter itself). It converts all python modules to C++ code, so that everything can be compiled to a native application. This makes it possible to also deploy your app to platforms such as Android and iOS. Of course, this is only useful if you use PyQt in your application to begin with, so for smaller, simpler apps using this method seems to be overkill.

I was curious if I could find another, very simple, solution for packaging Python apps and I found it in [Anaconda](https://www.continuum.io/downloads) (or [Miniconda](http://conda.pydata.org/miniconda.html) which is the slimmed down version). For those who don't know Anaconda: it is a science-focused Python distribution created by [Continuum.io](https://www.continuum.io/) that has an extensive set of tools to install and manage Python packages (like pip, but better in my opinion). One of the other major strenghts of Anaconda is the easiness with which you can create and manage virtual environments. Each of these virtual environments should in fact be regarded as a small independent anaconda installation by itself. The biggest plus is that *most* of the libraries that Python apps depend on are contained in the environment; not only the Python interpreter itself, but also non-Python ones such as Qt, sqlite, OpenSSL, you name it. Anaconda environments are already isolated from the rest of the OS and only marginally depend on external libraries; often only low-level libraries that are provided by the OS itself. In a sense, Anaconda environments are already half-way being a distributable. 

Below I describe how to perform the last step of transforming an Anaconda environment into a fully working Mac OS X app, and this is easier than you might think. As an example, I use my own experience of creating an app for the [OpenSesame experiment builder](http://osdoc.cogsci.nl) with this method. Needless to say, you'll have to change all references to OpenSesame to ones applicable to your own project.

A **small disclaimer** before we start: This way of creating an app will work, but it probably violates *all* rules that Apple poses for an app to be allowed into the app store. If you want your app to eventually end up there, you will have to make sure it adheres to [Apple's guidelines](https://developer.apple.com/app-store/review/guidelines/), regarding sandboxing, code signing, and so on. I have never tried passing the App Store review process with an app created the way I describe here, so I can't say at which points it violates the guidelines, but I highly doubt the app would be accepted without quite some extra work.

## Create an Anaconda environment and add your app

When anaconda or miniconda is installed on your system, you should have access to the `conda` command from your terminal. You should be able to create a new environment like this:

~~~
conda create -n OpenSesame python
~~~

Choose `y` when you are asked to install the listed packages. I am not going to dive into the specifics of creating virtual environments with conda (more about that can be found [here](http://conda.pydata.org/docs/using/envs.html)), but suffice to say that the above command creates a new environment with the name _OpenSesame_ (specified after the -n flag) and installs python and its dependencies as the only packages in it. If your program has more dependencies, [this is how you can install them using conda](http://conda.pydata.org/docs/using/pkgs.html).

The next step is to add your program/python module to the environment. You have two options for doing so. 

The first option is to simply copy your home-cooked python module somewhere into the environment folder, preferably the root. Anaconda environments are located in the `envs` subfolder of your main anaconda folder, which in turn can usually be found inside your home folder. For example, if you have created an environment named `MyEnv`, you will find it at `~/anaconda/envs/MyEnv` (or `~/miniconda/envs/MyEnv`). Once you have copied the folder containing your program's files into this environment, you are done for this step.

The second option that is cleaner and more elegant (you wouldn't say I have a preference would you?) is to create a setup.py script for your app that, when run with `python setup.py install`, installs your program's componentes at the conventional places in the environment. Instructions on how to create such a setup script can be found [in the Python documentation](https://pythonhosted.org/an_example_pypi_project/setuptools.html) or [here](http://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/quickstart.html).

To get back to our OpenSesame example, a simplified version of its setup.py script looks like:

~~~python

setup(name=u"python-opensesame",
    # ... Ommitted for brevity ...
    scripts=['opensesame', 'opensesamerun'],
    # ... Ommitted for brevity ...
    packages=[
        "openexp",
        "libopensesame",
        "libqtopensesame",
        ],
    # ... Ommitted for brevity ...
    )
~~~

You can find the full version [here](https://github.com/smathot/OpenSesame/blob/master/setup-mac.py) if you'd rather see that. 

The important variables here are `packages`, which contains the folders of your module that will be copied to the site-packages folder of python in your environment, and `scripts` which contains the files with which your program (or parts thereof) can be started (i.e. the entry point of your program). The files specified at `scripts` will be copied to the bin/ folder of the anaconda environment. 

To give an example, the OpenSesame entry point script merely contains:

~~~python
#!/usr/bin/env python
#-*- coding:utf-8 -*-
if __name__ == "__main__":
    from libqtopensesame import __main__
    __main__.opensesame()
~~~

You might have noticed the `.py` extensions are missing from files that we specified at `scripts`. By specifying `#!/usr/bin/env python` at the very first line of the file, your OS recognizes it as a python file even if you leave away the `.py` extension.

Don't forget to activate your environment before you install your app. Otherwise your app will install into the main anaconda installation. You can activate environments by calling the `source activate <environment-name>` command. For example:

~~~
source activate OpenSesame
~~~

If all goes well, a `[OpenSesame]` label should be prepended in front of your terminal prompt. Now you can call:

~~~
python setup.py install
~~~

to install everything. If you want to exit the virtual environment again, you can do so by simply calling

~~~
source deactivate
~~~

After this step, the environment plus your app are ready to be packaged into an OS X app. 

## Create the .app framework

You wouldn't know unless you are a (fanatic) terminal user, but a Mac OS X app is nothing more than a folder that has .app as extension. The internal structure and contents of this folder are bound to some specifications: 

1. One thing that always needs to be there is the **Contents/MacOS** folder which contains the script or executable file that starts your application. The name of this file should be the same as the one of your app, minus the .app extension.
2. An *Info.plist* file, located at **Contents/Info.plist**, which contains extra information about the app (author, version, etc.), If this file is not present when the app is started for the first time, MacOS will create a default one for you, but it is so generic that it often leaves much to be desired.
3. A **Contents/Resources** folder, which contains all other files your app depends on, such as images or sounds, but they can be virtually anything, such as a complete anaconda environment, as you will see.

So, the basic structure of our OpenSesame app looks like this:

~~~ bash
OpenSesame.app/
    Contents/
        MacOS/
            OpenSesame
        Info.plist
        Resources/
~~~

We'll leave these two files (OpenSesame and Info.plist) empty for now.

Not to sound pedantic, but be sure to create the .app folder at a different location than inside the Anaconda environment you are going to package.

## Copy the Anaconda environment

Now that you have the app skeleton all set up, you can copy the anaconda environment into it. You can copy the contents of the environment folder entirely to the `Resources` folder of your app. In our example case, I also named my virtual environment _OpenSesame_, which resulted in the command:

~~~
cp -R ~/anaconda/envs/Opensesame/* ~/app-output/OpenSesame.app/Contents/Resources/
~~~

where app-output is the folder in which I created the app skeleton for the OpenSesame.app in this example. You can of course also just drag and drop all files using Finder if you like, although it skips hidden files and folders, so the safest way is to just copy everything using the `cp` command in the terminal (although hidden items are not really used in anaconda environments as far as I know).

If everything went ok, your app structure should look like this:

~~~ bash
OpenSesame.app/
    Contents/
        MacOS/
            OpenSesame
        Info.plist
        Resources/
            bin/
            conda-meta/
            imports/
            include/
            lib/
            mkspecs/
            plugins/
            python
            share/
            ssl/
~~~

There might be some deviations, because a few conda packages can install some of their dependencies at the root level of the environment, or things have changed in conda versions that were released later than this article. Furthermore, the folder containing your apps modules should also be present if you have chosen option 1 of integrating your app into the environment (i.e. copy everything directly into the environment, instead of using setup script). Thus, if things look a little bit differently than shown above, don't fret: as long as you have copied all content of the target environment's folder, you should be ok.

Now everything is placed where it should be, there are two things left to do.

## Create the app's entry script

At this point, it is time to write the contents of the executable in *Contents/MacOS*, in this example case *Contents/MacOS/OpenSesame*. This will be a simple bash script that calls the Python interpreter inside the anaconda environment that you just copied, and passes it the path to the entry point  of your program as an argument. So if you chose option one to integrate your program into the Anaconda environment, the contents should look (something) like this:

~~~bash
#!/usr/bin/env bash
script_dir=$(dirname "$(dirname "$0")")
$script_dir/Resources/bin/python $script_dir/Resources/MyApp/myapp.py $@
~~~

The second line simply saves the location of your *Contents* folder by going up a folder (we are in Contents/MacOS now). The third line calls the python interpreter inside the .app from this location, with your program's entry-point script as an argument. The `$@` at the end of this line is supposed to pass all other command line arguments to your script as well, but this hasn't worked for me. Most likely OS X wraps extra arguments with a `--args` flag, but I'm not sure.

If you installed the app using a `setup.py` script, you should let this argument point to your entry script in the bin/ folder. In the context of our example OpenSesame app, this would become:

~~~bash
#!/usr/bin/env bash
script_dir=$(dirname "$(dirname "$0")")
$script_dir/Resources/bin/python $script_dir/Resources/bin/opensesame $@
~~~

Of course you need to replace `opensesame` with the name of your program.

Don't forget to make the entry script _executable_ by issuing the command

~~~bash
chmod a+x <extecutable_file>
~~~

so in our example case that would be the command

~~~bash
chmod a+x OpenSesame.app/Contents/MacOS/OpenSesame
~~~

from the folder in which OpenSesame.app is located.

You can already try out if it works, by double-clicking your app in finder, or starting the app from the command line by issuing the command

~~~
OpenSesame.app/Contents/MacOS/OpenSesame
~~~

from the terminal, with the current working directory being te folder in which the .app is located. This is useful for debugging, for instance if your app seems to launch but closes shortly after with no further notification. When started from the terminal, any error output is printed there.

## Create the contents of Info.plist

A Mac OS X app is required to have an `Info.plist` file, which contains extra information about the app, such as its version, author, and so on. There are a couple of fields that are mandatory, but a lot of them are optional. You'll do yourself a favor however to put as much information about your app in the Info.plist as you can. For instance, if you specify the file extensions that your app can handle (not mandatory), OS X will automatically let these filetypes be opened by your app if a user double clicks such files in Finder (although I have neither had much success with this: my app starts, but the file is not loaded. Probably this is because OS X works with events that signal a file needs to be opened, instead of passing the path simply as a command line argument on opening). If the extension is not unique to your app, it will appear in the list of apps that could open the file, if you click on it and select "Open With" in Finder. Pretty neat.

Don't be fooled by the .plist extension; it is just an .xml file that you can open with any text editor. Here is what the one I generated for OpenSesame looks like:

~~~xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleDevelopmentRegion</key>
    <string>en</string>
    <key>CFBundleDisplayName</key>
    <string>OpenSesame</string>
    <key>CFBundleDocumentTypes</key>
    <array>
        <dict>
            <key>CFBundleTypeIconFile</key>
            <string>opensesame.icns</string>
            <key>CFBundleTypeName</key>
            <string>OpenSesame experiment</string>
            <key>CFBundleTypeRole</key>
            <string>Editor</string>
            <key>LSHandlerRank</key>
            <string>Owner</string>
            <key>LSItemContentTypes</key>
            <array>
                <string>nl.cogsci.osdoc.osexp</string>
            </array>
            <key>NSExportableTypes</key>
            <array>
                <string>nl.cogsci.osdoc.osexp</string>
            </array>
        </dict>
    </array>
    <key>CFBundleExecutable</key>
    <string>OpenSesame</string>
    <key>CFBundleIconFile</key>
    <string>opensesame.icns</string>
    <key>CFBundleIdentifier</key>
    <string>nl.cogsci.osdoc</string>
    <key>CFBundleInfoDictionaryVersion</key>
    <string>6.0</string>
    <key>CFBundleName</key>
    <string>OpenSesame</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
    <key>CFBundleShortVersionString</key>
    <string>3.1.6</string>
    <key>CFBundleSignature</key>
    <string>????</string>
    <key>CFBundleVersion</key>
    <string>3.1.6 Jazzy James</string>
    <key>LSMinimumSystemVersion</key>
    <string>10.7.0</string>
    <key>LSUIElement</key>
    <false/>
    <key>NSAppTransportSecurity</key>
    <dict>
        <key>NSAllowsArbitraryLoads</key>
        <true/>
    </dict>
    <key>NSHighResolutionCapable</key>
    <true/>
    <key>NSHumanReadableCopyright</key>
    <string>© 2017 Sebastiaan Mathôt</string>
    <key>NSMainNibFile</key>
    <string>MainMenu</string>
    <key>NSPrincipalClass</key>
    <string>NSApplication</string>
    <key>UTExportedTypeDeclarations</key>
    <array>
        <dict>
            <key>UTTypeConformsTo</key>
            <array>
                <string>org.gnu.gnu-zip-archive</string>
            </array>
            <key>UTTypeDescription</key>
            <string>OpenSesame experiment</string>
            <key>UTTypeIdentifier</key>
            <string>nl.cogsci.osdoc.osexp</string>
            <key>UTTypeTagSpecification</key>
            <dict>
                <key>public.filename-extension</key>
                <string>osexp</string>
                <key>public.mime-type</key>
                <string>application/gzip</string>
            </dict>
        </dict>
    </array>
</dict>
</plist>

~~~

Each configurable option consists of variable name between the `<key>` tags, and its value between the `<string>` tags. There are a lot of options (most of which have self-explanatory variable names), so I'm not going to elaborate on them any further here. You can find a full list of options and their descriptions [at Apple's documentation site](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.html#//apple_ref/doc/uid/TP40009249-SW1). The ones that you definitely want to specify are the entries that correctly identify your app (`CFBundleName`, `CFBundleDisplayName`, `CFBundleVersion`, `CFBundleShortVersionString`) and the ones that identify you as the author of the app (`NSHumanReadableCopyright`, `CFBundleIdentifier`). If you don't want the name of the executable to be the same as that of the app (I can't think of any reason), you can specify a different name with `CFBundleExecutable`. The final field that you probably want to specify is `CFBundleIconFile`, which specifies the path to your icon file (.icns) as resolved from the Resources folder. If you eventually want to get your app into the app store, it's a start to make sure that your icon has the required minimal resolution of 1024x1024px.

There is a python-based tool called [biplist](https://bitbucket.org/wooster/biplist) which makes generating and editing .plist files a lot easier, so that may be worth a look too.

## Clean up (optional)

Of course, there are some files that we don't need when the anaconda environment is packaged inside our app, so the next step will be removing those files. This step is entirely optional. The risk of actually breaking things is quite large, because I'm not 100% certain that all files and folders I remove here are never needed (but this action never broke my apps though, so that might be regarded a small reassurance). Nevertheless, removing unnecessary item can reduce the size of your app quite a bit, so it is probably worth experimenting with.

Let's start with the /bin folder. If you navigate into this folder inside the Resources folder of the app, you will see that there are a lot of other apps and excutables there; some of which have a considerable file size. Generally you won't need the majority of the files you find here (except the ones necessary to run Python of course), but to be safe I usually leave most of them in there and just focus on the really large files which blow up the size of the app. If your app has Qt as a dependency, you are free to delete all the qt apps that you find in the bin folder (an .app inside in .app is completely useless), in addition to large non-app executables such as `qmake`, `qdoc3`, `qt3to4`.

Next, we are going to delete all files an folders that are only relevant when you are using anaconda to build Python modules or 'conda packages', which you probably are not going to do when the evironment is encapsulated in an app. Two of such folders are `mkspecs` (build information for qt) and `include` (C header files of modules present in the environment). The other one is `conda-meta`. If you remove these folders, you are left with

~~~ bash
OpenSesame.app/
    Contents/
        MacOS/
            OpenSesame
        Info.plist
        Resources/
            bin/
            imports/
            lib/
            plugins/
            python
            share/
            ssl/
~~~

Possibly you could slim down your package even further, but that is up to you. The remaining files and folders probably are not really that large, so it's likely not the effort to spend too much time on this.

## Le moment suprême

That's all there is to it. Double click the app in Finder and see if it works. If nothing happened, or you receive an error message, you can always start your app from the terminal and see if it prints any error message there:

~~~bash
~/app-output/OpenSesame.app/Contents/MacOS/OpenSesame
~~~

Your app should now be up and running. I'm curious what you think of this transparent and easy, but very unconventional way of creating an app.

## Why not create a script for all this?

Well, I have. You can find a (configurable and customizable) script that does everything described above (and more) [on github](https://github.com/dschreij/anaconda-env-to-osx-app). In the future, I hope to provide better documentation on its usage soon (famous last words...), but at the moment it is still evolving too quickly and changes a lot each time I work on it. You should therefore regard the script as a 'proof of concept' and working example than something that is directly ready to use.


Title: Stanford Dogs Dataset, Flutter, Dart, and Java 
Date: 2019-10-13 20:00
Category: Mobile Dev
Tags: mobile, app, android, linux
Slug: stanford-dogs-dataset-flutter-dart-java
Author: Tom Ordonez
Status: published
Summary: Exploring data about dogs. Thoughts about Flutter, Dart, and Java.

I thought of building an app about dogs, where the interface is swiping pictures of dogs.

A quick search for 'dog pictures dataset' turned to this result...

## Stanford Dogs Dataset

[Stanford Dogs Dataset](http://vision.stanford.edu/aditya86/ImageNetDogs/)

I downloaded these files:

* images.tar
* annotations.tar
* lists.tar

The file `lists.tar` had these files:

* file_list.mat
* test_list.mat
* train_list.mat

I created a new `conda` environment to open the mat files:

    conda create --name dogs scipy

Loaded the data with:

    import scipy.io
    data = scipy.io.loadmat('file_list.mat')

Here is a sample of the data:
    
    'annotation_list': array([[array(['n02085620-Chihuahua/n02085620_10074'], dtype='<U35')],
       [array(['n02085620-Chihuahua/n02085620_10131'], dtype='<U35')],
       [array(['n02085620-Chihuahua/n02085620_10621'], dtype='<U35')],
       ...,
       [array(['n02116738-African_hunting_dog/n02116738_9829'], dtype='<U44')],

I also opened the `images.tar` and found the files that corresponded to the data above:

    n02085620-Chihuahua/n02085620_10131
    n02085620-Chihuahua/n02085620_10621
    n02116738-African_hunting_dog/n02116738_9829

This is the content of `annotations.tar` for the first file above:

    <annotation>
        <folder>02085620</folder>
        <filename>n02085620_10131</filename>
        <source>
                <database>ImageNet database</database>
        </source>
        <size>
                <width>395</width>
                <height>495</height>
                <depth>3</depth>
        </size>
        <segment>0</segment>
        <object>
                <name>Chihuahua</name>
                <pose>Unspecified</pose>
                <truncated>0</truncated>
                <difficult>0</difficult>
                <bndbox>
                    <xmin>49</xmin>
                    <ymin>9</ymin>
                    <xmax>393</xmax>
                    <ymax>493</ymax>
                </bndbox>
        </object>
    </annotation>

## From Flutter/Dart to Java

I studied Flutter and Dart for about a month. This is a great stack. However, I wanted to build knowledge that could be used for something other than just building an Android app. I am sure that Dart can be used for other types of applications. However, Java is still used for pretty much everything.

I dropped Flutter/Dart and decided to move forward with Java to build a few simple Android apps.

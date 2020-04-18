<br>

<title>[Auto]Stitching Photo Mosaics</title>

<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <!-- common.css -->
  <style>* {-webkit-tap-highlight-color: rgba(0,0,0,0);}html {-webkit-text-size-adjust: none;}body {font-family: -apple-system, Helvetica, Arial, sans-serif;margin: 0;padding: 20px;color: #333;word-wrap: break-word;}h1, h2, h3, h4, h5, h6 {line-height: 1.1;}img {max-width: 100% !important;height: auto;}blockquote {margin: 0;padding: 0 15px;color: #777;border-left: 4px solid #ddd;}hr {background-color: #ddd;border: 0;height: 1px;margin: 15px 0;}code {font-family: Menlo, Consolas, 'Ubuntu Mono', Monaco, 'source-code-pro', monospace;line-height: 1.4;margin: 0;padding: 0.2em 0;font-size: 90%;background-color: rgba(0,0,0,0.04);border-radius: 3px;}pre > code {margin: 0;padding: 0;font-size: 100%;word-break: normal;background: transparent;border: 0;}ol {list-style-type: decimal;}ol ol, ul ol {list-style-type: lower-latin;}ol ol ol, ul ol ol, ul ul ol, ol ul ol {list-style-type: lower-roman;}table {border-spacing: 0;border-collapse: collapse;margin-top: 0;margin-bottom: 16px;}table th {font-weight: bold;}table th, table td {padding: 6px 13px;border: 1px solid #ddd;}table tr {border-top: 1px solid #ccc;}table tr:nth-child(even) {background-color: #f8f8f8;}input[type="checkbox"] {cursor: default;margin-right: 0.5em;font-size: 13px;}.task-list-item {list-style-type: none;}.task-list-item+.task-list-item {margin-top: 3px;}.task-list-item input {float: left;margin: 0.3em 1em 0.25em -1.6em;vertical-align: middle;}#tag-field {margin: 8px 2px 10px;}#tag-field .tag {display: inline-block;background: #cadff3;border-radius: 4px;padding: 1px 8px;color: black;font-size: 12px;margin-right: 10px;line-height: 1.4;}</style>
  <!-- ace-static.css -->
  <style>.ace_static_highlight {white-space: pre-wrap;}.ace_static_highlight .ace_gutter {width: 2em;text-align: right;padding: 0 3px 0 0;margin-right: 3px;}.ace_static_highlight.ace_show_gutter > .ace_line {padding-left: 2.6em;}.ace_static_highlight .ace_line {position: relative;}.ace_static_highlight .ace_gutter-cell {-moz-user-select: -moz-none;-khtml-user-select: none;-webkit-user-select: none;user-select: none;top: 0;bottom: 0;left: 0;position: absolute;}.ace_static_highlight .ace_gutter-cell:before {content: counter(ace_line, decimal);counter-increment: ace_line;}.ace_static_highlight {counter-reset: ace_line;}</style>
  <style>.ace-chrome .ace_gutter {background: #ebebeb;color: #333;overflow : hidden;}.ace-chrome .ace_print-margin {width: 1px;background: #e8e8e8;}.ace-chrome {background-color: #FFFFFF;color: black;}.ace-chrome .ace_cursor {color: black;}.ace-chrome .ace_invisible {color: rgb(191, 191, 191);}.ace-chrome .ace_constant.ace_buildin {color: rgb(88, 72, 246);}.ace-chrome .ace_constant.ace_language {color: rgb(88, 92, 246);}.ace-chrome .ace_constant.ace_library {color: rgb(6, 150, 14);}.ace-chrome .ace_invalid {background-color: rgb(153, 0, 0);color: white;}.ace-chrome .ace_fold {}.ace-chrome .ace_support.ace_function {color: rgb(60, 76, 114);}.ace-chrome .ace_support.ace_constant {color: rgb(6, 150, 14);}.ace-chrome .ace_support.ace_type,.ace-chrome .ace_support.ace_class.ace-chrome .ace_support.ace_other {color: rgb(109, 121, 222);}.ace-chrome .ace_variable.ace_parameter {font-style:italic;color:#FD971F;}.ace-chrome .ace_keyword.ace_operator {color: rgb(104, 118, 135);}.ace-chrome .ace_comment {color: #236e24;}.ace-chrome .ace_comment.ace_doc {color: #236e24;}.ace-chrome .ace_comment.ace_doc.ace_tag {color: #236e24;}.ace-chrome .ace_constant.ace_numeric {color: rgb(0, 0, 205);}.ace-chrome .ace_variable {color: rgb(49, 132, 149);}.ace-chrome .ace_xml-pe {color: rgb(104, 104, 91);}.ace-chrome .ace_entity.ace_name.ace_function {color: #0000A2;}.ace-chrome .ace_heading {color: rgb(12, 7, 255);}.ace-chrome .ace_list {color:rgb(185, 6, 144);}.ace-chrome .ace_marker-layer .ace_selection {background: rgb(181, 213, 255);}.ace-chrome .ace_marker-layer .ace_step {background: rgb(252, 255, 0);}.ace-chrome .ace_marker-layer .ace_stack {background: rgb(164, 229, 101);}.ace-chrome .ace_marker-layer .ace_bracket {margin: -1px 0 0 -1px;border: 1px solid rgb(192, 192, 192);}.ace-chrome .ace_marker-layer .ace_active-line {background: rgba(0, 0, 0, 0.07);}.ace-chrome .ace_gutter-active-line {background-color : #dcdcdc;}.ace-chrome .ace_marker-layer .ace_selected-word {background: rgb(250, 250, 255);border: 1px solid rgb(200, 200, 250);}.ace-chrome .ace_storage,.ace-chrome .ace_keyword,.ace-chrome .ace_meta.ace_tag {color: rgb(147, 15, 128);}.ace-chrome .ace_string.ace_regex {color: rgb(255, 0, 0)}.ace-chrome .ace_string {color: #1A1AA6;}.ace-chrome .ace_entity.ace_other.ace_attribute-name {color: #994409;}.ace-chrome .ace_indent-guide {background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAE0lEQVQImWP4////f4bLly//BwAmVgd1/w11/gAAAABJRU5ErkJggg==") right repeat-y;}</style>
  <!-- export.css -->
  <style>
    body{margin:0 auto;max-width:1200px;line-height:1.4}
    #nav{margin:5px 0 10px;font-size:15px}
    #titlearea{border-bottom:1px solid #ccc;font-size:17px;padding:10px 0;}
    #contentarea{font-size:15px;margin:16px 0}
    .cell{outline:0;min-height:20px;margin:5px 0;padding:5px 0;}
    .code-cell{font-family:Menlo,Consolas,'Ubuntu Mono',Monaco,'source-code-pro',monospace;font-size:12px;}
    .latex-cell{white-space:pre-wrap;}
  </style>
  <!-- User CSS -->
  <style> .text-cell {font-size: 15px;}.code-cell {font-size: 12px;}.markdown-cell {font-size: 15px;}.latex-cell {font-size: 15px;}</style>
  <script type='text/x-mathjax-config'>MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$']]}});</script>
  <script type='text/javascript' src='http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML'></script>


</head>


# [Auto]Stitching Photo Mosaics

## Project 5, CS 194-26, Spring 2020

**by Suraj Rampure (`suraj.rampure@berkeley.edu`, `cs194-26-adz`)**


---

In the first half of this project, we create homographies between images, in order to warp one to be in the perspective of another. After doing this, we are able to stitch these images together using a mask, creating a panorama-type effect. In the second half, we automate the process of picking correpondences between the images.

---

## Part A: Image Warping and Mosaicing

### `homography(pts1, pts2)`, `warp_image(im, H)`

The first step is to create a homography between points in one image and points in another. Specifically, we want to find some 3 x 3 matrix $H$ such that maps $p = [x, y, 1]^T$ in image 1 to $p' = w \cdot [x', y', 1]$ in image 2. 

We want to minimize the loss created by our homography. Specifically, we want to minimize 

<img src='loss.png' width = 300>


An equivalent formulation, using the same constants in H, can be written as follows:

<img src='ahb.png' width = 400>

The above equation is of the form Av = b; solving for v using least squares gives us estimates of the values of a, b, c, d, e, f, g, h.

Now that we have the values of these 8 constants (and hence, know the 3 x 3 matrix H), we can warp points in one image to those in another using the specified homography. 

<br>

### Rectification

In order to check that my homography and warping methods were working, I rectified an image. Specifically, I took an image of a painting that was taken from an angled perspective, defined its corners, and computed a homography between the set of corners of that image and a flat rectangle. Below is the original image followed by a rectified version of it.

<img src='IMG_6379.png' width=300>&nbsp;&nbsp;&nbsp;&nbsp;<img src='rectified.png' width=284>

As you can see, it turns out quite well. (I took this picture at the Louvre in Paris.)

Here's another example:

<img src='IMG_1456.png' width=300>&nbsp;&nbsp;&nbsp;&nbsp;<img src='rectified2.png' width=284>

There's some noticable aliasing here, admittedly, but the rectification itself works. I fixed the aliasing later on.

<br>

### Defining Correspondences

The first step is to take images and define correspondences between them. I took 3 pairs of images, and defined between 19 and 30 correspondences on each. (The first pair is from my kitchen, the second pair is from a park near my house, and the third pair is in my backyard.)


<img src='kitchleft.png' width = 250>&nbsp;&nbsp;&nbsp;&nbsp;<img src='kitchright.png' width = 250> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img src='parkleft.png' width = 250>&nbsp;&nbsp;&nbsp;&nbsp;<img src='parkright.png' width = 250>

<img src='backleft.png' width = 333>&nbsp;&nbsp;&nbsp;&nbsp;<img src='backright.png' width = 333>

<br>

Then, I computed a median correspondence, similar to what was done in Project 3. (I found that this gave better results than trying to warp image 1 into the perspective of image 2.) This produces warped versions of both images in the pair.

<img src='warpa.png' width = 250>&nbsp;&nbsp;&nbsp;&nbsp;<img src='warpb.png' width = 250> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img src='parkwarp1.png' width = 250>&nbsp;&nbsp;&nbsp;&nbsp;<img src='parkwarp2.png' width = 250>

<img src='backwarp1.png' width = 333>&nbsp;&nbsp;&nbsp;&nbsp;<img src='backwarp2.png' width = 333>

<br>

Lastly, I overlaid and aligned the warped images on top of one another.

<img src='merge.png' width=550> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img src='parkmos.png' width=550>

<img src='backmos.png' width=550>

<br>

The park panorama seems to have come out the best; I believe it's because it has the least details in the region of overlap. The kitchen isn't great, especially near on the left edge of the island. The backyard is decent but some details towards the back are imperfect (in particular, the rear pillars).

<br><br>

---


## Part 2: Feature Matching for Autostitching


I primarily used the park images while implementing each of the features here, but at the end I present the results of autostitching on the other two examples as well. In order to do the computations in this section, I rescaled my images from being 12MP to 0.75MP (still ~1000 x 700, which is certainly good enough).

<br>

### Step 0: Harris corners

Luckily, we were provided `get_harris_corners`. Here's the result after calling it on the left park image:

<img src='harrispark.png' width=300>

<br>

### Step 1: Adaptive Non-Maximal Suppression

I then implemented Adaptive Non-Maximal Suppression (ANMS), which is detailed in [this paper](https://inst.eecs.berkeley.edu/~cs194-26/sp20/Papers/MOPS.pdf). In short, this aims to find points that are spaced out that are in relevant positions. I chose the top 500.

<img src='anms.png' width=300>

<br>

### Step 2 and 3: Feature Extraction and Feature Matching

In Step 2, we take 8x8 samples (from a larger 40x40 patch) in the neighborhood of each keypoint (in both images), and normalize them. In Step 3, we compare the set of normalized samples in one image with the set of normalized samples in the other, and compute distances between them. The goal of this is to find "matches" between a keypoint in the first image and a keypoint in the second, to denote that these are one correspondence.

In order to select correspondences, I computed the Lowe ratio – (distance to 1NN)/(distance to 2NN) – and took pairs for whom this ratio was below 0.45.

<img src='nnpoints.png' width=700>

As depicted above, the chosen points are quite close.

<br>

### Step 4: RANSAC

I then implemented RANSAC, i.e. "Random Sample Consensus", in order to determine the subset of keypoints that created the best homographies. I used this subset of keypoints to generate two homographies again – one from the left image to a median, and one from the right image to a median. I then followed the same process above to warp the two images and stitch them together. 

Below, on the left we have the resulting panorama given by using Part B methods (ANMS, RANSAC), and on the right we have the resulting panorama using manually-defined correspondences from Part A.


<img src='parkmos.png' width=550>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='parkmos_ransac.png' width=550>
<img src='backmos.png' width=550>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='backmos_ransac.png' width=550>
<img src='merge.png' width=550>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='kitmos_ransac.png' width=550>

<br>

### Conclusion

This project showed me the many intricacies involved in creating automatic panoramas. It's far more complicated than I thought.
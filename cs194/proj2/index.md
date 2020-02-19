<br>

<title>Fun with Filters and Frequencies</title>

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


# Fun with Filters and Frequencies

## Project 2, CS 194-26, Spring 2020

**by Suraj Rampure (`suraj.rampure@berkeley.edu`, `cs194-26-adz`)**


---

In this project, we play around with convolutions with difference operators and Gaussians in order to straighten, sharpen, hybridize, and blend images together. Fun stuff!

---

<a name='part1'>

## Part 1: Fun with Filters

</a>


<a name='1.1'>

### 1.1: Finite Difference Operator

</a>

We begin with a grayscale image of a cameraman, as provided in the spec.

<img src="cameraman.png" width=200>

First, we convolve our image with the finite difference operators $D_x = [1, -1]$ and $D_y = [1, -1]^T$ in order to show an estimate of the $x$ and $y$ gradients, respectively. The $x$ gradient is shown on the left below, with the $y$ gradient on the right:

<div align = center>

  <img src="export/cameraman_dx.jpg" width=200>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="export/cameraman_dy.jpg" width=200>

</div>

As we can see, in the $x$ gradient, we see primarily vertical lines, as these depict the direction in which the image changes horizontally (and vice versa in the $y$ gradient).

We then compute the magnitude of the gradient, by taking the square root of the sum of the squares of the magnitudes of both gradients. This image is shown on the **left**. This does a decent job at detecting the edges in the `cameraman` image. However, there is a decent amount of noise, so in order to make the edges a little more prominent, we can binarize the above image. On the **right** is the result of doing so, using a threshold of `t = 0.3`:

<img src="export/cameraman_grad_raw.jpg" width=200>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="export/cameraman_grad_raw_binarized.jpg" width=200>

<br>

---

<a name='1.2'>

### 1.2: Derivative of Gaussian (DoG) Filter

</a>

Consider the Gaussian kernel, shown here with width 10 and $\sigma = 1.5$:

<img src="export/gauss_screenshot.png" width=200>

First, we convolve this Gaussian kernel with our `cameraman` image:

<img src="export/cameraman_blurred.jpg" width=200>

Note, the result is slightly blurred. We can then apply the same $D_x$ and $D_y$ derivative filters from above, and use them to create a gradient magnitude plot. Below is the gradient magnitude, shown raw (left) and binarized (right) with threshold $t = 0.7$:

<img src="export/cameraman_blur_first.jpg" width=200>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="export/cameraman_blur_first_binarized.jpg" width=200>

<br>

Alternatively, we can first convolve the Gaussian kernel with the $D_x$ and $D_y$ filters, and then convolve these with the original image. Doing this yields the following raw (left) and binarized (right, again with the same $t = 0.7$) gradient magnitude images:

<img src="export/camerman_grad_dog.jpg" width=200>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="export/camerman_grad_dog_binarized.jpg" width=200>

We see that the end result, after binarizing, is the same, and are both noticably less noisy than the gradient magnitude image from Part 1.1. The non-binarized versions show the same amount of detail, and just vary by some constant. 

We've just demonstrated the associativity property of the convolution operator (`*`):

```(image * gradient) * blur = image * (gradient * blur)```

<br>

---

<a name='1.3'>

### 1.3: Image Straightening

</a>

Now, we will switch gears and focus on image straightening. Specifically, given an image, we want to find the angle of rotation $\beta$ that maximizes the number of horizontal and vertical edges.

We will implement the following pseudocode:

```
given: image (image to blur), betas (possible rotation angles)

for beta in betas:
  rotate image by beta
  crop away outer 35% of image
  convolve image with Gaussian kernel
  for each pixel in rotated image:
    compute theta = arctan2(dy, dx) and store in thetas
  compute score = number of values in thetas corresponding to horizontal and vertical edges 
return beta with best score

```

We use $\theta = tan^{-1}(dy / dx)$ as this provides us with the angular rate of change at that point. We count "horizontal edges" as pixels with $\theta \approx 0º$ or $\theta \approx 180º$ and "vertical edges" as pixels with $\theta \approx \pm 90º$.

For  `betas`, we look at every integral angle in the range [-20, 20]. 

Below, we show several images, the optimal rotation angle, their rotated version, and histograms of angles for both the base and rotated image.

| Image | Angle of Rotation | Rotated Image | Base Histogram | Rotated Histogram |
| --- | --- | --- | --- | --- |
| <img src='facade.jpg' width = 200> | $-3º$ | <img src='export/straightened/facade_fixed.jpg' width = 200> | <img src='export/straightened/facade_base_histogram.jpg' width = 300> | <img src='export/straightened/facade_rotated_histogram.jpg' width = 300> |
| <img src='crooked_2.jpeg' width = 200> | $-11º$ | <img src='export/straightened/crooked_2_fixed.jpg' width = 200> | <img src='export/straightened/crooked_2_base_histogram.jpg' width = 300> | <img src='export/straightened/crooked_2_rotated_histogram.jpg' width = 300> |
| <img src='crooked.jpeg' width = 200> | $-6º$ | <img src='export/straightened/crooked_fixed.jpg' width = 200> | <img src='export/straightened/crooked_base_histogram.jpg' width = 300> | <img src='export/straightened/crooked_rotated_histogram.jpg' width = 300> |
| <img src='screenshot.png' width = 200> | $11º$ | <img src='export/straightened/screenshot_fixed.jpg' width = 200> | <img src='export/straightened/screenshot_base_histogram.jpg' width = 300> | <img src='export/straightened/screenshot_rotated_histogram.jpg' width = 300> |

<br> 

Below are two failure cases.

| Image | Angle of Rotation | Rotated Image | Base Histogram | Rotated Histogram |
| --- | --- | --- | --- | --- |
| <img src='fakecamp.png' width = 200> | $12º$ | <img src='export/straightened/fakecamp_fixed.jpg' width = 200> | <img src='export/straightened/fakecamp_base_histogram.jpg' width = 300> | <img src='export/straightened/fakecamp_rotated_histogram.jpg' width = 300> |
| <img src='sunset.png' width = 200> | $-20º$ | <img src='export/straightened/sunset_fixed.jpg' width = 200> | <img src='export/straightened/sunset_base_histogram.jpg' width = 300> | <img src='export/straightened/sunset_rotated_histogram.jpg' width = 300> |

In the first image (of the bell tower at Imperial College London, that I called the "fake Campanile"), I believe it rotated in this way because of the horizontal lines going across the tower. In the second image (of a sunset at Santa Monica Pier), the waves and sunset gradient must've played a role.

One thing that helped my algorithm was blurring the images before rotating and counting edges. Before doing this, I believe there was far too much noise in the gradient magnitude plot to reliably detect edges.

<br><br>

---

## Part 2: Fun with Frequencies!

### 2.1: Image "Sharpening"

In order to sharpen an image, we can subtract a "blurry" version of it from itself, in order to compute the "detail" (a high-frequency-preserving version of the image). We can then add the "detail" back to the image, increasing the number of high frequencies in the image, making it appear sharper. 

For the sake of illustration, we can show all four stages of this process on the Taj Mahal sample image. From left to right, we have the original image, the blurred image, the detail image, and the resharpened image.

<img src="export/sharpen/taj.jpg" width=250>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="export/sharpen/taj_blurred.jpg" width=250>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="export/sharpen/taj_detail.jpg" width=250>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="export/sharpen/taj_sharpened.jpg" width=250>

We can combine these steps into a single filter, called the "un-sharp mask filter". Below is the result of this filter being called on a few images.

| Image | Sharpened Image |
| --- | --- | 
| <img src="export/sharpen/junior.png" width=300> | <img src="export/sharpen/junior_sharp.png" width=300> |
| <img src="export/sharpen/towerbridge.png" width=300> | <img src="export/sharpen/towerbridge_sharp.png" width=300> |

In each case, we can see that the "sharpened" image seems to have more prominent high frequencies, and certainly appear sharper. For example, look at the mulch in the bottom left of the picture of my dog (Junior, henceforth), or at my face. It's cool to note that the unsharp mask filter cannot "un-blur" the background in the picture of me; the Tower Bridge in the background remains blurry. This is because no new information is gained through this process.

We can see this phenomenon again, with this photo of the Eiffel Tower. From left to right, we have the original sharp image, a Gaussian-blurred version of it, and then the result of applying our unsharp mask filter to the blurred version.

<img src="export/sharpen/eiffel.png" width=250>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="export/sharpen/eiffel_blurred.png" width=250>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="export/sharpen/eiffel_resharpen.png" width=250>

The "resharpened" version is still quite blurry, as there aren't many high frequencies to begin with, so adding them back doesn't amount to much. 

<br>

---

### 2.2: Hybrid Images

To create hybrid images, we first need to select and align two images. One needs to be chosen as the "low pass" image, which will be visible from far away, and one is the "high pass", which will be visible from close by. 

| Image 1 (Low-Pass) | Image 2 (High-Pass) | Hybrid |
| --- | --- | --- |
| <img src="hybrid/raw/DerekPicture.jpg" width=250> | <img src="hybrid/raw/nutmeg.jpg" width=250> | <img src="hybrid/merged/catman.jpg" width=250> |
| <img src="hybrid/aligned/lebron.png" width=250> | <img src="hybrid/aligned/kobe.png" width=250> | <img src="hybrid/merged/lebronkobe.jpg" width=250> |
| <img src="hybrid/aligned/me copy.jpeg" width=250> | <img src="hybrid/aligned/littleme.jpeg" width=250> | <img src="hybrid/merged/youngoldme.jpg" width=250> |
| <img src="hybrid/aligned/junior.jpeg" width=250> | <img src="hybrid/aligned/me copy.jpeg" width=250> | <img src="hybrid/merged/mejunior.jpg" width=250> |

The last case – an attempted hybrid between Junior and I – didn't work out too well, and I believe it's because of the dramatically different backgrounds of the images. I consider this a failure, as I don't think anyone views this as a true hybrid between me and Junior. The other two examples I chose – a hybrid between LeBron and Kobe, and a hybrid between a 21-year old and 10-year old version of me – had similar backgrounds, and so they turned out quite well.

<br>

Let's look at the Fourier Transform of the LeBron-Kobe hybrid image. 

<img src="hybrid/merged/lkf1.jpg" width=350>&nbsp;&nbsp;<img src="hybrid/merged/lkf2.jpg" width=350>

<img src="hybrid/merged/lkf3.jpg" width=350>&nbsp;&nbsp;<img src="hybrid/merged/lkf4.jpg" width=350>

<img src="hybrid/merged/lkf5.jpg" width=350>

The FFT of the final merged image contains the low frequencies from the LeBron image and the high frequencies from the Kobe image.

<br>

---

### 2.3: Gaussian and Laplacian Stacks

To create a Gaussian stack, we can iteratively blur our image with a Gaussian kernel, making it blurrier each time. To create a Laplacian stack, we take the successive differences between each layer of the Gaussian stack of the same image.

Consider the example Lincoln image provided in the spec:

<img src="lincoln.jpg" width=200>

Here are the Gaussian and Laplacian stacks of this image, respectively.

<img src="export/stacks/abegaussian.jpg" width=1000>

<img src="export/stacks/abelaplacian.jpg" width=1000>

<br>

Here is the Mona Lisa, along with its Gaussian and Laplacian stacks.

<img src="monalisa.jpg" width=200>

<img src="export/stacks/monagaussian.jpg" width=1000>

<img src="export/stacks/monalaplacian.jpg" width=1000>


Here's yet another picture of Junior.

<img src="junior2.png" width=200>

<img src="export/stacks/juniorgaussian.jpg" width=1200>
<img src="export/stacks/juniorlaplacian.jpg" width=1200>

<br>

Lastly, we'll take a look at the Gaussian and Laplacian stacks for the LeBron-Kobe hybrid image from earlier.

<img src="hybrid/merged/lebronkobe.jpg" width=200>

<img src="export/stacks/goatgaussian.jpg" width=1200>
<img src="export/stacks/goatlaplacian.jpg" width=1200>

As we'd expect, the more we blur the image (i.e. the further we go down our Gaussian stack), the more the image looks like LeBron and the less it looks like Kobe.

<br>

---

### 2.4: Multiresolution Blending

Here, we take two images, and blend them together. This is done by creating Laplacian stacks of both images, as well as a Gaussian stack of a mask that specifies how to combine the two images. To do this, we use the rule

`LS[l] = GR[l] * LA[l] + (1 - GR[l]) * LB[l]`

where `LS` represents the output stack, `GR[l]` represents the Gaussian stack of our mask at level `l`, and `LA[l]` and `LB[l]` represent the Laplacian stack of our first / second image at level `l`, respectively.

Below are some results:

| Image 1 | Image 2 | Blended Image |
| --- | --- | --- |
| <img src="apple.jpeg" width=250> | <img src="orange.jpeg" width=250> | <img src="export/blend/orapple.jpg" width=250> |
| <img src="hybrid/aligned/lebron.png" width=250> | <img src="hybrid/aligned/kobe.png" width=250> | <img src="export/blend/goat.jpg" width=250> |

For the LeBron-Kobe stitching, the fact that their faces are of slightly different sizes makes the seam a little weird, but I think it still works. Let's take a look at the Laplacian stacks of the LeBron image, the Kobe image, and the blended image.

<img src="export/blend/lebronstack.jpg" width = 1000>

<img src="export/blend/kobestack.jpg" width = 1000>

<img src="export/blend/goatstack.jpg" width = 1000>

<br>

Finally, we'll look at a blend using an irregular mask. From left to right, we have the two images, the mask, and the final result.

<img src="export/blend/lapool.jpg" width=250>&nbsp;&nbsp;&nbsp;&nbsp;<img src="export/blend/lapeak.jpg" width=250>&nbsp;&nbsp;&nbsp;&nbsp;<img src="export/blend/lamask.jpg" width=250>&nbsp;&nbsp;&nbsp;&nbsp;<img src="export/blend/lablend.jpg" width=250>&nbsp;&nbsp;&nbsp;&nbsp;

<br><br><br>

## Conclusion

Overall, I thought this was a fascinating project. It was so cool to see that with relatively basic techniques (simple convolutions), we can generate some pretty powerful results. The basic edge detector (convolving with the finite difference operator) and the fact that we could straighten images using it was shocking.

It should be noted that I did several things in color when they were only asked to be done in grayscale, so I believe that counts as a bells-and-whistle.
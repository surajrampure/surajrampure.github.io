---
title: Home
---

<div style="width: 100%;" markdown="1">

<div style="width: 42%; float: left;">

<img src="assets/me-award-compressed.jpeg" width="100%">

</div>

<div style="margin-left: 46%; white-space: normal;" markdown="1"> 

# Suraj Rampure
<span style="display:block; color: #888; font-size: 0.95em; margin-top: -1em;">"soo-rudge rahm-poo-ray"</span>

Lecturer III<br>Computer Science and Engineering, University of Michigan<br>4721 Beyster Building<br>[rampure@umich.edu](mailto:rampure@umich.edu)<br>

<!-- <div id="current-location" style="
  display: inline-flex;
  align-items: center;
  background: linear-gradient(135deg, #74a9ff 0%, #1a73e8 100%);
  color: white;
  padding: 2px 6px;
  border-radius: 10px;
  font-size: 10px;
  font-weight: 500;
  margin: 0px 0 8px 0;
  box-shadow: 0 1px 4px rgba(0,0,0,0.1);
  transition: all 0.3s ease;
">
  <span style="margin-right: 3px; font-size: 10px;">📍</span>
  <span>Loading location...</span>
</div> -->

Hey! 👋 I'm a member of the teaching faculty in [Computer Science and Engineering](https://cse.engin.umich.edu/) at the University of Michigan. I am affiliated with [MIDAS](https://midas.umich.edu/faculty-member/suraj-rampure/), serve on the undergraduate computer science and data science program committees, and am one of the hosts of [Faculty Chats](https://cse.engin.umich.edu/academics/undergraduate/undergraduate-advising/faculty-chats/) (come say hi!).

Previously, I taught in the [Halıcıoğlu Data Science Institute](https://datascience.ucsd.edu/) at the University of California, San Diego, where I received the campus-wide Distinguished Teaching Award in 2024. I earned BS and MS degrees in [Electrical Engineering and Computer Sciences](https://eecs.berkeley.edu/) from the University of California, Berkeley, and I'm originally from Windsor, Ontario 🇨🇦.

</div>

<script>

async function loadLocation() {
    try {
        const response = await fetch('location.json');
        const data = await response.json();
        
        const locationElement = document.getElementById('current-location');
        locationElement.innerHTML = `
            <span style="margin-right: 3px; font-size: 10px;">📍</span>
            <span>Current Location: ${data.city}</span>
        `;
        locationElement.title = `Updated ${new Date(data.updated).toLocaleDateString()}`;
    } catch (error) {
        console.error('Failed to load location:', error);
        const locationElement = document.getElementById('current-location');
        locationElement.innerHTML = `
            <span style="margin-right: 3px; font-size: 10px;">📍</span>
            <span>Location unavailable</span>
        `;
    }
}
// Load on page load
loadLocation();
</script>

---

On this page: <a href="#teaching">Teaching</a> • <a href="#scholarship">Scholarship</a> • <a href="#awards">Awards</a><br>
Other links:  <a href="resources/cv-2025.pdf">CV</a> • <a href="tf-app-materials">Teaching Faculty Application Materials</a> • <a href="letters">Rec. Letters</a> • <a href="python-teaching-commons">Python Teaching Commons</a><br>
Totally random: <a href="travel">Travel Recommendations</a>

---

<a name='teaching'></a>

## Teaching

<div style="display: flex; align-items: flex-start;">
  <img src="assets/umich-logo.png" width="75" height="75" alt="University of Michigan" style="margin-right: 30px; margin-top: 4px;">
  <div style="flex: 1;">
    <h3 style="display: inline;">University of Michigan, Ann Arbor (2024-)</h3>
    <span style="display: block; height: 0.5em;"></span>
    <strong>EECS 245: Mathematics for Machine Learning 🧠</strong><br>
    Winter 2026, <a href="https://eecs245.org"><strong>Fall 2025</strong></a>
    <br><br>
    <strong>EECS 398: Practical Data Science 🛠️</strong><br>
    <a href="https://practicaldsc.org/next">Spring 2025 (Half-Term)</a> • <a href="https://practicaldsc.org/wn25">Winter 2025</a> • <a href="https://practicaldsc.org/fa24">Fall 2024</a><br>
    <!-- <small>Highlights: [Linear Algebra Review for Data Science (LARDS)](https://practicaldsc.org/lin-alg)</small> -->
    <br>
    <strong>Other Teaching</strong><br>
    <a href="dair3">Building Robust ML Models (MIDAS Biomedical Researchers Summer Academy 2025)</a>
  </div>
</div>

<br>

<div style="display: flex; align-items: flex-start;">
  <img src="assets/ucsd-logo.png" width="75" height="75" alt="UC San Diego" style="margin-right: 30px; margin-top: 4px;">
  <div style="flex: 1;">
    <h3 style="display: inline;">University of California, San Diego (2021-2024)</h3>
    <!-- <br> -->
    <!-- <em>You can view course websites for many DSC (and adjacent) courses <a href="https://dsc-courses.github.io">here</a>.</em> -->
    <span style="display: block; height: 0.5em;"></span>
    <strong>DSC 40A: Theoretical Foundations of Data Science I 🧠</strong><br>
    <a href="https://dsc-courses.github.io/dsc40a-2024-sp">Spring 2024</a> • <a href="http://dsc-courses.github.io/dsc40a-2021-fa/">Fall 2021</a><br>
    <!-- <small>Highlights: [Regression FAQs](https://dsc-courses.github.io/dsc40a-2024-sp/faqs), [Past Exam Practice](https://practice.dsc40a.com)</small> -->
    <br>
    <strong>DSC 95: Tutor Apprenticeship in Data Science 🧑‍🏫</strong><br>
    <a href="https://dsc-courses.github.io/dsc95-2024-sp/">Spring 2024</a> • <a href="https://dsc-courses.github.io/dsc95-2023-sp/">Spring 2023</a>
    <br><br>
    <strong>DSC 80: Practice and Application of Data Science 💪</strong><br>
    <a href="https://dsc-courses.github.io/dsc80-2024-wi">Winter 2024</a> • <a href="https://dsc-courses.github.io/dsc80-2023-wi">Winter 2023</a> • <a href="https://dsc-courses.github.io/dsc80-2022-sp">Spring 2022</a><br>
    <!-- <small>Highlights: [Past Exam Practice](https://practice.dsc80.com)</small> -->
    <br>
    <strong>DSC 180AB: Data Science Project (Senior Capstone) 👷</strong><br>
    <a href="https://dsc-capstone.org">Fall 2023 + Winter 2024</a> • <a href="https://dsc-capstone.org/2022-23/">Fall 2022 + Winter 2023</a>
    <br><br>
    <strong>DSC 10: Principles of Data Science 📊</strong><br>
    <a href="https://dsc-courses.github.io/dsc10-2023-fa/">Fall 2023 (with Janine Tiefenbruck & Rod Albuyeh)</a> • <a href="https://dsc-courses.github.io/dsc10-2023-sp/">Spring 2023</a> • <a href="http://dsc-courses.github.io/dsc10-2022-fa/">Fall 2022 (with Janine Tiefenbruck & Puoya Tabaghi)</a> • <a href="http://dsc-courses.github.io/dsc10-2022-wi/">Winter 2022</a> • <a href="http://dsc-courses.github.io/dsc10-2021-fa/">Fall 2021 (with Janine Tiefenbruck)</a><br>
    <!-- <small>Highlights: [Past Exam Practice](https://practice.dsc10.com)</small> -->
    <br>
    <strong>CSS 201S: Introduction to Python Bootcamp (Week 1 only) 🥾</strong><br>
    <a href="https://rampure.org/css-python-bootcamp/">Summer 2022</a>
    <br><br>
    <strong>DSC 90: History of Data Science Seminar 📚</strong><br>
    <a href="http://dsc-courses.github.io/dsc90-2022-sp/">Spring 2022</a> • <a href="http://dsc-courses.github.io/dsc90-2022-wi/">Winter 2022</a>
  </div>
</div>

<br>

<div style="display: flex; align-items: flex-start;">
  <img src="assets/berkeley-logo.png" width="75" height="75" alt="UC Berkeley" style="margin-right: 30px; margin-top: 4px;">
  <div style="flex: 1;">
    <h3 style="display: inline;">University of California, Berkeley (2016-2021)</h3>
    <span style="display: block; height: 0.5em;"></span>
    <strong>Data 94: Introduction to Computational Thinking with Data</strong><br>
    <a href="https://rampure.org/data-94-sp21">Spring 2021</a> (now known as <a href="http://data6.org">Data 6</a>)
    <br><br>
    <strong>Data 100: Principles and Techniques of Data Science</strong><br>
<a href="http://ds100.org/su20">Summer 2020 (with Allen Shen)</a><br>
TA: 
<a href="http://ds100.org/fa20">Fall 2020</a> &bull; 
<a href="http://ds100.org/sp20">Spring 2020</a> &bull; 
<a href="http://ds100.org/fa19">Fall 2019</a> &bull; 
<a href="http://ds100.org/sp19">Spring 2019</a> &bull; 
<a href="http://ds100.org/fa18">Fall 2018</a>
<br><br>
<strong>CS 198-087: Introduction to Mathematical Thinking <a href="http://decal.berkeley.edu">[DeCal]</a></strong><br>
<a href="http://imt-decal.org">Spring 2019</a>, Fall 2018
<br><br>
<strong>CS 70: Discrete Mathematics and Probability Theory</strong><br>
TA: <a href="http://su19.eecs70.org">Summer 2019</a>
<br><br>
<strong>CS 375: Teaching Techniques for Computer Science</strong><br>
TA: <a href="http://cs375.github.io/su19">Summer 2019</a>
<br><br>
<strong>CS 61A: Structure and Interpretation of Computer Programs</strong><br>
TA: <a href="https://inst.eecs.berkeley.edu/~cs61a/sp18/">Spring 2018</a>
<br><br>
<strong>Data 8: Foundations of Data Science</strong><br>
TA: <a href="http://data8.org/fa17">Fall 2017</a><br>
Tutor: <a href="http://data8.org/sp17">Spring 2017</a>
<br><br>
  </div>
</div>

---

<a name='scholarship'></a>

## Scholarship

### Papers

- [The Challenges of Evolving Technical Courses at Scale: Four Case Studies of Updating Large Data Science Courses](https://www.samlau.me/pubs/Challenges-of-Evolving-Data-Courses_L@S-2022.pdf). Sam Lau, Justin Eldridge, Shannon Ellis, Aaron Fraenkel, Marina Langlois, Suraj Rampure, Janine Tiefenbruck, Philip Guo. In _ACM Conference on Learning @ Scale (L@S), 2022_.
- [A New Data-Focused Introductory Programming Course](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2021/EECS-2021-106.html). Suraj Rampure. 2021. Master's technical report, UC Berkeley EECS.
- [Experiences Teaching a Large Upper-Division Data Science Course Remotely](https://dl.acm.org/doi/pdf/10.1145/3408877.3432561). Suraj Rampure\*, Allen Shen\*, and Josh Hug. 2020. In _Proceedings of the 52nd ACM Technical Symposium on Computer Science Education (SIGCSE ’21)._ ([slides](https://docs.google.com/presentation/d/1xBMcdYKrhM0U1FxOKZ93TCqIdDIWFqdz7ns49LN_ukg/edit?usp=sharing)) ([video](https://youtu.be/_p-JUp4QyNA))

### Talks
- RISE and Shine: Teaching with Jupyter Notebooks in Real Time. Suraj Rampure, Nishant Kheterpal, and Janine Tiefenbruck. Talk at _[JupyterCon 2025](https://jupytercon2025.sched.com/event/28H4f/rise-and-shine-teaching-with-jupyter-notebooks-in-real-time-suraj-rampure-nishant-kheterpal-university-of-michigan-janine-tiefenbruck-university-of-california-san-diego)_.
- Different Mediums for Different Audiences: A Capstone Case Study. Suraj Rampure. Talk at _[Teaching and Evaluating Data Communication at Scale 2024](https://www.imsi.institute/activities/teaching-and-evaluating-data-communication-at-scale/)_. ([slides](https://cdn.imsi.institute/videos/49129/iPxQvXT38E/slides.pdf)) ([video](https://www.imsi.institute/videos/different-mediums-for-different-audiences-a-capstone-case-study/))
- Otter-Grader: A Lightweight Solution for Creating and Grading Jupyter Notebook Assignments. Suraj Rampure, Christopher Pyles, Justin Eldridge, and Lisa Yan. Talk at _[Jupytercon 2023](https://cfp.jupytercon.com/2023/talk/XABS9S/)_. ([materials](https://github.com/chrispyles/otter-grader-jupytercon-2023)) ([video](https://www.youtube.com/watch?v=9_x532_2T2w))
- Data 6: A New Introductory Course. Talk at _[2021 National Workshop on Data Science Education](https://data.berkeley.edu/academics/resources/data-science-education-workshop/2021-national-workshop-data-science-education)_. ([slides](https://docs.google.com/presentation/d/1eeJvHmDNQanVOFjKn8Jky63ONxHPmDyq6I764f-YPdE/edit#slide=id.gb6d01dc2f6_0_124)) ([video](https://www.youtube.com/watch?v=4pMLelvesR8))
- Various sessions on Data 100: Principles and Techniques of Data Science at _[2020 National Workshop on Data Science Education](https://data.berkeley.edu/academics/resources/data-science-education-resources/2020-national-workshop-data-science-education)_. ([pre-recorded talk](https://www.youtube.com/watch?v=VxL9L7VkJTE&feature=youtu.be)) ([Q&A](https://www.youtube.com/watch?v=lfyyZQDlyXQ)) ([workshop](https://www.youtube.com/watch?v=1FsYgKKh9gk&feature=youtu.be))

### Panels and Related Sessions

- [A New Class of Teaching-Track Faculty: No Ph.D. Required](https://sigcse2025.sigcse.org/details/sigcse-ts-2025-birds-of-a-feather/31/A-New-Class-of-Teaching-Track-Faculty-No-Ph-D-Required). Birds of a Feather session at _Proceedings of the 56th ACM Technical Symposium on Computer Science Education (SIGCSE '25)._
- [A New Class of Teaching-Track Faculty: No Ph.D. Required](https://dl.acm.org/doi/10.1145/3545947.3569608). In _Proceedings of the 54th ACM Technical Symposium on Computer Science Education (SIGCSE '23)._ ([slides](https://docs.google.com/presentation/d/1H2ngrPNb8TQXxIrCOFhXHce8-x6KEgHzw-bdFNrmQpQ/edit#slide=id.gb6f9b1ca0f_0_53))
- Introduction to Computational Thinking with Data and Society. In _[2022 National Workshop on Data Science Education](https://data.berkeley.edu/2022workshop/schedule)_.
- [A New Class of Teaching-Track Faculty: No Ph.D. Required](https://dl.acm.org/doi/10.1145/3478432.3499227). In _Proceedings of the 53rd ACM Technical Symposium on Computer Science Education (SIGCSE '22)._ ([slides](https://docs.google.com/presentation/d/12PalILpKLBHadL9GibmY4jATogp6BMHdIcsT_NUVSRc/edit#slide=id.gb6f9b1ca0f_0_53))

### Media

- UC San Diego Today: [Signature Program Demonstrates How UC San Diego Undergraduates Learn to Transform Data into Action](https://today.ucsd.edu/story/signature-program-demonstrates-how-uc-san-diego-undergraduates-learn-to-transform-data-into-action)
- ComputingPaths at UC San Diego: [Meet Suraj Rampure, Lecturer in the Halıcıoğlu Data Science Institute](https://www.youtube.com/watch?v=rQYUDs6Wz3E)
- UC Berkeley Research News: [UC Berkeley and Tuskegee University Announce Data Science Partnership](https://vcresearch.berkeley.edu/news/uc-berkeley-and-tuskegee-university-announce-data-science-partnership)
- UC Berkeley Data Science Education Podcast: [The Importance of Data Science Course Staff](https://datascienceeducation.substack.com/p/the-importance-of-data-science-course)

<br>

---

<a name='awards'></a>

## Awards

- 2023-2024 [UC San Diego Distinguished Teaching Award](https://senate.ucsd.edu/grants-awards/senate-awards/distinguished-teaching-award)
- 2020-2021 [UC Berkeley Extraordinary Teaching in Extraordinary Times Award](https://rtl.berkeley.edu/extraordinary-teaching-extraordinary-times-award) ([article](https://data.berkeley.edu/news/cdss-instructors-honored-five-awards-extraordinary-teaching-extraordinary-times))
- 2019-2020 [UC Berkeley EECS Distinguished GSI Award](https://www2.eecs.berkeley.edu/Students/Awards/13/)
- 2017-2018 [UC Berkeley EECS Outstanding GSI Award](https://gsi.berkeley.edu/programs-services/award-programs/ogsi/ogsi-2018/)<br><br>

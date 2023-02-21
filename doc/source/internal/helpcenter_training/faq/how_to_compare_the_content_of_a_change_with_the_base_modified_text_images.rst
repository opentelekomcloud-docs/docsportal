============================================================================
How to compare the content of a change with the base (modified text/images)?
============================================================================

Gitea/Github natively support the comparison between the diffs and new PR is nothing else just a diff to a base. Text comparison is represented as a "red" (removals) and "green" (addons) highlighted changes as shown on the image below:

.. figure:: /_static/images/compare_text.png

Image comparison offers multiple options how to visualize changes. The most common is side by side comparison:

.. figure:: /_static/images/compare_images.png

In case there are only added changes or the whole new files are added then the whole file is highlighted by green color:

.. figure:: /_static/images/added_new_text.png


Gitea/Github also natively support comparison changes between the multiple commits inside of the single pull request. For example follow-up updates from Huawei based on QA/UAT reviews are represented as multiple commits in same PR. The differences between the commits can be seen by clicking on the respecitve commit which will show the differences against the previous commit.

.. figure:: /_static/images/compare_commits.png


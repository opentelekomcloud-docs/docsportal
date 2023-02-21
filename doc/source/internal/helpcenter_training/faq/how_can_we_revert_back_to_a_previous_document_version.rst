.. _how_can_we_revert_back_to_a_previous_document_version:

======================================================
How can we revert back to a previous document version?
======================================================

In git the revert action would mean just another PR with changes pushing the document to previous state. To minimize revert situations both Gitea/Github represents 3 phases of validatiing the documentation.

-  Automated check jobs which validate syntax, conversion and build possibility of the documentation change.

-  Manual approval based on QA/UAT review.

-  Labelling the PR with **gate** label which is only applicable when previous 2 conditions are succefully completed. (Final Gate label will initiate auto-merge jobs and final publishing of the documentation change to Help Center portal). Squad can decide that this final "Go" can be triggered by different person only delegated for releasing activities.

============
Introduction
============

The HelpCenter3.0 is Open Telekom Cloud product developed by Ecosystem squad introducing new approach in the documentation management.
It aims to bring the benefits of the gitops approach such as:

-  Openness
-  Transparency
-  Comprehensive review capabilities
-  Full control during the documentation lifecycle
-  Documentation as a source code

.. figure:: /_static/images/helpcenter_gitops.png

Solution is completely open source based and HLD is described at https://docs.otc-service.com/system-config/docsportal.html
Implementation is based on:

-  Restructured Text (RST) as source documentation format
-  Gitea/Github as a repository
-  Zuul as a CI/CD engine for workflows
-  Sphinx as a documentation rendering framework (HTML/PDF/...
-  OpenSearch as a search engine
-  Swift object storage as a storage for documentation
-  Pandoc as a documentation converter
-  OTC Infrastructure (ECS, CCE, ELB, ...)

HC3.0 comes with the following features:

-  Support of UMN, API, DEV and other public facing documents
-  PROD and PREPROD documentation portal:

   -  docs.otc.t-systems.com
   -  docs-int.otc.service.com

-  Support of all old HC links redirections
-  Search functionality
-  Mobile-ready UI layout
-  Report issue functionality directly on any page
-  Suggest documentation fix functionality 
-  Consolidation of extra content like blueprints, tools, and libraries for developers 
-  One repository represents one cloud service
-  Each squad can control and manage their documentation independently
-  Automatization and check jobs across whole documentation lifecycle (from import to release)

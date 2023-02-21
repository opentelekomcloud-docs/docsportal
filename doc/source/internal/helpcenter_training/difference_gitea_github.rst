.. _difference_gitea_github:

=========================
Difference Gitea / Github
=========================

Due to the several requirements on Huawei and TSI side 2 gitops stages introduced. At first stage Huawei imports documentation to Gitea and TSI review and approve it.
Afterwards documentation change is introduced to Github and TSI formally review it and approve.

But there are few more differences which are described in the table below:

+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Differences**                                    | **Gitea**                                          | **Github**                                         |
+====================================================+====================================================+====================================================+
| Link                                               | https://gitea.eco.tsi-dev.otc-service.com/docs     | https://github.com/opentelekomcloud-docs/          |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Environment                                        | PREPROD                                            | PROD                                               |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
|                                                    | internal                                           | public                                             |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Who can introduce changes                          | Huawei                                             | Anyone (TSI, Huawei, customer)                     |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Source of documentation                            | Huawei                                             | TSI+Huawei                                         |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Form of change                                     | Overwrite                                          | Diff                                               |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Portal                                             | https://docs-int.otc-service.com                   | https://docs.otc.t-systems.com                     |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Document types                                     | -  UMN, API, DEV, other public facing documents    | -  UMN, API, DEV, other public facing documents    |
|                                                    |                                                    |                                                    |
|                                                    | -  PD, HLD, CDR, other internal documents          |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Stages                                             | 1. Import of the documentation change by Huawei in | 1. Review of the documentation change in target    |
|                                                    |    doc-exports repo (html)                         |    document repository                             |
|                                                    |                                                    |                                                    |
|                                                    | 2. Conversion of the documentation to target       | 2. Resolve potential conflicts                     |
|                                                    |    document repository (rst)                       |                                                    |
|                                                    |                                                    | 3. Approve and gate documentation change in target |
|                                                    | 3. Review of the documentation change in target    |    document repository                             |
|                                                    |    document repository                             |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | 4. Approve and gate documentation change in target |                                                    |
|                                                    |    document repository                             |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | 5. Approve and gate documentation change in        |                                                    |
|                                                    |    doc-exports repo                                |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | 6. Zuul automatically creates documentation change |                                                    |
|                                                    |    in Github repo                                  |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+


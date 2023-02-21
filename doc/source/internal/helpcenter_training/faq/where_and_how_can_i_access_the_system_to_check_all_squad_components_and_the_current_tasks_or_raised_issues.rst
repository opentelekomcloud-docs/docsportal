.. _where_and_how_can_i_access_the_system_to_check_all_squad_components_and_the_current_tasks_or_raised_issues:

===========================================================================================================
Where and how can I access the system to check all squad components and the current tasks or raised issues?
===========================================================================================================

There are multiple places based on source of the review task. All Gitea links are related to Huawei changes and changes being introduced on the PREPROD docportal:

-  https://gitea.eco.tsi-dev.otc-service.com/docs/doc-exports/pulls - general place where Huawei is introducing new PRs with the documents imports in HTML file (this is meta repository and not the final repository for a review of the change)

-  https://gitea.eco.tsi-dev.otc-service.com/docs/TARGET-SERVICE-NAME/pulls - this is place where Huawei's PRs are converted to service RST PRs which are ready for a review by QA/UAT for example https://gitea.eco.tsi-dev.otc-service.com/docs/resource-template-service/pulls

-  https://gitea.eco.tsi-dev.otc-service.com/org/docs/teams/docs-orchestration-rw/repositories - good starting point for seeing all service doc repositories of the whole squad for PREPROD documentation

-  https://github.com/opentelekomcloud-docs/TARGET-SERVICE-NAME/pulls - this is place where PRs are being created for changes coming from gitea after approval or from external changes (customer/TSI..) for example  https://github.com/opentelekomcloud-docs/resource-template-service/pulls

-  https://github.com/orgs/opentelekomcloud-docs/teams/docs-orchestration-rw/repositories - good starting point for seeing all service doc repositories of the whole squad for PROD documentation


.. note::

   In future we plan to implement also some monitoring dashboard to have all different PRs under one roof


There are multiple places based on source of the issue. All Gitea links are related to issues addressed to Huawei or Ecosystem squad and issues related to PREPROD doc portal

-  https://gitea.eco.tsi-dev.otc-service.com/docs/docsportal/issues - general PREPROD docsportal issues 

-  https://gitea.eco.tsi-dev.otc-service.com/docs/TARGET-SERVICE-NAME/issues - this is place for service based issue towards Huawei or Ecosystem squad for PREPROD for example https://gitea.eco.tsi-dev.otc-service.com/docs/resource-template-service/issues

-  https://github.com/opentelekomcloud-docs/docsportal/issues - general PROD docsportal issues (also customers can raise the issues here)

-  https://github.com/opentelekomcloud-docs/TARGET-SERVICE-NAME/issues - this is place for service based issue towards TSI (also customers can raise issues here) for PROD for example https://github.com/opentelekomcloud-docs/resource-management-service/issues

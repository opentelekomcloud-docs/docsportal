======================================================
User Guide for the Open Telekom Cloud Status Dashboard
======================================================

Welcome to the Open Telekom Cloud Status Dashboard – your go-to
resource for monitoring the availability of various components in
different regions. This guide is tailored for IT professionals to
navigate and extract valuable insights from the Open Telekom Cloud
platform.

This documentation has two major parts: The first section is
explaining in a hands-on fashion how the Status Dashboard works: where
to find its overview, how to understand the semaphore levels for the
Open Telekom cloud services, and how to access its extra features. See
section [Accessing the Status Dashboard website](#Accessing the Status
Website). To find out more how those metrics are obtained in order to
derive potential actions for your cloud workloads, see section
[Background Information](#background information).


Find Information about the Open Telekom Cloud's status
======================================================

The status Dashboard is an application you access with any web
browser. This section explains the structure of the dashboard.

Accessing the Status Website
----------------------------

Visit the Status Website at https://status.otc-service.com/.

Selecting Regions
-----------------

The platform supports multiple regions. Choose the corresponding tab
for your desired region (e.g., "EU-DE" for Germany or "EU-NL" for the
Netherlands) to assess availability in that specific area.

Service Status
--------------

Services are categorized into sections such as Compute, Network, or
Storage. Each service comes with an icon, also known as a semaphore.

- **Green:** Service fully operational
- **Yellow:** Service available but may have restrictions or slow response
- **Red:** Service unresponsive or experiencing issues
- **Blue with a wrench:** Planned downtime

Incident Displays
-----------------

Current Incidents are displayed above the status area. Incidents are
initially grouped as "Incident" until further analysis and resolution
by a Service Manager. Updates provide real-time information on
incident progress and estimated restoration times.

Incident History
----------------

Access the "Incident History" through the top-right menu. Explore a
comprehensive history of past incidents.

Component Availability
----------------------

Navigate to "Component Availability" in the menu. View component
availability grouped by services for the past months. This feature
offers insights into service performance over an extended period.

Suggestions for Visuals
-----------------------

- Include screenshots of the website interface, emphasizing region
  tabs, service icons, and incident displays.
- Diagrams illustrating the categorization of services and their
  corresponding icons.
- Graphs showcasing historical component availability for a visual
  representation.

Pro Tips
--------

- Bookmark the Status Website for quick access during troubleshooting.
- Leverage incident history to identify recurring patterns and
  potential optimizations.
- Customize notifications based on your region and specific services
  using the platform's alert settings.

Thank you for utilizing Open Telekom Cloud. If you have any queries or
encounter issues, our support team is ready to assist. Happy
monitoring!


Background Information
======================

Understanding Status Semaphores in Open Telekom Cloud

Dear Valued Customers,

We understand that the computation and visualization of status
semaphores in the dashboard might seem intricate, but the underlying
principle is straightforward. Each component within Open Telekom Cloud
comprises one or more services, typically represented by an API
(Application Programmable Interface).

These APIs are utilized by various software applications, cloud
automation tools like Terraform or Ansible, as well as the console or
command-line interface (`openstack`). They adhere to REST standards,
offering endpoints for web services, enabling access to specific
functions of a service following the CRUD paradigm (Create, Retrieve,
Update, Delete). For instance, Compute service resources include
servers (ECS instances), Network service includes IP addresses (EIP)
or subnets, and Blockstorage service involves API calls to manage
Elastic Volumes.

Within the numerous endpoints for Open Telekom Cloud resources, the
Status Dashboard selects a meaningful subset and sends requests to
them, primarily collecting two parameters: the status code and the
response time. A typical response code is 200 for "OK," while 404
indicates a non-existent request, and 503 signifies a communication
failure or server malfunction within an agreed-upon timeframe. A
service is considered operational only if it reports a status code
of 200.

The second parameter, response time, varies depending on factors such
as the type of request and the complexity of service operations. Some
requests involve simple database queries, while others require
accessing multiple resources across clusters, affecting the overall
response time. The Status Dashboard evaluates this data in the context
of historical results.

Certain metrics incur higher costs in terms of computation and are not
as frequently calculated as simpler queries. Therefore, there's no
uniform interval for queries; instead, an optimal and meaningful
utilization of query periods is pursued.

Based on these metrics, the Status Dashboard internally calculates the
presence of certain potentially critical situations. For example, a
low success rate of responses received before timeouts triggers an
"API Low Success Rate" alert. Other internal flags indicate extended
response times or additional error metrics.

It's important to note that while the Status Dashboard can
automatically report suspected cases, final confirmation of normalcy
requires human intervention. Therefore, the Open Telekom Cloud
maintains a dedicated team around the clock to address reported
suspicions. In most cases, these turn out to be false alarms. The
on-duty team regularly reviews values to understand response times and
the circumstances leading to alerts, enabling proactive measures.

We hope this information provides clarity on the workings of our
status monitoring system. Should you have any further questions or
concerns, please don't hesitate to reach out to us.

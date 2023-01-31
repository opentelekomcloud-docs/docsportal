What Can I Do If the System Fails to Switch to Open Telekom Cloud from MyWorkplace on a Client Running Linux OS?
================================================================================================================

**Symptom**

On a client running Linux OS, a user attempts to switch to the **Open Telekom Cloud** page from the **MyWorkplace** page, but the **Open Telekom Cloud** page
fails to be displayed.

**Possible Cause**

The MTU value of the NIC on the device housing the client is greater than the PMTU value, causing loss of large TCP packets.

**Solution**

Perform the following procedure to reduce the MTU value of the NIC:

-  For Community Enterprise Operating System (CentOS), Red Hat Enterprise Linux (RHEL), and Fedora Linux

   1. Log in to the Linux OS using the system account and run the **sudo su root** command to switch to user **root**.

   .. _EN-US_TOPIC_0027928402__li2281496917029:

   2. Run the **ifconfig** command to query the NIC bound to the client host IP address.

   3. Run the following command to open the **ifcfg-**\ *XXX* file:

      ..

         **vi /etc/sysconfig/network-scripts/ifcfg-**\ *XXX*

      .. note::

         *XXX* indicates the NIC bound to the client host IP address queried in :ref:`2 <EN-US_TOPIC_0027928402__li2281496917029>`, such as **eth0**.

   4. Press **i** and run the following command to configure the MTU value of the NIC:

      ..

         **MTU="512"**

      .. note::

         If the MTU value is greater than or equal to 1497, this issue may occur. Therefore, the MTU value must be set to less than or equal to 1496. Setting it to
         512 is recommended.

   5. Press **Esc** and run the **:wq!** command to save the configuration and exit.

   6. Run the following command to restart the network:

      ..

         **service network restart**

-  For SUSE Linux OS

   1. Log in to the Linux OS using the system account and run the **sudo su root** command to switch to user **root**.

   .. _EN-US_TOPIC_0027928402__li2833310617613:

   2. Run the **ifconfig** command to query the NIC bound to the client host IP address.

   3. Run the following command to open the **ifcfg-**\ *XXX* file:

      ..

         **vi /etc/sysconfig/network/ifcfg-**\ *XXX*

      .. note::

         *XXX* indicates the NIC bound to the client host IP address queried in :ref:`2 <EN-US_TOPIC_0027928402__li2833310617613>`, such as **eth0**.

   4. Press **i** and run the following command to configure the MTU value of the NIC:

      ..

         **MTU="512"**

      .. note::

         If the MTU value is greater than or equal to 1497, this issue may occur. Therefore, the MTU value must be set to less than or equal to 1496. Setting it to
         512 is recommended.

   5. Press **Esc** and run the **:wq!** command to save the configuration and exit.

   6. Run the following command to restart the network:

      ..

         **service network restart**

-  For Debian and Ubuntu Linux

   1. Log in to the Linux OS using the system account and run the **sudo su root** command to switch to user **root**.

   2. Run the following command to open the **interfaces** file:

      ..

         **vi /etc/network/interfaces**

   3. Press **i** and run the following command to configure the MTU value of the NIC:

      ..

         **mtu 512**

      .. note::

         If the MTU value is greater than or equal to 1497, this issue may occur. Therefore, the MTU value must be set to less than or equal to 1496. Setting it to
         512 is recommended.

   4. Press **Esc** and run the **:wq!** command to save the configuration and exit.

   5. Run the following command to restart the network:

      ..

         **/etc/init.d/networking restart**

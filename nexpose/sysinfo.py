#! /usr/bin/python

<?xml version="1.0" encoding="UTF-8"?>
<LoginRequest user-id="nxadmin" password="nxadmin" />

<!DOCTYPE LoginResponse [
<!ELEMENT LoginResponse (Failure?)>
<!-- the session id to be used with all subsequent requests -->
<!ATTLIST LoginResponse session-id CDATA #REQUIRED>
<!-- set to 1 upon success, 0 otherwise -->
<!ATTLIST LoginResponse success (0|1) #REQUIRED>
]>

<LoginResponse success="1" sessionid="0DA2FE1D69917350BC15B43A60A2F217D77CF522"/>

<?xml version="1.0" encoding="UTF-8"?>
<LogoutRequest session-id="${Login#Response#//LoginResponse[1]
/@session-id}" />

<LogoutResponse success="1"/>

<?xml version="1.0" encoding="utf-8"?>
<SystemInformationRequest session-id="${Login#Response#//LoginResponse
[1]/@session-id}">
</SystemInformationRequest>

<!DOCTYPE SystemInformationResponse[
<!ELEMENT SystemInformationResponse (SystemInformationSummary)>
<!ATTLIST SystemInformationResponse success (0|1) #REQUIRED>
<!-- set to 1 upon success, 0 otherwise -->
<!ELEMENT SystemInformationSummary (Statistic*)>
<!ELEMENT Statistic CDATA #IMPLIED>
<!ATTLIST Statistic name (cpu-count|cpu-speed|diskinstall|java-name|
jre-version|last-update-date|last-update-id|disk-tmp|nscname|nsc-version|nse-version|os|ram-free|ram-total|uptime|db-product|db-version|java-heap-max|java-heapcommitted|java-heap-free|java-heap-used|java-total-threadcount|java-started-thread-count|java-thread-peak-count|javadaemon-thread-count)
#IMPLIED>
]>

<SystemInformationResponse success="1">
<StatisticsInformationSummary>
<Statistic name="cpu-count">2</Statistic>
<Statistic name="cpu-speed">2660</Statistic>
<Statistic name="diskinstall">/opt/rapid7/nexpose=32901904</Statistic>
<Statistic name="disk-tmp">../shared/temp=32901904</Statistic>
<Statistic name="os">Ubuntu Linux 12.04</Statistic>
<Statistic name="ram-free">170376</Statistic>
<Statistic name="ram-total">8177868</Statistic>
<Statistic name="up-time">45757264</Statistic>
<Statistic name="db-product">postgresql</Statistic>
<Statistic name="db-version">PostgreSQL 9.0.13 on x86_64-
unknown-linux-gnu, compiled by GCC gcc (GCC) 4.1.2 20080704 (Red
Hat 4.1.2-52), 64-bit</Statistic>
<Statistic name="java-name">Java HotSpot(TM) 64-Bit Server
VM</Statistic>
<Statistic name="java-heap-max">6263537664</Statistic>
<Statistic name="java-heap-committed">4829077504</Statistic>
<Statistic name="java-heap-free">3694844920</Statistic>
<Statistic name="java-heap-used">2568692744</Statistic>
<Statistic name="jre-version">24.0-b56</Statistic>
<Statistic name="nsc-name">CN=NeXpose Security Console,
O=Rapid7</Statistic>
<Statistic name="nsc-version">5.12.2</Statistic>
<Statistic name="last-update-date">1423140440496</Statistic>
<Statistic name="last-update-id">1028948869</Statistic>
<Statistic name="java-daemon-thread-count">44</Statistic>
<Statistic name="java-total-thread-count">67</Statistic>
<Statistic name="java-thread-peak-count">118</Statistic>
<Statistic name="java-started-thread-count">4950</Statistic>
</StatisticsInformationSummary>
</SystemInformationResponse>

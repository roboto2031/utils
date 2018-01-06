#! /usr/bin/perl

use IO::Socket::INET;

$sock = IO::Socket::INET->new('172.30.128.61:4321') or die "ERROR can not connect\n";
while (1)
{
	$data = <STDIN>;
	$sock->send($data);
}
$sock->close();


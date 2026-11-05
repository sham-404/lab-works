set ns [new Simulator]

$ns namtrace-all [open out.nam w]
$ns trace-all [open out.tr w]

proc finish {} {
    global ns
    $ns flush-trace
    exec nam out.nam &
    exit 0
}

# Create 4 nodes
for {set i 0} {$i < 4} {incr i} {
    set n($i) [$ns node]
}

# Duplex links: 10Mbps bandwidth, 10ms delay, DropTail queue
$ns duplex-link $n(0) $n(1) 10Mb 10ms DropTail
$ns duplex-link $n(1) $n(3) 10Mb 10ms DropTail
$ns duplex-link $n(2) $n(1) 10Mb 10ms DropTail

# Node positioning for visual layout in NAM
$ns duplex-link-op $n(0) $n(1) orient right-down
$ns duplex-link-op $n(2) $n(1) orient right-up
$ns duplex-link-op $n(1) $n(3) orient right

# Traffic Flow 1: TCP/FTP from Node 0 to Node 3
set tcp [new Agent/TCP]
set sink [new Agent/TCPSink]
$ns attach-agent $n(0) $tcp
$ns attach-agent $n(3) $sink
$ns connect $tcp $sink
set ftp [new Application/FTP]
$ftp attach-agent $tcp

# Traffic Flow 2: UDP/CBR from Node 2 to Node 3
set udp [new Agent/UDP]
set null [new Agent/Null]
$ns attach-agent $n(2) $udp
$ns attach-agent $n(3) $null
$ns connect $udp $null
set cbr [new Application/Traffic/CBR]
$cbr attach-agent $udp

# Break link n(1)-n(3) at 1.0s, restore at 2.0s
$ns rtmodel-at 1.0 down $n(1) $n(3)
$ns rtmodel-at 2.0 up $n(1) $n(3)

# Enable Link State Routing Protocol
$ns rtproto LS

# Event Timings
$ns at 0.1 "$ftp start"
$ns at 0.2 "$cbr start"
$ns at 5.0 "finish"

$ns run

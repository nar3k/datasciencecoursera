set port1 0
set port2 4
set group 10
set ip 10.10.0.8
puts "Connecting to the chassis"
set bps [bps::connect $ip admin admin]
#test create a connection
puts "Creating chassis object"
set chassis1 [$bps getChassis]    
set group 10
$chassis1 setCardModeBPS 1  
#reserve ports
puts "Reserving ports"
$chassis1 reservePort 1 $port1 -group $group
$chassis1 reservePort 1 $port2 -group $group
#create a network
puts "Creating a network"
set network [$bps createNetwork];        
#give a name to a network
$network configure -name Routed_network
#adding interfaces
$network add interface -id "interface1" -number 1 -mac_address "0A:00:00:01:01:01"  -duplicate_mac_address 1
$network add interface -id "interface2" -number 2 -mac_address "0A:00:00:01:01:02"  -duplicate_mac_address 1
#adding routers
$network add ip_router -id "Router1" -default_container "interface1" -ip_address "1.1.1.2" -netmask 24 -gateway_ip_address "1.1.1.1"
$network add ip_router -id "Router2" -default_container "interface2" -ip_address "2.2.2.2" -netmask 24 -gateway_ip_address "2.2.2.1"
#adding endpoints
$network add ip_static_hosts -id "static_host_1" -default_container "Router1" -tags "host1" -ip_address "3.3.3.2" -count 250 -gateway_ip_address "3.3.3.1" -netmask 24
$network add ip_static_hosts -id "static_host_2" -default_container "Router2" -tags "host2" -ip_address "4.4.4.2" -count 250 -gateway_ip_address "4.4.4.1" -netmask 24
$network save -name Routed_network -force 
#================================================================================================
puts "Looking for max CPS"


set test1 [$bps createTest -name "CPS"]
$test1 configure -neighborhood Routed_network
$test1 configure -dut SRX
set comp1 [$test1 createComponent sessionsender CPS]
set  cpsMAX 5000
set  cpsSTEP 50
set failSTEP 50
$comp1 configure -payload.transport tcp
$comp1 configure -payloadSizeDist.type constant
$comp1 configure -payloadSizeDist.min 1400     
$comp1 configure -sessions.max $cpsMAX 
$comp1 configure -sessions.maxPerSecond $cpsMAX  
set time [expr $cpsMAX/$cpsSTEP]
$comp1 configure -rampDist.up [expr int($time/3600)]:[expr [expr int($time/60)]%60]:[expr int($time%60) %60 + 10]
unset time
$comp1 configure -packetsPerSession 0
$comp1 configure -rampDist.upBehavior full+data+close 
$comp1 configure -rampUpProfile.interval 1
$comp1 configure -rampUpProfile.increment $cpsSTEP 
$comp1 configure -rampUpProfile.max $cpsMAX 
$comp1 configure -rampUpProfile.min $cpsSTEP 
$comp1 configure -rampUpProfile.type step 
$comp1 configure -rampDist.steady 00:00:10
$comp1 configure -client_tags host1
$comp1 configure -server_tags host2 

set rateList 0
set print true
proc cancel_after_cps {testid statvals} {
global print
global failSTEP
global test1
global rateList
if {[dict exist $statvals tcpAttemptRate] && [dict exist $statvals tcpClientEstablishRate] && $print } {
puts "time: [expr int([dict get $statvals time])]"
puts "tcpAttemptRate: [dict get $statvals tcpAttemptRate]"
puts "tcpClientEstablishRate: [dict get $statvals tcpClientEstablishRate]"
if {[dict exist $statvals tcpClientClosedByReset] && [expr [dict get $statvals tcpClientClosedByReset] > $failSTEP] } {
puts "Found top value - canceling the test"
set print false
$test1 cancel
} elseif {[dict get $statvals tcpAttemptRate] > [lindex $rateList [expr [llength $rateList]-1]]} {
lappend rateList [dict get $statvals tcpAttemptRate]
}
}
}

puts "clearing..."
#just in case - if called 
proc print_rtstats {testid statvals} {
dict for {var val} $statvals {
puts "$var: $val"
}
}

$test1 run  -rtstats cancel_after_cps -group $group

#clearing double values in ratelist
set rateListCleared 0
for {set i 1} {$i < [expr [llength $rateList] -1]} { incr i} {
global rateList
global rateListCleared
if {[lindex $rateList $i] != [lindex $rateList [expr $i + 1]]} {
lappend rateListCleared [expr int([lindex $rateList $i])]
}
}
puts "MAX_CPS:[lindex $rateListCleared [expr [llength $rateListCleared] -1]]"

itcl::delete object $comp1
itcl::delete object $test1
itcl::delete object $chassis1
itcl::delete object $bps

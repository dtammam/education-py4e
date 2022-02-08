'''
Switch Config

    First off, no pressure but I finished this last night in Powershell. lol 
    LIke I said through text, I think this is the kind of thing that Powershell is way better at than any other language but I'm curious to see what you come up with in Python.

    The idea is to build a switch config based on the data in the spreadsheet. Each row contains the necessary information for 1 port. Attached is the output from when I ran my script but I'll try to lay out the conditions.

    First off, every port config starts with a description. From there, a port will either be an access port or a trunk port. The command will either be switchport mode access or switchport mode trunk

    If an access port, the config would be as follows (bold are variables from spreadsheet):
        description desc
        switchport mode access
        switchport access vlan Access_VLAN
        spanning-tree portfast
        spanning-tree bpdugard enable
        switchport nonegotiate
        spanning-tree guard root

    If a port is an access port and has a value in the Voice_VLAN column, then that port also gets
        switchport voice vlan Voice_VLAN
        auto qos trust
        auto qos voip cisco-phone

    If a port is a trunk, you get the following:
        switchport mode trunk
        switchport nonegotiate
        switchport trunk allowed vlan add Trunk_Allowed_VLANs
        switchport trunk native vlan Trunk_Native_VLAN

    If a port is a trunk and has a value in the Port_Channel_Member field, it also gets:
        channel-group Port_Channel_Member mode Port_Channel_Mode

    The script should output the config to a text file and I have included my output for reference. Also, between each port config, put a !
    And don't bother with error checking. Assume the person running the script will have all the proper data in the spreadsheet, the spreadsheet will exist, etc.
'''


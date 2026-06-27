---
title: "Create a SpeedPak Configuration Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_SpeedPak_Example_VB.htm"
---

# Create a SpeedPak Configuration Example (VBA)

This example shows how to create a SpeedPak configuration for the active configuration.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Open an assembly.
 '
 ' Postconditions:
 ' 1. Adds active_configuration (Default_speedpak) to the
 '    ConfigurationManager.
 ' 2. Click the ConfigurationManager tab and expand Default.
 '---------------------------------------------------------------------------
Option Explicit
Sub main()
    Dim SwApp As SldWorks.SldWorks
     Dim Part As SldWorks.ModelDoc2
     Dim boolstatus As Boolean
     Dim ConfigMgr As SldWorks.ConfigurationManager
    Set SwApp = Application.SldWorks
     If SwApp Is Nothing Then Exit Sub
    Set Part = SwApp.ActiveDoc
     Set ConfigMgr = Part.ConfigurationManager

    ' Add a SpeedPak configuration with a part/body selection threshold of 0.5 to the active configuration
     ConfigMgr.AddSpeedPak2 1, 0.5
     boolstatus = Part.ForceRebuild3(False)
End Sub
```

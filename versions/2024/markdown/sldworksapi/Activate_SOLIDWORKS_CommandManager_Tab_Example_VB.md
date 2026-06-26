---
title: "Activate SOLIDWORKS CommandManager Tab Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Activate_SOLIDWORKS_CommandManager_Tab_Example_VB.htm"
---

# Activate SOLIDWORKS CommandManager Tab Example (VBA)

This example shows how to activate a SOLIDWORKS CommandManager tab.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Open a part.
 '
 ' Postconditions:
 ' 1. Inspect the Immediate window for the SOLIDWORKS CommandManager tab
 '    information.
 ' 2. Inspect the CommandManager.
 '      * Sketch tab is activated.
 '      * Mold Tools tab (tab index 5) is visible.
 ' ---------------------------------------------------------------------------
Dim swApp           As SldWorks.SldWorks
 Dim swModelDoc      As SldWorks.ModelDoc2
 Dim swModelDocExt   As SldWorks.ModelDocExtension
 Dim retval          As Boolean
 Dim cmdTabs         As Variant
 Dim activeTab       As String
 Dim activeTabIndex  As Long
Option Explicit
 Sub main()
    Set swApp = Application.SldWorks
     Set swModelDoc = swApp.ActiveDoc
     Set swModelDocExt = swModelDoc.Extension

    'Get SOLIDWORKS CommandManager tabs
     cmdTabs = swModelDocExt.GetCommandTabs

     'Active CommandManager tab is "Features"
     activeTab = swModelDocExt.ActiveCommandTab
     Debug.Print "Active tab is " & activeTab

     activeTabIndex = swModelDocExt.ActiveCommandTabIndex
     Debug.Print "Active tab index is " & activeTabIndex

     'Tab with index 5 is not visible
     retval = swModelDocExt.CommandTabVisible(5)
     Debug.Print "Tab with index 5 is visible? " & retval

    'Set the active CommandManager tab
     swModelDocExt.ActiveCommandTab = "Sketch"
     activeTabIndex = swModelDocExt.ActiveCommandTabIndex

     'Make tab with index 5 visible
     swModelDocExt.CommandTabVisible(5) = True
End Sub
```

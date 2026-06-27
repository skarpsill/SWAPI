---
title: "Activate SOLIDWORKS CommandManager Tab Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Activate_SOLIDWORKS_CommandManager_Tab_Example_VBNET.htm"
---

# Activate SOLIDWORKS CommandManager Tab Example (VB.NET)

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

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swModelDoc As ModelDoc2
     Dim swModelDocExt As ModelDocExtension
     Dim retval As Boolean
     Dim cmdTabs As Object
     Dim activeTab As String
     Dim activeTabIndex As Integer

     Sub main()

         swModelDoc = swApp.ActiveDoc
         swModelDocExt = swModelDoc.Extension

         'Get SOLIDWORKS CommandManager tabs
         cmdTabs = swModelDocExt.GetCommandTabs
         'Active CommandManager tab is "Features"
         activeTab = swModelDocExt.ActiveCommandTab
         Debug.Print("Active tab is " & activeTab)
         activeTabIndex = swModelDocExt.ActiveCommandTabIndex
         Debug.Print("Active tab index is " & activeTabIndex)
         'Tab with index 5 is not visible
         retval = swModelDocExt.CommandTabVisible(5)
         Debug.Print("Tab with index 5 is visible? " & retval)

         'Set the active CommandManager tab
         swModelDocExt.ActiveCommandTab = "Sketch"
         activeTabIndex = swModelDocExt.ActiveCommandTabIndex
         'Make tab with index 5 visible
         swModelDocExt.CommandTabVisible(5) = True

     End Sub

     Public swApp As SldWorks

 End  Class
```
